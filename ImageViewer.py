from PyQt5 import QtGui, QtWidgets
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QTransform, QPalette
from PyQt5.QtWidgets import QFileDialog, QMainWindow
from mainwindow import Ui_MainWindow
from Image import Image
import webbrowser


class ImageViewer (QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.info_box_is_visible = False
        self.ui.geo_info.setEnabled(False)
        self.ui.info_box.setHeaderLabel("Exif data")
        self.image = None
        self.zoom_ratio = 1
        self.ui.info_box.setVisible(self.info_box_is_visible)
        self.ui.left_rotate.clicked.connect(self.left_rotate_button_clicked)
        self.ui.right_rotate.clicked.connect(self.right_rotate_button_clicked)
        self.ui.zoom_in.clicked.connect(self.zoom_in_button_clicked)
        self.ui.zoom_out.clicked.connect(self.zoom_out_button_clicked)
        self.ui.show_info.clicked.connect(self.show_info_box)
        self.ui.load_image.clicked.connect(self.open)
        self.ui.geo_info.clicked.connect(self.geo_info_button_clicked)
        self.ui.scrollArea.setBackgroundRole(QPalette.Dark)
        self.image_box = QtWidgets.QLabel()
        self.image_box.setStyleSheet('background-color: #202020')
        self.image_box.setAlignment(Qt.AlignCenter)
        self.ui.scrollArea.setWidget(self.image_box)
        self.ui.scrollArea.setVisible(True)

    def left_rotate_button_clicked(self):
        transform = QTransform().rotate(-90)
        self.image.set_pixmap(self.image.get_pixmap().transformed(transform, Qt.SmoothTransformation))
        self.update_view()

    def right_rotate_button_clicked(self):
        transform = QTransform().rotate(90)
        self.image.set_pixmap(self.image.get_pixmap().transformed(transform, Qt.SmoothTransformation))
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
        lat = self.image.geo_data["Latitude"]
        long = self.image.geo_data["Longitude"]
        webbrowser.open("https://www.google.com/maps/search/?api=1&query={},{}".format(lat, long))

    def show_info_box(self):
        self.info_box_is_visible = not self.info_box_is_visible
        self.ui.info_box.setVisible(self.info_box_is_visible)
        self.update_view()

    def resizeEvent(self, a0: QtGui.QResizeEvent):
        self.update_view()

    def update_view(self):
        if self.image is not None:
            size = QSize(self.ui.scrollArea.width()*self.zoom_ratio-3, self.ui.scrollArea.height()*self.zoom_ratio-3)
            self.image_box.setPixmap(self.image.get_pixmap().scaled(size, Qt.KeepAspectRatio, Qt.SmoothTransformation))

    def open(self):
        options = QFileDialog.Options()
        self.zoom_ratio = 1
        filename, _ = QFileDialog.getOpenFileName(self, 'QFileDialog.getOpenFileName()', '',
                                                  'Images (*.png *.jpeg *.jpg *.bmp *.gif)', options=options)
        if filename:
            self.image = Image(filename)
            width = min(self.image.get_pixmap().width(), 1600)
            height = min(self.image.get_pixmap().height(), 900)
            self.image_box.setPixmap(self.image.get_pixmap().scaled(QSize(width, height), Qt.KeepAspectRatio, Qt.SmoothTransformation))
            self.update_view()
        self.ui.info_box.clear()
        if self.image.geo_data:
            self.ui.geo_info.setEnabled(True)
        else:
            self.ui.geo_info.setEnabled(False)
        self.add_exif_data()

    def add_exif_data(self):
        if self.image.exif_data:
            for key in self.image.exif_data:
                exif_code_item = QtWidgets.QTreeWidgetItem()
                exif_code_item.setText(0, key)
                self.ui.info_box.addTopLevelItem(exif_code_item)
                exif_value_item = QtWidgets.QTreeWidgetItem()
                exif_value_item.setText(0, str(self.image.exif_data[key]))
                exif_code_item.addChild(exif_value_item)
        else:
            exif_error_item = QtWidgets.QTreeWidgetItem()
            exif_error_item.setText(0, "No exif data")
            self.ui.info_box.addTopLevelItem(exif_error_item)
