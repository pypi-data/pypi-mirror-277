from .gradio_interfaces import *


def start_service():
    tabbed_interface.launch(inbrowser=True, server_name='0.0.0.0')


if __name__ == '__main__':
    start_service()
