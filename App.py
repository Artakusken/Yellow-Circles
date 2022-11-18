import sys
from random import randint
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QPainter, QBrush, QColor, QPolygon
from UI import Ui_MainWindow


class App(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        # uic.loadUi('UI.ui', self)
        self.setupUi(self)
        self.setMouseTracking(True)
        self.coords_ = (250, 250)
        self.qp = QPainter()
        self.flag = False
        self.usefulButton.clicked.connect(self.drawf)

    def drawf(self):
        self.flag = True
        self.update()

    def paintEvent(self, event):
        if self.flag:
            self.qp = QPainter()
            self.qp.begin(self)
            self.draw()
            self.qp.end()

    def draw(self):
        color = QColor.fromRgb(randint(0, 255), randint(0, 255), randint(0, 255))
        size = randint(5, 180)
        self.qp.setBrush(QBrush(color))
        self.qp.drawEllipse(*self.coords_, size, size)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    k = App()
    k.show()
    sys.exit(app.exec())
