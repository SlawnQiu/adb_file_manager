# -*- coding: utf-8 -*-
# 获取设备存储空间信息子进程
import os

from PyQt5.QtCore import QThread, pyqtSignal


class GetSpaceThread(QThread):
    signal = pyqtSignal(list)  # 自定义信号对象。参数str就代表这个信号可以传一个字符串

    def __init__(self):
        super(GetSpaceThread, self).__init__()

    def run(self):
        result = os.popen('adb devices').read().strip('List of devices attached').strip('\n')
        if 'device' in result:
            try:
                storageinfo = os.popen('adb shell df -h').read()  # 岚：TW带“-h”参数会报错，此处用于判断是否为TW系统
                if 'No such file or directory' in storageinfo:
                    storageinfo = os.popen('adb shell df').read().split('\n')[-3].split(' ')
                    storageinfo = [i for i in storageinfo if i != '']

                    # 岚：TW系统输出信息不显示百分比，故需计算；获取的容量单位不为字节，故需要换算

                    if list(storageinfo[1])[-1] == 'G':
                        total_ = float(storageinfo[1].replace('G', ''))
                        total_ = total_ * float(1024)
                    elif list(storageinfo[1])[-1] == 'M':
                        total_ = float(storageinfo[1].replace('M', ''))
                    elif list(storageinfo[1])[-1] == 'K':
                        total_ = float(storageinfo[1].replace('K', ''))
                        total_ = total_ / float(1024)
                    else:
                        total_ = float(storageinfo[1].replace('B', ''))
                        total_ = (total_ / float(1024)) / float(1024)

                    if list(storageinfo[2])[-1] == 'G':
                        used_ = float(storageinfo[2].replace('G', ''))
                        used_ = used_ * float(1024)
                    elif list(storageinfo[2])[-1] == 'M':
                        used_ = float(storageinfo[2].replace('M', ''))
                    elif list(storageinfo[2])[-1] == 'K':
                        used_ = float(storageinfo[2].replace('K', ''))
                        used_ = used_ / float(1024)
                    else:
                        used_ = float(storageinfo[2].replace('B', ''))
                        used_ = (used_ / float(1024)) / float(1024)

                    total = storageinfo[1]  # 岚：直接显示最优单位
                    used = storageinfo[2]
                    free = storageinfo[3]
                    percent = str(int((used_ / total_) * 100)) + '%'  # 岚：百分比计算

                    print('total: ', total)
                    print('used: ', used)
                    print('free: ', free)
                    print('percent: ', percent)
                    filem_free = '<html><head/><body><p align="center">' + free + '</p></body></html>'
                    filem_used = '<html><head/><body><p align="center">' + used + '</p></body></html>'
                    filem_total = '<html><head/><body><p align="center">' + total + '</p></body></html>'
                    filem_percent = '<html><head/><body><p align="center">' + percent + '</p></body></html>'
                    message = [filem_free, filem_used, filem_total, filem_percent]
                    self.signal.emit(list(message))

                else:
                    result = os.popen('adb shell df -H').read().split('\n')
                    data = result[-2].split(' ')
                    data = [i for i in data if i != '']
                    total = data[1]  # 岚：修改为直接显示最优单位
                    used = data[2]
                    free = data[3]
                    percent = data[4]
                    print('total: ', total)
                    print('used: ', used)
                    print('free: ', free)
                    print('percent: ', percent)
                    filem_free = '<html><head/><body><p align="center">' + free + '</p></body></html>'
                    filem_used = '<html><head/><body><p align="center">' + used + '</p></body></html>'
                    filem_total = '<html><head/><body><p align="center">' + total + '</p></body></html>'
                    filem_percent = '<html><head/><body><p align="center">' + percent + '</p></body></html>'
                    message = [filem_free, filem_used, filem_total, filem_percent]
                    self.signal.emit(list(message))
            except Exception as e:
                print(e)
                filem_free = '<html><head/><body><p align="center">错误</p></body></html>'
                filem_used = '<html><head/><body><p align="center">错误</p></body></html>'
                filem_total = '<html><head/><body><p align="center">错误</p></body></html>'
                filem_percent = '<html><head/><body><p align="center">错误</p></body></html>'
                message = [filem_free, filem_used, filem_total, filem_percent]
                self.signal.emit(list(message))
        else:
            filem_free = '<html><head/><body><p align="center">无设备</p></body></html>'
            filem_used = '<html><head/><body><p align="center">无设备</p></body></html>'
            filem_total = '<html><head/><body><p align="center">无设备</p></body></html>'
            filem_percent = '<html><head/><body><p align="center">无设备</p></body></html>'
            message = [filem_free, filem_used, filem_total, filem_percent]
            self.signal.emit(list(message))
