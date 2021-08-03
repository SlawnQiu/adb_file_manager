# -*- coding: utf-8 -*-
# 进度条窗口类
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QCursor
from PyQt5.QtWidgets import QMainWindow

from Ui.ProgressWindow import Ui_ProgressWindow


class ProgressForm(QMainWindow, Ui_ProgressWindow):
    def __init__(self):
        super(ProgressForm, self).__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon('logo.ico'))
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.progressBar.setValue(0)

    def OPEN(self):
        self.show()

    def CLOSE(self):
        self.hide()

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