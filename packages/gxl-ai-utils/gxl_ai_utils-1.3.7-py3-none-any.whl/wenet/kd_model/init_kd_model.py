import logging
from collections import OrderedDict

import torch

from wenet.branchformer.encoder import BranchformerEncoder
from wenet.e_branchformer.encoder import EBranchformerEncoder
from wenet.efficient_conformer.encoder import EfficientConformerEncoder
from wenet.kd_model.kd_loss import KD_CTC
from wenet.kd_model.kd_model import KD_model, KD_model_2
from wenet.kd_model.teacher_student_class import TeacherStudentModel
from wenet.squeezeformer.encoder import SqueezeformerEncoder
from wenet.transformer.asr_model import ASRModel
from wenet.transformer.cmvn import GlobalCMVN
from wenet.transformer.encoder import TransformerEncoder, ConformerEncoder
from wenet.utils.checkpoint import load_checkpoint, load_trained_modules
from wenet.utils.cmvn import load_cmvn
from wenet.kd_model import kd_utils
from wenet.utils.init_model import init_model


def init_kd_model(args, configs):
    """
    得到kd 模型

    """
    # 加载whisper的encoder
    input_dim = configs['input_dim']  # 在 check_modify_and_save_config 函数中写入
    vocab_size = configs['output_dim']  # 在init_dataset_and_dataloader函数中写入
    whisper_encoder_type = configs.get('whisper_encoder', 'transformer')
    whisper_encoder = None
    if whisper_encoder_type == 'transformer':
        whisper_encoder = TransformerEncoder(input_dim,
                                             global_cmvn=None,
                                             **configs['whisper_encoder_conf'])
        print(whisper_encoder)
        if configs['whisper_checkpoint'] is not None:
            kd_utils.load_whisper_encoder_origin_param(whisper_encoder, configs)
    else:
        logging.error('not support whisper_encoder_type: %s', whisper_encoder_type)
    student_model, config = init_model(args, configs)
    ctc4whisper = KD_CTC(vocab_size, whisper_encoder.output_size(),
                         blank_id=configs['ctc_conf']['ctc_blank_id']
                         if 'ctc_conf' in configs else 0
                         )
    whisper_model = TeacherStudentModel(whisper_encoder, ctc4whisper)
    if configs.get('frozen_teacher', True):
        for p in whisper_model.encoder.parameters():
            p.requires_grad = False

    kd_model = KD_model_2(whisper_model, student_model)
    logging.info('init kd model success, 参数如下：-------------------------')
    num_params_wh = sum(p.numel() for p in kd_model.whisper_model.parameters())
    logging.info('whisper_model num_params: {}M'.format(num_params_wh / 1e6))
    num_params_stu = sum(p.numel() for p in kd_model.student_model.parameters())
    logging.info('student_model num_params: {}M'.format(num_params_stu / 1e6))

    if hasattr(args, 'checkpoint') and args.checkpoint is not None:
        infos = load_checkpoint(kd_model, args.checkpoint)
    elif hasattr(args, 'checkpoint') and args.enc_init is not None:
        infos = load_trained_modules(kd_model, args)
    else:
        infos = {}
    configs["init_infos"] = infos
    logging.info(f'耿雪龙：configs:{configs}')
    return kd_model, configs
