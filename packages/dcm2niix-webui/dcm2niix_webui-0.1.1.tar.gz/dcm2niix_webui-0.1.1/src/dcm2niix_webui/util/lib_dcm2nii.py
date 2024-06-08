import os


def dicom_to_nii(dicom_dir_path: str, nii_dir_path: str, depth: int = 5, gz: str = "n"):
    """
    dicom文件转nii文件
    :param dicom_dir_path: dicom文件目录
    :param nii_dir_path: 转换后要保存的nii文件路径
    :param depth: directory search depth. Convert DICOMs in sub-folders of in_folder? (0..9, default 5)
    :param gz: gz compress images (y/i/n/3, default n) [y=pigz, i=internal:miniz, n=no, 3=no,3D]
    :return: None
    """

    result_code = os.system(rf'dcm2niix.exe -o "{nii_dir_path}" -z {gz}  -d {depth} "{dicom_dir_path}"')
    return result_code
