import logging
import os
from typing import List, Dict

from torch import nn
import torch
from wenet.kd_model.teacher_student_class import TeacherStudentModel
import torch.nn.functional as F
from wenet.kd_model.kd_loss import KD_KLLoss, KD_MSELoss
from wenet.kd_model.kd_utils import do_repeat_for_consistent
from wenet.transformer.search import DecodeResult
from wenet.utils.context_graph import ContextGraph
from wenet.transformer.asr_model import ASRModel


class KD_model(nn.Module):
    def __init__(self,
                 paraformer_model: TeacherStudentModel,
                 whisper_model: TeacherStudentModel,
                 student_model: TeacherStudentModel):
        super(KD_model, self).__init__()
        self.kl_loss = KD_KLLoss()
        self.mse_loss = KD_MSELoss()
        self.paraformer_model = paraformer_model
        self.whisper_model = whisper_model
        self.student_model = student_model

    def forward(self,
                batch: dict,
                device: torch.device,
                ):
        """
        学生模型采用whisper的前端输入

        Returns:

        """
        speech4pa: torch.Tensor = batch["feats4pa"].to(device)
        speech_lengths4pa: torch.Tensor = batch["feats_lengths4pa"].to(device)
        speech4wh: torch.Tensor = batch["feats"].to(device)
        speech_lengths4wh: torch.Tensor = batch["feats_lengths"].to(device)
        text: torch.Tensor = batch["target"].to(device)
        text_lengths: torch.Tensor = batch["target_lengths"].to(device)
        assert text_lengths.dim() == 1, text_lengths.shape
        # Check that batch_size is unified
        assert (speech4pa.shape[0] == speech_lengths4pa.shape[0] == speech4wh.shape[0] == speech_lengths4wh.shape[0] ==
                text.shape[0] ==
                text_lengths.shape[0]), (speech4wh.shape, speech_lengths4wh.shape,
                                         speech4pa.shape, speech_lengths4pa.shape,
                                         text.shape, text_lengths.shape)

        ctc_loss4pa, logits4pa, _ = self.paraformer_model(speech4pa, speech_lengths4pa, text, text_lengths)
        ctc_loss4wh, logits4wh, enc_out_wh = self.whisper_model(speech4wh, speech_lengths4wh, text, text_lengths)
        ctc_loss4stu, logits4stu, enc_out_stu = self.student_model(speech4wh, speech_lengths4wh, text, text_lengths)

        logits4pa_padding = do_repeat_for_consistent(logits4pa, logits4wh)

        loss_mse = self.mse_loss(enc_out_wh, enc_out_stu)

        kd_loss4pa = self.kl_loss(logits4stu, logits4pa_padding)
        kd_loss4wh = self.kl_loss(logits4stu, logits4wh)
        loss = loss_mse + ctc_loss4pa + ctc_loss4wh + ctc_loss4stu + kd_loss4pa + kd_loss4wh
        return {
            'loss': loss,
            'ctc_loss4pa': ctc_loss4pa,
            'ctc_loss4wh': ctc_loss4wh,
            'ctc_loss4stu': ctc_loss4stu,
            'kd_loss4pa': kd_loss4pa,
            'kd_loss4wh': kd_loss4wh,
            'loss_mse': loss_mse
        }

    def decode(
            self,
            methods: List[str],

            keys: List[str],

            speech: torch.Tensor,
            speech_lengths: torch.Tensor,

            speech4pa: torch.Tensor,
            speech_lengths4pa: torch.Tensor,

            beam_size: int,
            decoding_chunk_size: int = -1,
            num_decoding_left_chunks: int = -1,
            ctc_weight: float = 0.0,
            simulate_streaming: bool = False,
            reverse_weight: float = 0.0,
            context_graph: ContextGraph = None,
            big_file: dict = None,
            tokenizer=None
    ):
        encoder_dict = {
            'paraformer': self.paraformer_model,
            'whisper': self.whisper_model,
            'student': self.student_model
        }
        for encoder_name, model in encoder_dict.items():
            results = model.decode(
                methods,
                speech4pa if encoder_name == 'paraformer' else speech,
                speech_lengths4pa if encoder_name == 'paraformer' else speech_lengths,
                beam_size,
                decoding_chunk_size=decoding_chunk_size,
                num_decoding_left_chunks=num_decoding_left_chunks,
                ctc_weight=ctc_weight,
                simulate_streaming=simulate_streaming,
                reverse_weight=reverse_weight,
                context_graph=context_graph)
            files = big_file[encoder_name]
            max_format_len = max([len(mode) for mode in methods])
            for i, key in enumerate(keys):
                for mode, hyps in results.items():
                    tokens = hyps[i].tokens
                    line = '{} {}'.format(key, tokenizer.detokenize(tokens)[0])
                    logging.info('{} {} {}'.format(encoder_name, mode.ljust(max_format_len),
                                                   line))
                    files[mode].write(line + '\n')


class KD_model_2(nn.Module):
    def __init__(self,
                 whisper_model: TeacherStudentModel,
                 student_model: ASRModel):
        super(KD_model_2, self).__init__()
        self.kl_loss = KD_KLLoss()
        self.mse_loss = KD_MSELoss()
        self.whisper_model = whisper_model
        self.student_model = student_model

    def forward(self,
                batch: dict,
                device: torch.device,
                ):
        """
        学生模型采用whisper的前端输入

        Returns:

        """
        ctc_loss4wh, logits4wh, enc_out_wh = self.whisper_model(batch, device)
        dict_res = self.student_model(batch, device)
        loss = dict_res["loss"]
        loss_att = dict_res["loss_att"]
        loss_ctc = dict_res["loss_ctc"]
        encoder_out = dict_res["encoder_out"]
        ctc_probs = dict_res["ctc_probs"]

        loss_mse = self.mse_loss(enc_out_wh, encoder_out)
        kd_loss4wh = self.kl_loss(ctc_probs, logits4wh)
        loss_all = 0.2*loss_mse + ctc_loss4wh + 0.8*kd_loss4wh + loss
        return {
            'loss': loss_all,
            'ctc_loss4wh': ctc_loss4wh,
            'kd_loss4wh': kd_loss4wh,
            'mse_loss4wh': loss_mse,
            'loss_att': loss_att,
            'loss_ctc': loss_ctc,
            'loss_stu': loss
        }

    def decode(
            self,
            methods: List[str],

            keys: List[str],

            speech: torch.Tensor,
            speech_lengths: torch.Tensor,

            speech4pa: torch.Tensor,
            speech_lengths4pa: torch.Tensor,

            beam_size: int,
            decoding_chunk_size: int = -1,
            num_decoding_left_chunks: int = -1,
            ctc_weight: float = 0.0,
            simulate_streaming: bool = False,
            reverse_weight: float = 0.0,
            context_graph: ContextGraph = None,
            big_file: dict = None,
            tokenizer=None
    ):
        encoder_dict = {
            'paraformer': self.paraformer_model,
            'whisper': self.whisper_model,
            'student': self.student_model
        }
        for encoder_name, model in encoder_dict.items():
            results = model.decode(
                methods,
                speech4pa if encoder_name == 'paraformer' else speech,
                speech_lengths4pa if encoder_name == 'paraformer' else speech_lengths,
                beam_size,
                decoding_chunk_size=decoding_chunk_size,
                num_decoding_left_chunks=num_decoding_left_chunks,
                ctc_weight=ctc_weight,
                simulate_streaming=simulate_streaming,
                reverse_weight=reverse_weight,
                context_graph=context_graph)
            files = big_file[encoder_name]
            max_format_len = max([len(mode) for mode in methods])
            for i, key in enumerate(keys):
                for mode, hyps in results.items():
                    tokens = hyps[i].tokens
                    line = '{} {}'.format(key, tokenizer.detokenize(tokens)[0])
                    logging.info('{} {} {}'.format(encoder_name, mode.ljust(max_format_len),
                                                   line))
                    files[mode].write(line + '\n')