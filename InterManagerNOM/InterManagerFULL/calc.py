# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Calcccc.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Calccc(object):
    def setupUi(self, Calccc):
        Calccc.setObjectName("Calccc")
        Calccc.resize(551, 318)
        Calccc.setMinimumSize(QtCore.QSize(551, 318))
        Calccc.setMaximumSize(QtCore.QSize(551, 318))
        self.centralwidget = QtWidgets.QWidget(Calccc)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(60, 200, 151, 51))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(30, 50, 201, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.Group = QtWidgets.QGroupBox(self.centralwidget)
        self.Group.setGeometry(QtCore.QRect(240, 20, 71, 161))
        self.Group.setAutoFillBackground(True)
        self.Group.setStyleSheet("gray")
        self.Group.setTitle("")
        self.Group.setObjectName("Group")
        self.radioButton = QtWidgets.QRadioButton(self.Group)
        self.radioButton.setGeometry(QtCore.QRect(20, 30, 121, 21))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.Group)
        self.radioButton_2.setGeometry(QtCore.QRect(20, 120, 99, 21))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(self.Group)
        self.radioButton_3.setGeometry(QtCore.QRect(20, 90, 99, 21))
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_4 = QtWidgets.QRadioButton(self.Group)
        self.radioButton_4.setGeometry(QtCore.QRect(20, 60, 99, 21))
        self.radioButton_4.setObjectName("radioButton_4")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(320, 50, 201, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(240, 210, 211, 31))
        self.lineEdit_3.setReadOnly(True)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(350, 270, 171, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        Calccc.setCentralWidget(self.centralwidget)

        self.retranslateUi(Calccc)
        self.pushButton_2.clicked.connect(Calccc.close)
        QtCore.QMetaObject.connectSlotsByName(Calccc)

    def retranslateUi(self, Calccc):
        _translate = QtCore.QCoreApplication.translate
        Calccc.setWindowTitle(_translate("Calccc", "Калькулятор"))
        self.pushButton.setText(_translate("Calccc", "Рассчитать"))
        self.radioButton.setText(_translate("Calccc", "+"))
        self.radioButton_2.setText(_translate("Calccc", "*"))
        self.radioButton_3.setText(_translate("Calccc", "/"))
        self.radioButton_4.setText(_translate("Calccc", "-"))
        self.pushButton_2.setText(_translate("Calccc", "Закрыть калькулятор"))
