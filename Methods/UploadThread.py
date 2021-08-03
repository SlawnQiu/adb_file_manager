# -*- coding: utf-8 -*-
# 上传文件子进程
import os

from PyQt5.QtCore import pyqtSignal, QThread


class UploadThread(QThread):
    signal = pyqtSignal(str)  # 自定义信号对象。参数str就代表这个信号可以传一个字符串

    def __init__(self, filepath, local_file):
        super(UploadThread, self).__init__()
        self.filepath = filepath
        self.local_file = local_file

    def run(self):
        upload_order = "adb push " '"' + self.local_file + '"' + ' ' + '"' + self.filepath + '"'
        load_progess = os.popen(upload_order)
        load_progess = load_progess.buffer.read().decode(encoding='utf8')
        self.signal.emit(str(load_progess))