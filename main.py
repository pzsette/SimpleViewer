import sys
from ImageViewer import ImageViewer
from PyQt5.QtWidgets import QMainWindow, QApplication


if __name__ == '__main__':
    print("Avviata")
    app = QApplication(sys.argv)
    window = ImageViewer()
    window.show()
    sys.exit(app.exec())
