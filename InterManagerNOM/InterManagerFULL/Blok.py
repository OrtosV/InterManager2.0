# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Blok.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3

class Ui_Blokn(object):

    def loadData(self):
        rowCount = self.tableWidget.rowCount()
        columnCount = self.tableWidget.columnCount()
        for row in range(rowCount):
            rowData = ''
            for column in range(columnCount):
                widgetItem = self.tableWidget.item(row, column)
                if(widgetItem and widgetItem.text):
                    rowData = rowData + ' - ' + widgetItem.text()
                else:
                    rowData = rowData + ' - ' + 'NULL'
            print(rowData + '\n')


    def setupUi(self, Blokn):
        Blokn.setObjectName("Blokn")
        Blokn.resize(521, 403)
        Blokn.setMinimumSize(QtCore.QSize(521, 403))
        Blokn.setMaximumSize(QtCore.QSize(521, 403))
        self.centralwidget = QtWidgets.QWidget(Blokn)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(0, 10, 341, 381))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(3)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(360, 350, 141, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(360, 90, 141, 41))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(360, 160, 141, 41))
        self.pushButton_4.setObjectName("pushButton_4")
        Blokn.setCentralWidget(self.centralwidget)

        self.retranslateUi(Blokn)
        self.pushButton.clicked.connect(Blokn.close)
        QtCore.QMetaObject.connectSlotsByName(Blokn)

    def retranslateUi(self, Blokn):
        _translate = QtCore.QCoreApplication.translate
        Blokn.setWindowTitle(_translate("Blokn", "Блокнот"))
        self.pushButton.setText(_translate("Blokn", "Закрыть блокнот"))
        self.pushButton_3.setText(_translate("Blokn", "Добавить строку"))
        self.pushButton_4.setText(_translate("Blokn", "Удалить строку"))
