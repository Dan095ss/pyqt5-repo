from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import *
from PyQt5 import uic
import random


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.setWindowTitle('Draw circles')

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(QPen(Qt.black, 5, Qt.SolidLine))

        for i in range(3):
            painter.setBrush(QBrush(Qt.red, Qt.SolidPattern))
            # painter.setBrush(QBrush(Qt.green, Qt.DiagCrossPattern))

            painter.drawEllipse(random.randint(0, 100), random.randint(0, 100),
                                random.randint(0, 400), random.randint(0, 200))


if __name__ == '__main__':
    app = QApplication([])
    mn = MainWindow()
    mn.show
    app.exec_()

