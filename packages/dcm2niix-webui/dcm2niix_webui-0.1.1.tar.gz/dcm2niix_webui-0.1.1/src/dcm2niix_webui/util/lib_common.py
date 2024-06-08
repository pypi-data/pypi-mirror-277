import zipfile
import os
from datetime import datetime


def unzip_dicom_file(zip_file_path: str, save_dir_path: str):
    with zipfile.ZipFile(zip_file_path, "r") as zfile:
        # 文件名包含中文时有乱码问题
        zfile.extractall(save_dir_path)

        # 找到存放dicom文件的目录
        # 如果存在名称为dicom的目录，直接就用
        for info in zfile.infolist():
            if info.is_dir() and info.filename == "dicom":
                return info.filename
        # 否则获取第一个目录，排除MAC上的固定目录
        for info in zfile.infolist():
            if info.is_dir() and not info.filename == "__MACOSX/":
                return info.filename
        # 如果还是找不到，就直接用当前目录
        return "."


def get_latest_nii_file(nii_dir_path: str):
    """
    获取最新转换出的nii文件
    :param nii_dir_path:
    :return: nii文件JSON信息, nii文件
    """
    latest_json_file = ""
    latest_json_file_mtime = 0
    latest_nii_file = ""
    latest_nii_file_mtime = 0
    for file in os.listdir(nii_dir_path):
        file_whole_path = os.path.join(nii_dir_path, file)
        if os.path.isfile(file_whole_path):  # and file.startswith("dicom_T1_RARE_"):
            if file.endswith(".json"):
                json_file_mtime = os.path.getmtime(file_whole_path)
                if json_file_mtime > latest_json_file_mtime:
                    latest_json_file_mtime = json_file_mtime
                    latest_json_file = file_whole_path
            elif file.endswith(".nii.gz") or file.endswith(".nii"):
                nii_file_mtime = os.path.getmtime(file_whole_path)
                if nii_file_mtime > latest_nii_file_mtime:
                    latest_nii_file_mtime = nii_file_mtime
                    latest_nii_file = file_whole_path

    return latest_json_file, latest_nii_file


def get_all_nii_file(nii_dir_path: str):
    """
    获取所有转换出的nii文件
    :param nii_dir_path:
    :return: nii文件列表
    """
    files = []
    for file in os.listdir(nii_dir_path):
        file_whole_path = os.path.join(nii_dir_path, file)
        if os.path.isfile(file_whole_path):
            if file.endswith(".json") or file.endswith(".nii.gz") or file.endswith(".nii"):
                files.append(file_whole_path)
    return files


def generate_dir_name():
    """
    生成目录名称
    :return:
    """
    str_time = datetime.now().strftime('%Y%m%d%H%M%S-%f')
    return "nii-" + str_time
