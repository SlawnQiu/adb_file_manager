# -*- coding: utf-8 -*-
# 下载文件子进程
import os

from PyQt5.QtCore import QThread, pyqtSignal


class DownloadFileThread(QThread):
    signal = pyqtSignal(str)  # 自定义信号对象。参数str就代表这个信号可以传一个字符串

    def __init__(self, filepath, target, local_path):
        super(DownloadFileThread, self).__init__()
        self.filepath = filepath
        self.target = target
        self.local_path = local_path

    def run(self):
        download_order = "adb pull " '"' + self.filepath + self.target + '"' + ' "' + self.local_path + '"'
        result = os.popen(download_order)
        result = result.buffer.read().decode(encoding='utf8')
        self.signal.emit(str(result))