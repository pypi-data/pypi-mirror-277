import os
import gradio as gr
import zipfile

from .util import lib_dcm2nii
from .util import lib_common

EXAMPLE_DICOM_DIR_PATH = 'D:/project/xxx/Task/ABC_Test_02/xxx'
EXAMPLE_NII_DIR_PATH = 'D:/project/res/'
EXAMPLE_DICOM_ZIP_JPG = os.path.join(os.path.dirname(__file__), "./resources/image/example_dicom_zip.jpg")
EXAMPLE_DICOM_DIR_JPG = os.path.join(os.path.dirname(__file__), "./resources/image/example_dicom_dir.jpg")
CONCURRENCY_LIMIT = 3


def service_local_dicom_to_nii(dicom_dir_path, depth, nii_dir_path, gz, image):
    print(f"===> service_local_dicom_to_nii: {dicom_dir_path} to {nii_dir_path}")
    # 校验
    if not dicom_dir_path or dicom_dir_path.strip() == "" or not os.path.isdir(dicom_dir_path):
        gr.Warning(f"请填入正确的[dicom文件目录路径]，例如'{EXAMPLE_DICOM_DIR_PATH}'")
        return
    if not nii_dir_path or nii_dir_path.strip() == "":
        gr.Info("未填写nii文件路径，将使用dicom目录的父目录")
        nii_dir_path = os.path.abspath(os.path.join(dicom_dir_path, ".."))

    try:
        nii_dir_path = os.path.join(nii_dir_path, lib_common.generate_dir_name())
        if not os.path.exists(nii_dir_path) or not os.path.isdir(nii_dir_path):
            os.mkdir(nii_dir_path)

        result_code = lib_dcm2nii.dicom_to_nii(os.path.abspath(dicom_dir_path), os.path.abspath(nii_dir_path), depth,
                                               gz)
        if result_code == 0:
            # json_file, nii_file = get_latest_nii_file(nii_dir_path)
            return nii_dir_path, lib_common.get_all_nii_file(nii_dir_path)
        else:
            raise gr.Error("dicom 转 nii 时，发生异常，请确保填入了正确的dicom文件目录。异常码为：" + str(result_code))
    except Exception as e:
        raise gr.Error("dicom 转 nii 时，发生异常，请确保填入了正确的dicom文件目录。异常信息为：" + str(e))


local_iface = gr.Interface(
    fn=service_local_dicom_to_nii,
    inputs=[
        gr.Textbox(label="dicom文件目录路径（必填）",
                   info=f"例如'{EXAMPLE_DICOM_DIR_PATH}'，下面有多个目录存放各自的dicom文件时，将会分别自动处理"),
        gr.Radio(label="dicom目录的搜索深度",
                 info="directory search depth. Convert DICOMs in sub-folders of in_folder? (0..9, default 5)",
                 choices=list(range(1, 10)), value=5),
        gr.Textbox(label="保存nii文件目录路径（可选）",
                   info=f"例如'{EXAMPLE_NII_DIR_PATH}'。如果不填，会输出到dicom的父目录下。"),
        gr.Radio(label="nii文件的压缩选项",
                 info="gz compress images (y/i/n/3, default n) [y=pigz, i=internal:miniz, n=no, 3=no,3D]",
                 choices=["y", "i", "n", "3"], value="n"),
        gr.Image(label="dicom目录示例（下面存放所有的*.dcm文件）", value=EXAMPLE_DICOM_DIR_JPG,
                 interactive=False),

    ],
    outputs=[gr.Text(label="nii文件目录路径"), gr.Files(label="保存nii文件目录下的nii文件")],
    description="在本地电脑端启动时使用，点击【开始转换】按钮执行转换。",
    allow_flagging="never",
    submit_btn="开始转换",
    clear_btn=gr.Button(value="clear", interactive=False, visible=False),
    concurrency_limit=CONCURRENCY_LIMIT
)


def service_server_dicom_to_nii(file, depth, gz, example_image):
    print(f"===> service_server_dicom_to_nii: {file}")
    # 校验
    if not file or not zipfile.is_zipfile(file.name):
        gr.Warning(f"请传入dicom文件目录的ZIP压缩包，如'dicom.zip'")
        return
    dicom_zipfile_path = file.name

    # 创建本次的工作目录
    save_dir_path = os.path.dirname(dicom_zipfile_path)
    current_work_dir = os.path.join(save_dir_path, lib_common.generate_dir_name())
    os.mkdir(current_work_dir)
    save_dir_path = current_work_dir

    # 解压
    with zipfile.ZipFile(file.name, "r") as zfile:
        # 文件名包含中文时有乱码问题
        zfile.extractall(save_dir_path)

    # dicom 转 nii
    try:
        result_code = lib_dcm2nii.dicom_to_nii(save_dir_path, save_dir_path, depth, gz)
        if result_code == 0:
            return save_dir_path, lib_common.get_all_nii_file(save_dir_path)
        else:
            raise gr.Error("dicom 转 nii 时，发生异常，请确保填入了正确的dicom文件目录。异常码为：" + str(result_code))
    except Exception as e:
        raise gr.Error("dicom 转 nii 时，发生异常：" + str(e))


server_iface = gr.Interface(
    fn=service_server_dicom_to_nii,
    inputs=[
        gr.File(label="dicom文件目录的压缩包（必填，例如'dicom.zip'）"),
        gr.Radio(label="dicom目录的搜索深度",
                 info="directory search depth. Convert DICOMs in sub-folders of in_folder? (0..9, default 5)",
                 choices=list(range(1, 10)), value=5),
        gr.Radio(label="nii文件的压缩选项",
                 info="gz compress images (y/i/n/3, default n) [y=pigz, i=internal:miniz, n=no, 3=no,3D]",
                 choices=["y", "i", "n", "3"], value="n"),
        gr.Image(
            label="dicom压缩包示例（不要带中文，压缩包内每个目录存放各自所有的*.dcm文件。）",
            value=EXAMPLE_DICOM_ZIP_JPG,
            interactive=False
        )
    ],
    outputs=[gr.Text(label="nii文件目录路径"), gr.Files(label="保存nii文件目录下的nii文件")],
    description="在本地电脑端、服务器端启动时皆可使用，点击【开始转换】按钮执行转换。",
    allow_flagging="never",
    submit_btn="开始转换",
    clear_btn=gr.Button(value="clear", interactive=False, visible=False),
    concurrency_limit=CONCURRENCY_LIMIT
)

tabbed_interface = gr.TabbedInterface(
    interface_list=[local_iface, server_iface],
    tab_names=["本地端", "通用端"],
    title="dicom 转 nii"
)
