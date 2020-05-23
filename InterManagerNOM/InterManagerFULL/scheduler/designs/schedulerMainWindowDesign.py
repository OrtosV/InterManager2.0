# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Documents\schedulerMainWindowDesign.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1080, 731)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.canvasGraphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.canvasGraphicsView.setResizeAnchor(QtWidgets.QGraphicsView.NoAnchor)
        self.canvasGraphicsView.setObjectName("canvasGraphicsView")
        self.verticalLayout.addWidget(self.canvasGraphicsView)
        self.newElementBtn = QtWidgets.QPushButton(self.centralwidget)
        self.newElementBtn.setObjectName("newElementBtn")
        self.verticalLayout.addWidget(self.newElementBtn)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Планировщик"))
        self.newElementBtn.setText(_translate("MainWindow", "Добавить новый элемент..."))
