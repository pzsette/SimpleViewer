from PIL.ExifTags import GPSTAGS
from PyQt5.QtGui import QPixmap
from PIL import Image as PILImage
from PIL.ExifTags import TAGS
from utils import convert_to_degree


class Image:
    def __init__(self, path):
        self.__path = path
        self.__pixmap = QPixmap(self.__path)
        self.exif_data = {}
        self.geo_data = {}
        self.get_exif_data()

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
                    value = exif_code_data[code]
                    for t in value:
                        sub_decoded_data = GPSTAGS.get(t, t)
                        self.geo_data[sub_decoded_data] = value[t]
                    latitude = convert_to_degree(self.geo_data["GPSLatitude"])
                    longitude = convert_to_degree(self.geo_data["GPSLongitude"])
                    self.geo_data = {
                        "Latitude": latitude,
                        "Longitude": longitude
                    }
                else:
                    self.exif_data[key_value] = exif_code_data[code]


