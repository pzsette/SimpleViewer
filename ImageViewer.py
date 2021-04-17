import PyQt5
from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QPixmap, QTransform, QPalette
from PyQt5.QtWidgets import QFileDialog, QMessageBox, QMainWindow
from mainwindow import Ui_MainWindow


class ImageViewer (QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.pixmap = None
        self.filename = None
        self.info_box_is_visible = False
        self.zoom_ratio = 1
        self.ui.info_box.setVisible(self.info_box_is_visible)
        self.ui.left_rotate.clicked.connect(self.left_rotate_button_clicked)
        self.ui.right_rotate.clicked.connect(self.right_rotate_button_clicked)
        self.ui.zoom_in.clicked.connect(self.zoom_in_button_clicked)
        self.ui.zoom_out.clicked.connect(self.zoom_out_button_clicked)
        self.ui.show_info.clicked.connect(self.show_info_box)
        self.ui.load_image.clicked.connect(self.open)
        self.ui.scrollArea.setBackgroundRole(QPalette.Dark)
        self.image_box = QtWidgets.QLabel()
        self.image_box.setAlignment(Qt.AlignCenter)
        self.ui.scrollArea.setWidget(self.image_box)
        self.ui.scrollArea.setVisible(True)

        #self.ui.image_box.setStyleSheet('background-color: #202020')

    def left_rotate_button_clicked(self):
        transform = QTransform().rotate(-90)
        self.pixmap = self.pixmap.transformed(transform, Qt.SmoothTransformation)
        self.update_view()

    def right_rotate_button_clicked(self):
        transform = QTransform().rotate(90)
        self.pixmap = self.pixmap.transformed(transform, Qt.SmoothTransformation)
        self.update_view()

    def zoom_in_button_clicked(self):
        if self.zoom_ratio+0.5 <= 5:
            self.zoom_ratio += 0.5
            self.update_view()

    def zoom_out_button_clicked(self):
        if self.zoom_ratio-0.5 >= 1:
            self.zoom_ratio -= 0.5
            self.update_view()

    def geo_info_button_clicked(self):
        print("Geo info")

    def show_info_box(self):
        self.info_box_is_visible = not self.info_box_is_visible
        self.ui.info_box.setVisible(self.info_box_is_visible)
        self.update_view()

    def resizeEvent(self, a0: QtGui.QResizeEvent):
        self.update_view()

    def update_view(self):
        if self.pixmap is not None:
            size = QSize(self.ui.scrollArea.width()*self.zoom_ratio-3, self.ui.scrollArea.height()*self.zoom_ratio-3)
            self.image_box.setPixmap(
                self.pixmap.scaled(size, Qt.KeepAspectRatio, Qt.SmoothTransformation))

    def open(self):
        options = QFileDialog.Options()
        self.filename, _ = QFileDialog.getOpenFileName(self, 'QFileDialog.getOpenFileName()', '',
                                                  'Images (*.png *.jpeg *.jpg *.bmp *.gif)', options=options)
        self.pixmap = QPixmap(self.filename)
        width = self.pixmap.width()
        height = self.pixmap.height()
        self.image_box.setPixmap(
            self.pixmap.scaled(QSize(min(width, 1600), min(900, height)), Qt.KeepAspectRatio, Qt.SmoothTransformation))
        self.update_view()
