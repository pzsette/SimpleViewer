from PIL.ExifTags import GPSTAGS
from PyQt5.QtGui import QPixmap
from PyQt5 import QtWidgets
from PIL import Image as PILImage
from PIL.ExifTags import TAGS
from utils import convert_to_degree

class Image:
    def __init__(self, path):
        self.__path = path
        self.__pixmap = QPixmap(self.__path)
        self.exif_data = {}
        self.get_exif_data()
        self.geo_data = None

    def set_pixmap(self, pixmap):
        self.__pixmap = pixmap

    def get_pixmap(self):
        return self.__pixmap

    def get_exif_data(self):
        exif_code_data = PILImage.open(self.__path)._getexif()
        if exif_code_data is not None:
            for code in exif_code_data:
                key_value = TAGS[code]
                if key_value == "GPSInfo":
                    print(exif_code_data[code][2])
                    latitude = convert_to_degree(exif_code_data[code][2])
                    longitude = convert_to_degree(exif_code_data[code][4])
                    self.geo_data = {
                        "Latitude": latitude,
                        "Longitude": longitude
                    }
                    print("Latitude: {}, Longitude: {}".format(latitude, longitude))
                else:
                    self.exif_data[key_value] = exif_code_data[code]
#https://www.google.com/maps/search/?api=1&query=47.5951518,-122.3316393

