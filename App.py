import sys
from random import randint
from PyQt5.QtWidgets import QWidget, QApplication, QLabel
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QPainter, QBrush, QColor, QPolygon
from PyQt5 import uic


class Example(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('antiplagiat.ui', self)
        self.setMouseTracking(True)
        self.coords_ = []
        self.qp = QPainter()
        self.flag = False

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
        color = QColor.fromRgb(210, 210, 20)
        size = randint(5, 180)
        self.qp.setBrush(QBrush(color))
        self.qp.setBrush(10)
        x, y = self.coords_
        b = randint(50, 150)
        a = randint(50, 250)
        coords = QPolygon([QPoint(x, y + b), QPoint(x + a / 2, y - b), QPoint(x + a, y + b)])
        self.qp.setBrush(QBrush(color))
        self.qp.drawPolygon(coords)

    def mousePressEvent(self, event):
        self.coords_ = [event.x(), event.y()]
        self.drawf()

    def mouseMoveEvent(self, event):
        self.coords_ = [event.x(), event.y()]
