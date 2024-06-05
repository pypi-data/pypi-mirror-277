from gxl_ai_utils.utils import utils_file
import os
kespeech_dir="/home/work_nfs8/xlgeng/new_workspace/wenet_gxl_salmonn/examples/aishell/salmonn/data_list/kespeech"
datanames_list=os.listdir(kespeech_dir)
print(datanames_list)
for dataname in datanames_list:
    if dataname and dataname[0].isupper():
        utils_file.logging_print("开始处理",dataname)
        input_dir=os.path.join(kespeech_dir,dataname,"test")
        wav_dir = os.path.join(input_dir, "wav")
        wav_scp_path = os.path.join(input_dir, "wav.scp")
        # utils_file.copy_file(wav_scp_path, os.path.join(input_dir, "old_wav.scp"))
        # new_wav_dict =  utils_file.do_copy_files_by_manifest(wav_scp_path, wav_dir)
        # utils_file.write_dict_to_scp(new_wav_dict, wav_scp_path)
        text_scp_path = os.path.join(input_dir, "text")
        output_data_list_path = os.path.join(input_dir, "data.list")
        utils_file.do_convert_wav_text_scp_to_jsonl(wav_scp_path, text_scp_path, output_data_list_path)




        