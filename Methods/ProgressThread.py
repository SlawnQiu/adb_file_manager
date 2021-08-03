# -*- coding: utf-8 -*-
# 进度条子进程
import os

from PyQt5.QtCore import QThread, pyqtSignal


class ProgressThread(QThread):
    signal = pyqtSignal(int)  # 自定义信号对象。参数str就代表这个信号可以传一个字符串

    def __init__(self, local_file, filepath, progress_cond, target, local_path):
        super(ProgressThread, self).__init__()
        self.local_file = local_file
        self.filepath = filepath
        self.progress_cond = progress_cond
        self.target = target
        self.local_path = local_path

    def run(self):
        result = os.popen('adb devices').read().strip('List of devices attached').strip('\n')
        if 'device' in result:
            try:
                while True:
                    if self.progress_cond == 0:
                        self.source_file_size = os.path.getsize(self.local_file)
                        target = self.local_file.split('/')[-1]
                        order = 'adb shell ls -l ' + self.filepath + target
                        self.target_file_size = os.popen(order).read().split(' ')[4]
                        progress = int(self.target_file_size) / int(self.source_file_size) * 100
                        print(progress)
                        self.signal.emit(int(progress))
                    elif self.progress_cond == 1:
                        target_file = self.local_path + '/' + self.target
                        self.target_file_size = os.path.getsize(target_file)
                        order = 'adb shell ls -l ' + self.filepath + self.target
                        self.source_file_size = os.popen(order).read().split(' ')[4]
                        progress = int(self.target_file_size) / int(self.source_file_size) * 100
                        print(progress)
                        self.signal.emit(int(progress))
                    if str(self.target_file_size) == str(self.source_file_size):
                        self.signal.emit(int(101))
                        break
                    else:
                        pass
            except Exception as e:
                print(e)
        else:
            pass