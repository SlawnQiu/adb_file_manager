# -*- coding: utf-8 -*-
# 粘贴文件子进程
import os
import time

from PyQt5.QtCore import QThread, pyqtSignal


class PasteThread(QThread):
    signal = pyqtSignal(str)  # 自定义信号对象。参数str就代表这个信号可以传一个字符串

    def __init__(self, tip, source_file, filepath):
        super(PasteThread, self).__init__()
        self.tip = tip
        self.source_file = source_file
        self.filepath = filepath

    def run(self):
        if self.tip == 0:
            self.order = 'adb shell cp -a ' + '"' + self.source_file + '"' + ' ' + '"' + self.filepath + '"'
            print(self.order, self.tip)
            os.popen('adb root')
            os.popen('adb remount')
            os.popen(self.order)
            done = True
            time.sleep(0.1)
            self.signal.emit(str(done))
        elif self.tip == 1:
            self.order = 'adb shell mv -f ' + '"' + self.source_file + '"' + ' ' + '"' + self.filepath + '"'
            print(self.order, self.tip)
            os.popen('adb root')
            os.popen('adb remount')
            os.popen(self.order)
            done = True
            time.sleep(0.1)
            self.signal.emit(str(done))