import PyQt5
from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QImage, QPixmap, QPalette

from mainwindow import Ui_MainWindow
from PyQt5.QtWidgets import QFileDialog, QMessageBox, QMainWindow, QLabel, QSizePolicy, QScrollArea, QAction


class ImageViewer (QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.pixmap = None
        self.filename = None
        self.info_box_is_visible = False
        self.ui.info_box.setVisible(self.info_box_is_visible)
        self.ui.left_rotate.clicked.connect(self.left_rotate_button_clicked)
        self.ui.load_image.clicked.connect(self.open)
        self.ui.show_info.clicked.connect(self.show_info_box)
        self.ui.image_box.setStyleSheet('background-color: cyan')



    def left_rotate_button_clicked(self):
        print("Left rotation")

    def show_info_box(self):
        print("enable")
        self.info_box_is_visible = not self.info_box_is_visible
        self.ui.info_box.setVisible(self.info_box_is_visible)
        print(self.info_box_is_visible)

    def resizeEvent(self, a0: QtGui.QResizeEvent):
        self.update_view()

    def update_view(self):
        if self.pixmap is not None:
            self.pixmap = QPixmap(self.filename)
            width = max(500, self.ui.image_box.width())
            height = max(300, self.ui.image_box.height())
            self.ui.image_box.setPixmap(
                self.pixmap.scaled(QSize(width, height), Qt.KeepAspectRatio, Qt.SmoothTransformation))

    def open(self):
        options = QFileDialog.Options()
        # fileName = QFileDialog.getOpenFileName(self, "Open File", QDir.currentPath())
        self.filename, _ = QFileDialog.getOpenFileName(self, 'QFileDialog.getOpenFileName()', '',
                                                  'Images (*.png *.jpeg *.jpg *.bmp *.gif)', options=options)
        self.pixmap = QPixmap(self.filename)
        width = self.pixmap.width()
        height = self.pixmap.height()
        self.ui.image_box.setPixmap(
            self.pixmap.scaled(QSize(min(width, 1600), min(900, height)), Qt.KeepAspectRatio, Qt.SmoothTransformation))
        self.update_view()
