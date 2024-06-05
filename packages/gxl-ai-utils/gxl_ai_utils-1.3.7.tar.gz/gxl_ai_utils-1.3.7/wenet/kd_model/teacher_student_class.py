import logging
from typing import List, Dict, Tuple

import torch
import torch.nn as nn
from wenet.kd_model.kd_loss import KD_CTC
from wenet.transformer.search import DecodeResult, attention_beam_search, ctc_greedy_search, ctc_prefix_beam_search, \
    attention_rescoring
from wenet.utils.context_graph import ContextGraph


class TeacherStudentModel(nn.Module):
    def __init__(self, encoder, ctc: KD_CTC, freeze_encoder=True):
        """
        学生模型 / 老师模型, 只包含一个encoder和ctc模块
        Args:
            encoder:
            ctc:
        """
        super(TeacherStudentModel, self).__init__()
        self.encoder = encoder
        self.ctc = ctc
        if freeze_encoder:
            for param in self.encoder.parameters():
                param.requires_grad = False

    @torch.jit.unused
    def forward(self,
                batch,
                device
                ):

        speech4wh: torch.Tensor = batch["feats4wh"].to(device)
        speech_lengths4wh: torch.Tensor = batch["feats_lengths4wh"].to(device)
        text: torch.Tensor = batch["target"].to(device)
        text_lengths: torch.Tensor = batch["target_lengths"].to(device)
        assert text_lengths.dim() == 1, text_lengths.shape
        # Check that batch_size is unified
        assert (speech4wh.shape[0] == speech_lengths4wh.shape[0] ==
                text.shape[0] ==
                text_lengths.shape[0]), (speech4wh.shape, speech_lengths4wh.shape,
                                         text.shape, text_lengths.shape)
        # 1. Encoder
        encoder_out, encoder_mask = self.encoder(speech4wh, speech_lengths4wh)
        loss_ctc, res_logits = self._forward_ctc(encoder_out, encoder_mask,
                                                 text, text_lengths)
        return loss_ctc, res_logits, encoder_out

    @torch.jit.unused
    def _forward_ctc(self, encoder_out: torch.Tensor,
                     encoder_mask: torch.Tensor,
                     text: torch.Tensor, text_lengths: torch.Tensor):
        encoder_out_lens = encoder_mask.squeeze(1).sum(1)
        loss_ctc, res_logits = self.ctc(encoder_out, encoder_out_lens, text, text_lengths)
        return loss_ctc, res_logits

    def decode(
            self,
            methods: List[str],

            speech: torch.Tensor,
            speech_lengths: torch.Tensor,

            beam_size: int,
            decoding_chunk_size: int = -1,
            num_decoding_left_chunks: int = -1,
            ctc_weight: float = 0.0,
            simulate_streaming: bool = False,
            reverse_weight: float = 0.0,
            context_graph: ContextGraph = None,
    ) -> Dict[str, List[DecodeResult]]:
        """ Decode input speech

        Args:
            methods:(List[str]): list of decoding methods to use, which could
                could contain the following decoding methods, please refer paper:
                https://arxiv.org/pdf/2102.01547.pdf
                   * ctc_greedy_search
                   * ctc_prefix_beam_search
                   * atttention
                   * attention_rescoring
            speech (torch.Tensor): (batch, max_len, feat_dim)
            speech_length (torch.Tensor): (batch, )
            beam_size (int): beam size for beam search
            decoding_chunk_size (int): decoding chunk for dynamic chunk
                trained model.
                <0: for decoding, use full chunk.
                >0: for decoding, use fixed chunk size as set.
                0: used for training, it's prohibited here
            simulate_streaming (bool): whether do encoder forward in a
                streaming fashion
            reverse_weight (float): right to left decoder weight
            ctc_weight (float): ctc score weight

        Returns: dict results of all decoding methods
        """
        assert speech.shape[0] == speech_lengths.shape[0]
        assert decoding_chunk_size != 0
        encoder_out, encoder_mask = self._forward_encoder(
            speech, speech_lengths, decoding_chunk_size,
            num_decoding_left_chunks, simulate_streaming)
        encoder_lens = encoder_mask.squeeze(1).sum(1)
        ctc_probs = self.ctc.log_softmax(encoder_out)
        results = {}
        if 'attention' in methods:
            logging.warning('teacher_student_class not support attention decoder method')
        if 'ctc_greedy_search' in methods:
            results['ctc_greedy_search'] = ctc_greedy_search(
                ctc_probs, encoder_lens)
        if 'ctc_prefix_beam_search' in methods:
            ctc_prefix_result = ctc_prefix_beam_search(ctc_probs, encoder_lens,
                                                       beam_size, context_graph)
            results['ctc_prefix_beam_search'] = ctc_prefix_result
        if 'attention_rescoring' in methods:
            logging.warning('teacher_student_class not support attention_rescoring decoder method')
        return results
    def _forward_encoder(
        self,
        speech: torch.Tensor,
        speech_lengths: torch.Tensor,
        decoding_chunk_size: int = -1,
        num_decoding_left_chunks: int = -1,
        simulate_streaming: bool = False,
    ) -> Tuple[torch.Tensor, torch.Tensor]:
        # Let's assume B = batch_size
        # 1. Encoder
        if simulate_streaming and decoding_chunk_size > 0:
            encoder_out, encoder_mask = self.encoder.forward_chunk_by_chunk(
                speech,
                decoding_chunk_size=decoding_chunk_size,
                num_decoding_left_chunks=num_decoding_left_chunks
            )  # (B, maxlen, encoder_dim)
        else:
            encoder_out, encoder_mask = self.encoder(
                speech,
                speech_lengths,
                decoding_chunk_size=decoding_chunk_size,
                num_decoding_left_chunks=num_decoding_left_chunks
            )  # (B, maxlen, encoder_dim)
        return encoder_out, encoder_mask
