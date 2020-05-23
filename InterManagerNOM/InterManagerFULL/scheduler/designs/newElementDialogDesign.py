# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Documents\newElementDialogDesign.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_newElementDialog(object):
    def setupUi(self, newElementDialog):
        newElementDialog.setObjectName("newElementDialog")
        newElementDialog.resize(206, 229)
        newElementDialog.setModal(False)
        self.verticalLayout = QtWidgets.QVBoxLayout(newElementDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.sizeGroupBox = QtWidgets.QGroupBox(newElementDialog)
        self.sizeGroupBox.setObjectName("sizeGroupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.sizeGroupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.widthSpinBox = QtWidgets.QSpinBox(self.sizeGroupBox)
        self.widthSpinBox.setMinimum(10)
        self.widthSpinBox.setMaximum(1000)
        self.widthSpinBox.setProperty("value", 100)
        self.widthSpinBox.setObjectName("widthSpinBox")
        self.gridLayout.addWidget(self.widthSpinBox, 1, 0, 1, 1)
        self.heightSpinBox = QtWidgets.QSpinBox(self.sizeGroupBox)
        self.heightSpinBox.setMinimum(10)
        self.heightSpinBox.setMaximum(1000)
        self.heightSpinBox.setProperty("value", 100)
        self.heightSpinBox.setObjectName("heightSpinBox")
        self.gridLayout.addWidget(self.heightSpinBox, 1, 1, 1, 1)
        self.widthLabel = QtWidgets.QLabel(self.sizeGroupBox)
        self.widthLabel.setObjectName("widthLabel")
        self.gridLayout.addWidget(self.widthLabel, 0, 0, 1, 1)
        self.heightLabel = QtWidgets.QLabel(self.sizeGroupBox)
        self.heightLabel.setObjectName("heightLabel")
        self.gridLayout.addWidget(self.heightLabel, 0, 1, 1, 1)
        self.verticalLayout.addWidget(self.sizeGroupBox)
        self.colorGroupBox = QtWidgets.QGroupBox(newElementDialog)
        self.colorGroupBox.setObjectName("colorGroupBox")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.colorGroupBox)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.colorPickingBtn = QtWidgets.QPushButton(self.colorGroupBox)
        self.colorPickingBtn.setObjectName("colorPickingBtn")
        self.horizontalLayout_2.addWidget(self.colorPickingBtn)
        self.colorView = QtWidgets.QGraphicsView(self.colorGroupBox)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        self.colorView.setBackgroundBrush(brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        self.colorView.setForegroundBrush(brush)
        self.colorView.setInteractive(True)
        self.colorView.setObjectName("colorView")
        self.horizontalLayout_2.addWidget(self.colorView)
        self.verticalLayout.addWidget(self.colorGroupBox)
        self.buttonBox = QtWidgets.QDialogButtonBox(newElementDialog)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(newElementDialog)
        QtCore.QMetaObject.connectSlotsByName(newElementDialog)

    def retranslateUi(self, newElementDialog):
        _translate = QtCore.QCoreApplication.translate
        newElementDialog.setWindowTitle(_translate("newElementDialog", "Создание элемента"))
        self.sizeGroupBox.setTitle(_translate("newElementDialog", "Размер"))
        self.widthLabel.setText(_translate("newElementDialog", "Ширина:"))
        self.heightLabel.setText(_translate("newElementDialog", "Высота:"))
        self.colorGroupBox.setTitle(_translate("newElementDialog", "Выбор цвета"))
        self.colorPickingBtn.setText(_translate("newElementDialog", "Выбрать цвет..."))
