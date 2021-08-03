# -*- coding: utf-8 -*-
# 文件管理窗口类
import os
import time

from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSignal, QThread, Qt
from PyQt5.QtGui import QCursor, QIcon
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QFileDialog

from Form.ProcessForm import ProgressForm
from Form.RenameForm import RenameForm
from Methods.DownloadFileThread import DownloadFileThread
from Methods.GetFileInfoThread import GetFileInfoThread
from Methods.GetSpaceThread import GetSpaceThread
from Methods.ListFileThread import ListFileThread
from Methods.PasteThread import PasteThread
from Methods.ProgressThread import ProgressThread
from Methods.UploadThread import UploadThread
from Ui.FileManagerWindow import Ui_FileMangerWindow


# 文件管理窗口类
class FileManagerForm(QMainWindow, Ui_FileMangerWindow):
    def __init__(self):
        super(FileManagerForm, self).__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon('logo.ico'))
        self._translate = QtCore.QCoreApplication.translate
        self.renameForm = RenameForm()
        self.FileList.itemClicked.connect(self.setItem)
        self.FileList.doubleClicked.connect(self.cd)
        self.getSpaceThread = GetSpaceThread()  # 实例化线程对象
        self.getSpaceThread.signal.connect(self.getSpaceThreadBack)
        self.target = None
        self.local_path = None
        self.source_file = None
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.progressForm = ProgressForm()
        self.filepath = "/storage/emulated/0/"

    # 获取文件信息子线程信号槽
    def getFileInfoThreadBack(self, message):
        if message[0] == "noFile":
            '<html><head/><body><p align="center">' + self.target.rstrip('/') + '</p></body></html>'
            self.fileEditdate_data.setText(self._translate("FileMangerWindow", '无选中文件'))
            self.fileName_data.setText(self._translate("FileMangerWindow", '<html><head/><body><p align="center">无选中文件</p></body></html>'))
            self.fileSize_data.setText(self._translate("FileMangerWindow", '无选中文件'))
            self.fileType_data.setText(self._translate("FileMangerWindow", '无选中文件'))
        elif message[0] == "editDate":
            self.fileEditdate_data.setText(self._translate("FileMangerWindow", message[1]))
        elif message[0] == "fileName":
            self.fileName_data.setText(self._translate("FileMangerWindow", message[1]))
        elif message[0] == "fileSize":
            self.fileSize_data.setText(self._translate("FileMangerWindow", message[1]))
        elif message[0] == "setIcon":
            iconHtml = "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n" + \
                       "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n" + \
                       "p, li { white-space: pre-wrap; }\n" + \
                       "</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n" + \
                       "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/file_type/Resources/file_type/" + message[1] + ".svg\" /></p></body></html>"
            self.fileType_data.setText(self._translate("FileMangerWindow", message[2]))
            self.fileIcon.setHtml(self._translate("FileMangerWindow", iconHtml))

    # 获取设备空间信息子线程信号槽
    def getSpaceThreadBack(self, message):
        self.freeSpace_data.setText(self._translate("FileMangerWindow", message[0]))
        self.used_data.setText(self._translate("FileMangerWindow", message[1]))
        self.totalSpace_data.setText(self._translate("FileMangerWindow", message[2]))
        self.percent_data.setText(self._translate("FileMangerWindow", message[3]))

    # 获取设备内文件子线程信号槽
    def listFileThreadBack(self, message):
        if message[0] == "clear":
            self.target = None
            self.path_edit.setText(self.filepath)
            self.FileList.clear()
        elif message[0] == "error":
            self.FileList.addItem('获取设备文件时遇到错误，请重试！')
        else:
            if message == ['']:
                self.FileList.clear()
                self.FileList.addItem('..')
            else:
                self.FileList.addItem('..')
                self.FileList.addItems(message)
                print('set path: ', self.filepath)

    # 获取设备内文件函数
    def getFiles(self):
        self.list_file_thread = ListFileThread(self.filepath)  # 实例化线程对象
        self.list_file_thread.signal.connect(self.listFileThreadBack)
        self.list_file_thread.start()  # 启动线程

    # 设置文件列表Items函数
    def setItem(self):
        try:
            items = self.FileList.selectedItems()
            for item in items:
                self.target = item.text()
            self.getFileInfoThread = GetFileInfoThread(self.filepath, self.target)  # 实例化线程对象
            self.getFileInfoThread.signal.connect(self.getFileInfoThreadBack)
            self.getFileInfoThread.start()
        except Exception as e:
            print(e)
            self.fileType_data.setText(self._translate("FileMangerWindow", '获取失败'))

    # 进入目录函数
    def cd(self):
        result = os.popen('adb devices').read().strip('List of devices attached').strip('\n')
        if 'device' in result:
            items = self.FileList.selectedItems()
            for item in items:
                self.target = (item.text()).replace('\r', '')  # 岚：增加替换，避免TW系统中地址栏错误出现空格的问题
            if self.target == '..':
                try:
                    print('self.filepath', self.filepath)
                    self.filepath = self.filepath.replace('/', '  /')
                    self.filepath = self.filepath.replace('@', '  /').split('  ')
                    del (self.filepath[-2])
                    self.filepath = ''.join(self.filepath)
                    print('self.filepath', self.filepath)
                    if self.filepath == '':
                        self.filepath = '/'
                    self.getFiles()
                    self.fileIcon.setHtml(self._translate("FileMangerWindow",
                                                             "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                             "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                             "p, li { white-space: pre-wrap; }\n"
                                                             "</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                                             "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/file_type/Resources/file_type/folder.svg\" /></p></body></html>"))
                except Exception as e:
                    QMessageBox.warning(self, "错误", str(e))
            else:
                if '/' in self.target:
                    self.filepath = self.filepath + self.target
                    print('self.filepath ', self.filepath)
                    self.getFiles()
            if self.filepath == '/':
                QMessageBox.information(self, "警告","您正在进入的目录是 '/' 根目录，该目录下的文件您可能无权限进行正常操作。另外，您进入了本目录即视为您同意为因您对此目录下的文件(包括此目录下所有目录内的文件)修改、删除所造成的一切后果承担全部责任")
        else:
            QMessageBox.warning(self, "错误", "您尚未连接设备")

    # 删除文件函数
    def delFile(self):
        result = os.popen('adb devices').read().strip('List of devices attached').strip('\n')
        if 'device' in result:
            if self.target is None:
                QMessageBox.warning(self, "错误", "请先选择需要删除的文件", QMessageBox.Yes)
            else:
                if self.target == '..':
                    QMessageBox.warning(self, "错误", "禁止访问！", QMessageBox.Yes)
                else:
                    reply = QMessageBox.information(self, "确认？", "您确认要删除这个文件(夹)吗？", QMessageBox.Yes | QMessageBox.No,QMessageBox.Yes)
                    order = 'adb shell rm -rf ' + '"' + self.filepath + self.target + '"'
                    if reply == 16384:
                        os.popen(order)
                        time.sleep(0.1)
                        order = 'adb shell ls -F ' + '"' + self.filepath + '"'
                        result = os.popen(order)
                        result = result.buffer.read().decode(encoding='utf8').replace('\r\n', '\n').replace('@','/').rstrip(
                            '\n').split('\n')
                        if self.target in result:
                            self.getFiles()
                            self.getSpaceThread.start()  # 启动线程
                            QMessageBox.information(self, "错误", "删除失败", QMessageBox.Yes)

                        else:
                            self.getFiles()
                            self.getSpaceThread.start()  # 启动线程
                            QMessageBox.information(self, "消息", "删除完毕", QMessageBox.Yes)
        else:
            QMessageBox.warning(self, "错误", "您尚未连接设备")

    # 复制文件函数
    def copyFile(self):
        result = os.popen('adb devices').read().strip('List of devices attached').strip('\n')
        if 'device' in result:
            if self.target is None:
                QMessageBox.warning(self, "错误", "请先选择需要复制的文件", QMessageBox.Yes)
            else:
                if self.target == '..':
                    QMessageBox.warning(self, "错误", "禁止访问！", QMessageBox.Yes)
                else:
                    self.source_name = self.target
                    self.source_file = self.filepath + self.target
                    self.source_file = self.source_file.rstrip('/')
                    self.tip = 0
                    QMessageBox.information(self, "消息", "已将文件复制到剪切板！请到需要粘贴的地方点击粘贴来粘贴文件", QMessageBox.Yes)
        else:
            QMessageBox.warning(self, "错误", "您尚未连接设备")

    #粘贴文件函数
    def pasteFile(self):
        result = os.popen('adb devices').read().strip('List of devices attached').strip('\n')
        if 'device' in result:
            if self.source_file is None:
                QMessageBox.warning(self, "提示", "请先选择需要移动/复制的文件并点击复制/移动按钮", QMessageBox.Yes)
            else:
                self.getSpaceThread.start()  # 启动线程
                self.pasteThread = PasteThread(self.tip, self.source_file, self.filepath)  # 实例化线程对象
                self.pasteThread.signal.connect(self.pasteFileBack)
                self.pasteThread.start()  # 启动线程
        else:
            QMessageBox.warning(self, "错误", "您尚未连接设备")

    # 移动文件函数
    def moveFile(self):
        result = os.popen('adb devices').read().strip('List of devices attached').strip('\n')
        if 'device' in result:
            if self.target is None:
                QMessageBox.warning(self, "错误", "请先选择需要移动的文件", QMessageBox.Yes)
            else:
                if self.target == '..':
                    QMessageBox.warning(self, "错误", "禁止访问！", QMessageBox.Yes)
                else:
                    self.source_name = self.target
                    self.source_file = self.filepath + self.target
                    self.source_file = self.source_file.rstrip('/')
                    self.tip = 1
                    QMessageBox.information(self, "消息", "已将文件复制到剪切板！请到需要粘贴的地方点击粘贴来粘贴文件", QMessageBox.Yes)
        else:
            QMessageBox.warning(self, "错误", "您尚未连接设备")

    # 上传文件函数
    def uploadFile(self):
        result = os.popen('adb devices').read().strip('List of devices attached').strip('\n')
        if 'device' in result:
            self.local_file, type = QFileDialog.getOpenFileName(self, "选择需要上传的文件", "./", "所有文件 (*)")
            if self.local_file == '':
                pass
            else:
                self.uploadThread = UploadThread(self.filepath, self.local_file)  # 实例化线程对象
                self.uploadThread.signal.connect(self.uploadFileThreadBack)
                self.uploadThread.start()  # 启动线程
                self.progress_thread = ProgressThread(self.local_file, self.filepath, 0, self.target, self.local_path)  # 实例化线程对象
                self.progress_thread.signal.connect(self.getProgress)
                self.progress_thread.start()  # 启动线程
                self.progressForm.condition.setText(self._translate("ProgressWindow", "正在上传文件"))
                self.progressForm.OPEN()
        else:
            QMessageBox.warning(self, "错误", "您尚未连接设备")

    # 上传文件子线程信号槽
    def uploadFileThreadBack(self, result):
        print(result)
        if 'pushed' in result:
            self.progressForm.CLOSE()
            self.progressForm.progressBar.setValue(0)
            self.getSpaceThread.start()  # 启动线程
            self.getFiles()
            QMessageBox.information(self, "消息", "上传成功", QMessageBox.Yes)
        else:
            self.progressForm.CLOSE()
            msg = "上传失败！\n" + result
            QMessageBox.information(self, "消息", msg, QMessageBox.Yes)

    # 下载文件函数
    def downloadFile(self):
        result = os.popen('adb devices').read().strip('List of devices attached').strip('\n')
        if 'device' in result:
            if self.target is None:
                QMessageBox.warning(self, "错误", "请先选择需要下载的文件", QMessageBox.Yes)
            else:
                self.local_path = QFileDialog.getExistingDirectory(self, "请选择文件的保存位置", "./")
                if self.local_path == '':
                    pass
                else:
                    self.downloadFileThread = DownloadFileThread(self.filepath, self.target, self.local_path)  # 实例化线程对象
                    self.downloadFileThread.signal.connect(self.downloadFileThreadBack)
                    self.downloadFileThread.start()  # 启动线程
                    self.local_file = self.filepath + self.target
                    self.progress_thread = ProgressThread(self.local_file, self.filepath, 1, self.target, self.local_path)  # 实例化线程对象
                    self.progress_thread.signal.connect(self.getProgress)
                    self.progress_thread.start()  # 启动线程
                    self.progressForm.condition.setText(self._translate("ProgressWindow", "正在下载文件"))
                    self.progressForm.OPEN()
        else:
            QMessageBox.warning(self, "错误", "您尚未连接设备")

    # 下载文件子线程信号槽
    def downloadFileThreadBack(self, result):
        print(result)
        if 'pulled' in result:
            self.progressForm.CLOSE()
            self.progressForm.progressBar.setValue(0)
            self.getSpaceThread.start()  # 启动线程
            QMessageBox.information(self, "消息", "下载成功", QMessageBox.Yes)
        else:
            self.progressForm.CLOSE()
            msg = "下载失败！\n" + result
            QMessageBox.information(self, "消息", msg, QMessageBox.Yes)

    def goto(self):
        result = os.popen('adb devices').read().strip('List of devices attached').strip('\n')
        if 'device' in result:
            self.filepath = self.path_edit.text()
            if self.filepath.endswith('/'):
                pass
            else:
                self.filepath = self.filepath + '/'
            self.getSpaceThread.start()  # 启动线程
            self.getFiles()
        else:
            QMessageBox.warning(self, "错误", "您尚未连接设备")

    # 刷新页面函数
    def refresh(self):
        result = os.popen('adb devices').read().strip('List of devices attached').strip('\n')
        if 'device' in result:
            self.target = None
            self.fileSize_data.setText(self._translate("FileMangerWindow", '无选中文件'))
            self.fileType_data.setText(self._translate("FileMangerWindow", '无选中文件'))
            self.fileEditdate_data.setText(self._translate("FileMangerWindow", '无选中文件'))
            self.fileName_data.setText(self._translate("FileMangerWindow", '<html><head/><body><p align="center">无选中文件</p></body></html'))
            self.getFiles()
        else:
            QMessageBox.warning(self, "错误", "您尚未连接设备")

    # 回到主目录函数
    def goHomeDir(self):
        result = os.popen('adb devices').read().strip('List of devices attached').strip('\n')
        if 'device' in result:
            self.filepath = '/storage/emulated/0/'  # 岚：路径由“/sdcard/”改为“/storage/emulated/0/”以适配所有设备（部分不存在“/sdcard/”的会提示获取文件列表失败）
            self.getSpaceThread.start()  # 启动线程
            self.getFiles()
        else:
            QMessageBox.warning(self, "错误", "您尚未连接设备")

    # 重命名文件函数
    def renameFile(self):
        result = os.popen('adb devices').read().strip('List of devices attached').strip('\n')
        if 'device' in result:
            if self.target == '..':
                QMessageBox.warning(self, "错误", "拒绝访问")
            else:
                self.renameForm.name_edit.setText(self.target.replace('/', ''))
                self.renameForm.show()
        else:
            QMessageBox.warning(self, "错误", "您尚未连接设备")

    # 重命名文件执行函数
    def renameFileDo(self):
        self.renameForm.hide()
        new_name = self.renameForm.name_edit.text()
        order = 'adb shell ls -F ' + '"' + self.filepath + '"'
        result = os.popen(order)
        result = result.buffer.read().decode(encoding='utf8').replace('\r\n', '\n').replace('@', '/').rstrip(
            '\n').split('\n')
        if new_name + "/" in result:
            QMessageBox.warning(self, "错误", "在当前目录中已有该文件名的文件夹存在")
        elif new_name in result:
            QMessageBox.warning(self, "错误", "在当前目录中已有该文件名的文件存在")
        else:
            if '' == new_name:
                QMessageBox.warning(self, "错误", "请输入新文件名")
                pass
            if ' ' in new_name:
                QMessageBox.warning(self, "错误", "请不要再文件名中加入空格")
                pass
            if '/' in new_name:
                QMessageBox.warning(self, "错误", "请不要再文件名中加入'/'")
                pass
            if ':' in new_name:
                QMessageBox.warning(self, "错误", "请不要再文件名中加入':'")
                pass
            if '@' in new_name:
                QMessageBox.warning(self, "错误", "请不要再文件名中加入'@'")
                pass
            if '*' in new_name:
                QMessageBox.warning(self, "错误", "请不要再文件名中加入'*'")
                pass
            else:
                order = 'adb shell mv ' + '"' + self.filepath + self.target + '"' + ' ' + '"' + self.filepath + new_name + '"'
                os.popen(order)
                time.sleep(0.1)
                order = 'adb shell ls -F ' + '"' + self.filepath + '"'
                result = os.popen(order)
                result = result.buffer.read().decode(encoding='utf8').replace('\r\n', '\n').replace('@', '/').rstrip(
                    '\n').split('\n')
                if new_name in result:
                    self.getFiles()
                    QMessageBox.information(self, "消息", "重命名成功", QMessageBox.Yes)
                elif new_name + '/' in result:
                    self.getFiles()
                    QMessageBox.information(self, "消息", "重命名成功", QMessageBox.Yes)
                else:
                    self.getFiles()
                    QMessageBox.warning(self, "消息", "重命名失败", QMessageBox.Yes)

    # 粘贴文件子线程信号槽
    def pasteFileBack(self, done):
        order = 'adb shell ls -F ' + '"' + self.filepath + '"'
        result = os.popen(order)
        result = result.buffer.read().decode(encoding='utf8').replace('\r\n', '\n').replace('@', '/').rstrip('\n').split('\n')
        if self.source_name in result:
            if self.tip == 1:
                self.getFiles()
                QMessageBox.information(self, "消息", "移动成功", QMessageBox.Yes)
            elif self.tip == 0:
                self.getFiles()
                QMessageBox.information(self, "消息", "复制成功", QMessageBox.Yes)
        else:
            if self.tip == 1:
                self.getFiles()
                QMessageBox.warning(self, "消息", "移动失败", QMessageBox.Yes)
            elif self.tip == 0:
                self.getFiles()
                QMessageBox.warning(self, "消息", "复制失败", QMessageBox.Yes)

    # 获取进度子线程信号槽
    def getProgress(self, progress):
        progress = int(progress)
        if progress == 101:
            self.progressForm.CLOSE()
            self.progressForm.progressBar.setValue(0)
        else:
            # 进度条设定值
            self.progressForm.progressBar.setValue(progress)

    # 重写窗口移动事件
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.m_flag = True
            self.m_Position = event.globalPos() - self.pos()  # 获取鼠标相对窗口的位置
            event.accept()

    def mouseMoveEvent(self, QMouseEvent):
        try:
            if Qt.LeftButton and self.m_flag:
                self.move(QMouseEvent.globalPos() - self.m_Position)  # 更改窗口位置
                QMouseEvent.accept()
        except Exception as e:
            print(e)

    def mouseReleaseEvent(self, QMouseEvent):
        self.m_flag = False
        self.setCursor(QCursor(Qt.ArrowCursor))


