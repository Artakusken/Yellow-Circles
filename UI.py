# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.uselessButton = QtWidgets.QPushButton(self.centralwidget)
        self.uselessButton.setGeometry(QtCore.QRect(10, 20, 131, 23))
        self.uselessButton.setObjectName("uselessButton")
        self.usefulButton = QtWidgets.QPushButton(self.centralwidget)
        self.usefulButton.setGeometry(QtCore.QRect(190, 20, 261, 111))
        self.usefulButton.setObjectName("usefulButton")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.uselessButton.setText(_translate("MainWindow", "Бесмысленная кнопка"))
        self.usefulButton.setText(_translate("MainWindow", "Смысленная кнопка"))