# -*- coding: utf-8 -*-
# 获取选择文件信息子进程
import os

from PyQt5.QtCore import QThread, pyqtSignal


class GetFileInfoThread(QThread):
    signal = pyqtSignal(list)  # 自定义信号对象。参数str就代表这个信号可以传一个字符串

    def __init__(self, filepath, target):
        super(GetFileInfoThread, self).__init__()
        self.filepath = filepath
        self.target = target

    def run(self):
        result = os.popen('adb devices').read().strip('List of devices attached').strip('\n')
        if 'device' in result:
            try:
                self.getFileEditDate()
                self.getFileName()
                self.getFileSize()
                self.setIcon()
            except Exception as e:
                print(e)

    # 获取文件修改日期
    def getFileEditDate(self):
        try:
            if self.target == '..':
                message = ["noFile"]
                self.signal.emit(list(message))
            else:
                order = 'adb shell stat ' + "'" + self.filepath + self.target + "'"
                result = os.popen(order)
                result = result.buffer.read().decode(encoding='utf8')

                if 'stat: not found' in result:  # 岚：TW系统不支持“adb shell stat”命令，增加判断，若不能获取则显示不支持
                    editDate = "系统不支持获取该值"
                else:
                    editDate = result.rstrip('\r\n').split('\r\n')[-1].split(' ')
                    del editDate[0]
                    editDate = ' '.join(editDate).split('.')
                    del editDate[-1]
                    editDate = ' '.join(editDate)
                message = ["editDate", editDate]
                self.signal.emit(list(message))
        except Exception as e:
            print(e)

    # 获取文件名
    def getFileName(self):
        try:
            if self.target == '..':
                message = ["noFile"]
                self.signal.emit(list(message))
            else:
                filename = '<html><head/><body><p align="center">' + self.target.rstrip('/') + '</p></body></html>'
                message = ["fileName", filename]
                self.signal.emit(list(message))
        except Exception as e:
            print(e)

    # 获取文件大小
    def getFileSize(self):
        try:
            if self.target == '..':
                message = ["noFile"]
                self.signal.emit(list(message))
            else:
                order = 'adb shell du -sh ' + "'" + self.filepath + self.target + "'"
                result = os.popen(order)
                result = result.buffer.read().decode(encoding='utf8')
                if 'Permission denied' in result:  # 岚：权限不足无法获取文件夹大小时显示（如/data/）
                    fileSize = '无足够权限查看该值'
                else:
                    try:  # 岚：AW中“Permission denied”错误不输出到result，此处为避免split失败
                        fileSize = result.split('\r\n')[
                            -2]  # 岚：避免出现目录中存在无读取权限的文件夹时导致显示错误（如TW中“/storage/emulated/”获取目录“0”信息时可能出现）
                        fileSize = fileSize.split('\t')[0]
                    except Exception as e:
                        print(e)
                        fileSize = '无足够权限查看该值'
                print('\n' + fileSize)
                message = ["fileSize", fileSize]
                self.signal.emit(list(message))
        except Exception as e:
            print(e)

    # 判断文件类型并设置图标
    def setIcon(self):
        try:
            if self.target.endswith('/'):
                message = ["setIcon", "folder", "文件夹"]
            elif self.target.endswith('.zip'):
                message = ["setIcon", "zip", "ZIP 压缩文件"]
            elif self.target.endswith('.rar'):
                message = ["setIcon", "rar", "RAR 压缩文件"]
            elif self.target.endswith('.7z'):
                message = ["setIcon", "7z", "7z 压缩文件"]
            elif self.target.endswith('.tar'):
                message = ["setIcon", "tar", "TAR 压缩文件"]
            elif self.target.endswith('.mp3'):
                message = ["setIcon", "mp3", "MP3 音频文件"]
            elif self.target.endswith('.wav'):
                message = ["setIcon", "wav", "WAV 音频文件"]
            elif self.target.endswith('.flac'):
                message = ["setIcon", "flac", "Flac 音频文件"]
            elif self.target.endswith('.mp4'):
                message = ["setIcon", "mp4", "MP4 视频文件"]
            elif self.target.endswith('.flv'):
                message = ["setIcon", "flv", "FLV 视频文件"]
            elif self.target.endswith('.3gp'):
                message = ["setIcon", "3gp", "3GP 视频文件"]
            elif self.target.endswith('.m4v'):
                message = ["setIcon", "m4v", "M4V 视频文件"]
            elif self.target.endswith('.avi'):
                message = ["setIcon", "avi", "AVI 视频文件"]
            elif self.target.endswith('.ppt'):
                message = ["setIcon", "ppt", "PPT 幻灯片"]
            elif self.target.endswith('.pptx'):
                message = ["setIcon", "ppt", "PPT 幻灯片"]
            elif self.target.endswith('.xlsx'):
                message = ["setIcon", "xls", "Excel 表格"]
            elif self.target.endswith('.xls'):
                message = ["setIcon", "xls", "Excel 表格"]
            elif self.target.endswith('.doc'):
                message = ["setIcon", "word", "Word 文档"]
            elif self.target.endswith('.docx'):
                message = ["setIcon", "word", "Word 文档"]
            elif self.target.endswith('.txt'):
                message = ["setIcon", "txt", "TXT 文本文件"]
            elif self.target.endswith('.png'):
                message = ["setIcon", "png", "PNG 图片文件"]
            elif self.target.endswith('.jpg'):
                message = ["setIcon", "jpg", "JPG 图片文件"]
            elif self.target.endswith('.jpeg'):
                message = ["setIcon", "jpeg", "JPEG 图片文件"]
            elif self.target.endswith('.pdf'):
                message = ["setIcon", "pdf", "PDF 文档"]
            elif self.target.endswith('.apk'):
                message = ["setIcon", "apk", "APK 安装包"]
            elif self.target == '..':
                message = ["setIcon", "folder", "无选中文件"]
            else:
                message = ["setIcon", "file", "文件"]
            self.signal.emit(list(message))
        except Exception as e:
            print(e)