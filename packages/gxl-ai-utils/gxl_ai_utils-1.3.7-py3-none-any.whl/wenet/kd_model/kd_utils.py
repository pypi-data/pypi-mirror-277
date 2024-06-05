import logging
from collections import OrderedDict

import torch


def load_paraformer_encoder_origin_param(paraformer_encoder, configs):
    checkpoint = torch.load(configs['paraformer_checkpoint'], map_location='cpu')
    # utils_file.print_checkpoint(checkpoint)
    # print(type(checkpoint))
    order_dict_new_checkpoint = OrderedDict()
    for k, v in checkpoint.items():
        if k.startswith('encoder.'):
            name = k[8:]  # remove `encoder.`
            order_dict_new_checkpoint[name] = v
    # utils_file.print_checkpoint(order_dict_new_checkpoint)
    missing_keys, unexpected_keys = paraformer_encoder.load_state_dict(
        order_dict_new_checkpoint, strict=False)
    for key in missing_keys:
        logging.info("missing tensor: {}".format(key))
    for key in unexpected_keys:
        logging.info("unexpected tensor: {}".format(key))


def load_whisper_encoder_origin_param(whisper_encoder, configs):
    checkpoint = torch.load(configs['whisper_checkpoint'], map_location='cpu')
    # utils_file.print_checkpoint(checkpoint)
    # print(type(checkpoint))
    order_dict_new_checkpoint = OrderedDict()
    for k, v in checkpoint.items():
        if k.startswith('encoder.'):
            name = k[8:]  # remove `encoder.`
            order_dict_new_checkpoint[name] = v
    # utils_file.print_checkpoint(order_dict_new_checkpoint)
    missing_keys, unexpected_keys = whisper_encoder.load_state_dict(
        order_dict_new_checkpoint, strict=False)
    for key in missing_keys:
        logging.info("missing tensor: {}".format(key))
    for key in unexpected_keys:
        logging.info("unexpected tensor: {}".format(key))


def do_repeat_for_consistent(input_tensor1, input_tensor2):
    """
    使用repeat的方式在time维度将Tensor1扩展为与Tensor2相同的形状,
    要求两者在batch维度和dim维度相同.
    首先求得Tensor2长度比上Tensor1的倍数,然后让Tensor1中的所有时间步复制该倍数,
    余数处理: 前余数个时间步复制倍数+1倍
    如:
    abc,-> 扩展为9倍,aaabbbccc
    abc,-> 扩展为11倍,aaaabbbbccc
    Args:
        input_tensor1:
        input_tensor2:

    Returns:

    """
    assert (input_tensor1.shape[0] == input_tensor2.shape[0] and
            input_tensor1.shape[2] == input_tensor2.shape[2] and
            input_tensor1.shape[1] <= input_tensor2.shape[1])
    multiple_num = input_tensor2.shape[1] // input_tensor1.shape[1]
    remainder = input_tensor2.shape[1] % input_tensor1.shape[1]
    temp_1 = input_tensor1[:, :remainder, :].repeat(1, multiple_num + 1, 1)
    temp_2 = input_tensor1[:, remainder:, :].repeat(1, multiple_num, 1)
    return torch.cat([temp_1, temp_2], dim=1)
