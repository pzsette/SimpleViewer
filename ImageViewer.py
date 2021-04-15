import PyQt5
from PyQt5 import QtGui
from mainwindow import Ui_MainWindow
from PyQt5.QtWidgets import QFileDialog, QMessageBox, QMainWindow


class ImageViewer (QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.left_rotate.clicked.connect(self.left_rotate_button_clicked)

    def left_rotate_button_clicked(self):
        print("Left rotation")