import PyQt5
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QImage, QPixmap, QPalette

from mainwindow import Ui_MainWindow
from PyQt5.QtWidgets import QFileDialog, QMessageBox, QMainWindow, QLabel, QSizePolicy, QScrollArea, QAction


class ImageViewer (QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.left_rotate.clicked.connect(self.left_rotate_button_clicked)
        self.ui.load_image.clicked.connect(self.open)
        self.ui.image_box.setStyleSheet('background-color: cyan')

        #self.ui.splitter.setStretchFactor(0, 0)
        #self.ui.splitter.setStretchFactor(0, 1)

    def left_rotate_button_clicked(self):
        print("Left rotation")


    def open(self):
        options = QFileDialog.Options()
        # fileName = QFileDialog.getOpenFileName(self, "Open File", QDir.currentPath())
        fileName, _ = QFileDialog.getOpenFileName(self, 'QFileDialog.getOpenFileName()', '',
                                                  'Images (*.png *.jpeg *.jpg *.bmp *.gif)', options=options)
        pixmap = QtGui.QPixmap(fileName)
        height_label = 100
        #self.ui.image_box.resize(self.ui.image_box.width(), self.ui.image_box.width())
        self.ui.image_box.setPixmap(pixmap.scaled(self.ui.image_box.size()))