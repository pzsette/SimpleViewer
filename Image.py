from PIL.ExifTags import GPSTAGS
from PyQt5.QtGui import QPixmap
from PyQt5 import QtWidgets
from PIL import Image as PILImage

class Image:
    def __init__(self, path):
        self.__path = path
        self.__pixmap = QPixmap(self.__path)
        self.extract_exif_details(path)
        self.exif_data = None
        self.geo_data = None
        self.extract_exif_details(self.__path)

    def set_pixmap(self, pixmap):
        self.__pixmap = pixmap

    def get_pixmap(self):
        return self.__pixmap

    def get_exif_data(self):
        self.exif_data = PILImage.open(self.__path)._getexif()
        if self.exif_data is not None:
            geo_data = GPSTAGS.get(key, key)
            latitude = self.convert_to_degree(exif_data[exif_code][2])
            longitude = self.convert_to_degree(exif_data[exif_code][4])
            self.geo_data = {
                "Latitude": latitude,
                "Longitude": longitude
            }
            print("Latitude: {}, Longitude: {}".format(latitude, longitude))

#https://www.google.com/maps/search/?api=1&query=47.5951518,-122.3316393

