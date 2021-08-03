# -*- coding: utf-8 -*-
# 列出文件子进程
import os

from PyQt5.QtCore import QThread, pyqtSignal


class ListFileThread(QThread):
    signal = pyqtSignal(list)

    def __init__(self, filepath):
        super(ListFileThread, self).__init__()
        self.filepath = filepath

    def run(self):
        try:
            self.signal.emit(list(["clear"]))
            order = 'adb shell ls -F ' + "'" + self.filepath + "'"
            self.result = os.popen(order)
            self.result = self.result.buffer.read().decode(encoding='utf8').replace('\r\n', '\n').replace('@','/').rstrip('\n').split('\n')
            lists = []
            for x in self.result:
                if x.startswith('d '):
                    x = x.lstrip('d')  # 岚：用lstrip保证仅删除左侧的“d ”下同
                    x = x.lstrip(' ') + '/'  # 岚：逐个删除能避免误删字符串（如“data”变“ata”的问题）
                elif x.startswith('ld '):
                    x = x.lstrip('ld')  # 岚：某些目录前缀不是“d ”而是"ld "（虚拟路径？），如“/storage/emulated/” (不带0)
                    x = x.lstrip(' ') + '/'
                if x.startswith('- '):
                    x = x.lstrip('-')
                    x = x.lstrip(' ')
                else:
                    pass
                lists.append(x)
                for r in range(0, len(lists)):  # 岚：历遍所有条目，删除无权访问的条目，避免作为文件/文件夹显示
                    if "failed: Permission denied" in lists[r] or 'opendir failed, Permission denied' in lists[r]:
                        del lists[r]
                for r in range(0, len(lists)):
                    if 'l? ' in lists[r]:
                        del lists[r]
                self.result = lists
            self.signal.emit(list(lists))
        except Exception as e:
            self.signal.emit(list(["error"]))
            print(e)