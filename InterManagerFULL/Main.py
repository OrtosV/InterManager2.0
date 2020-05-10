from PyQt5 import QtWidgets
from PyQt5 import QtCore

from calc import Ui_Calccc
from MainBody import Ui_MainWindow
from Blok import Ui_Blokn
#from Plann import Ui_Plan

import sys
import contextlib



class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.bloknotWindow = None
        self.calcWindow = None
        #self.plannerWindow = None

        self.BN = False
        self.CN = False
        #self.PN = False

        #Взаимодействие с кнопками Главного меню

        self.pushButton.clicked.connect(self.but_1)
        self.pushButton_3.clicked.connect(self.but_2)
        self.pushButton_2.clicked.connect(self.but_4)
        #self.pushButton_4.clicked.connect(self.but_3)


    def but_1(self):
        self.bloknotWindow = Bloknot()
        self.bloknotWindow.show()
        self.BN = True


    def but_2(self):
        self.calcWindow = Calculator()
        self.calcWindow.show()
        self.CN = True


    #def but_3(self):
        #self.plannerWindow = Planner()
        #self.plannerWindow.show()
        #self.PN = True


    def but_4(self):
        self.close()
        if self.BN == True:
            self.bloknotWindow.close()
        if self.CN == True:
            self.calcWindow.close()
        #if self.PN == True:
            #self.plannerWindow.close()



class Bloknot(QtWidgets.QMainWindow, Ui_Blokn):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        #Взаимодействие с кнопками Блокнота

        self.pushButton_3.clicked.connect(self.addRow)
        self.pushButton_4.clicked.connect(self.deleteRow)



#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#БАЗА ДАННЫХ

        self.read_settings()

    def closeEvent(self, event):
        self.write_settings()
        super().closeEvent(event)

    def read_settings(self):
        with settingsContext("data_T_W.ini") as m:
            for children in self.findChildren(QtWidgets.QWidget):
                if children.objectName():
                    m.read(children)

    def write_settings(self):
        with settingsContext("data_T_W.ini") as m:
            for children in self.findChildren(QtWidgets.QWidget):
                if children.objectName():
                    m.write(children)


#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!



    def addRow(self):
        numRows = self.tableWidget.rowCount()
        self.tableWidget.insertRow(numRows)


    def deleteRow(self):
        numRows = self.tableWidget.rowCount()
        self.tableWidget.removeRow(numRows - 1)





#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

class SettingsManager:
    def __init__(self, filename):
        self.m_settings = QtCore.QSettings(filename, QtCore.QSettings.IniFormat)

    @property
    def settings(self):
        return self.m_settings

    def read(self, widget):
        self.settings.beginGroup(widget.objectName())
        if isinstance(widget, QtWidgets.QAbstractItemView):
            selectionMode = self.settings.value(
                "selectionMode", type=QtWidgets.QAbstractItemView.SelectionMode
            )
            widget.setSelectionMode(selectionMode)

        if isinstance(widget, QtWidgets.QTableWidget):
            rowCount = self.settings.value("rowCount", type=int)
            columnCount = self.settings.value("columnCount", type=int)
            widget.setRowCount(rowCount)
            widget.setColumnCount(columnCount)
            items = self.settings.value("items")
            widget.setHorizontalHeaderLabels(["Наименование", "Цена", "Доходы/расходы"])
            widget.resizeColumnsToContents()
            if items is None:
                self.read_defaults(widget)
            else:

                stream = QtCore.QDataStream(items, QtCore.QIODevice.ReadOnly)
                while not stream.atEnd():
                    it = QtWidgets.QTableWidgetItem()
                    i = stream.readInt()
                    j = stream.readInt()
                    stream >> it
                    widget.setItem(i, j, it)
                selecteditems = self.settings.value("selecteditems")
                stream = QtCore.QDataStream(
                    selecteditems, QtCore.QIODevice.ReadOnly
                )
                while not stream.atEnd():
                    i = stream.readInt()
                    j = stream.readInt()
                    it = widget.item(i, j)
                    if it is not None:
                        it.setSelected(False)
        self.settings.endGroup()

    def write(self, widget):
        self.settings.beginGroup(widget.objectName())
        if isinstance(widget, QtWidgets.QAbstractItemView):
            self.settings.setValue("selectionMode", widget.selectionMode())

        if isinstance(widget, QtWidgets.QTableWidget):
            self.settings.setValue("rowCount", widget.rowCount())
            self.settings.setValue("columnCount", widget.columnCount())
            items = QtCore.QByteArray()
            stream = QtCore.QDataStream(items, QtCore.QIODevice.WriteOnly)
            for i in range(widget.rowCount()):
                for j in range(widget.columnCount()):
                    it = widget.item(i, j)
                    if it is not None:
                        stream.writeInt(i)
                        stream.writeInt(j)
                        stream << it
            self.settings.setValue("items", items)
            selecteditems = QtCore.QByteArray()
            stream = QtCore.QDataStream(
                selecteditems, QtCore.QIODevice.WriteOnly
            )
            for it in widget.selectedItems():
                #print(it.row(), it.column())
                stream.writeInt(it.row())
                stream.writeInt(it.column())
            self.settings.setValue("selecteditems", selecteditems)
        self.settings.endGroup()

    def release(self):
        self.m_settings.sync()

    def read_defaults(self, widget):
        if  widget.objectName() == "tableWidget":
            widget.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
            widget.setRowCount(3)
            widget.setColumnCount(3)
            widget.setItem(0, 0, QtWidgets.QTableWidgetItem("Стол"))
            widget.setItem(0, 1, QtWidgets.QTableWidgetItem("5000"))
            widget.setItem(0, 2, QtWidgets.QTableWidgetItem("Расход"))
            widget.setItem(1, 0, QtWidgets.QTableWidgetItem("Стул"))
            widget.setItem(1, 1, QtWidgets.QTableWidgetItem("3000"))
            widget.setItem(1, 2, QtWidgets.QTableWidgetItem("Расход"))
            widget.setItem(2, 0, QtWidgets.QTableWidgetItem("Зарплата"))
            widget.setItem(2, 1, QtWidgets.QTableWidgetItem("40000"))
            widget.setItem(2, 2, QtWidgets.QTableWidgetItem("Доход"))
            widget.setHorizontalHeaderLabels(["Наименование", "Цена", "Доходы/расходы"])
            widget.horizontalHeaderItem(0).setToolTip("Наименование вашей записи ")
            widget.horizontalHeaderItem(1).setToolTip("Необходимые затраты / прибыль ")
            widget.horizontalHeaderItem(2).setToolTip("Доходы/расходы ")

            widget.horizontalHeaderItem(0).setTextAlignment(QtCore.Qt.AlignCenter)
            widget.horizontalHeaderItem(1).setTextAlignment(QtCore.Qt.AlignCenter)
            widget.horizontalHeaderItem(2).setTextAlignment(QtCore.Qt.AlignCenter)
            widget.resizeColumnsToContents()


@contextlib.contextmanager
def settingsContext(filename):
    manager = SettingsManager(filename)
    try:
        yield manager
    finally:
        manager.release()

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


class Calculator(QtWidgets.QMainWindow, Ui_Calccc):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        #Взаимодействие с кнопкой в Калькуляторе

        self.pushButton.clicked.connect(self.answer)


    def answer(self):

        self.i = 2
        try:
            float(self.lineEdit.text())
            self.i = self.i + 1
        except ValueError:
            self.i = self.i - 1

        try:
            float(self.lineEdit_2.text())
            self.i = self.i + 1
        except ValueError:
            self.i = self.i - 1

        if self.i == 4:
            number1 = float(self.lineEdit.text())
            number2 = float(self.lineEdit_2.text())
            if self.radioButton.isChecked():
                sum = str(number1 + number2)
                self.lineEdit_3.setText(sum)
            if self.radioButton_4.isChecked():
                sum = str(number1 - number2)
                self.lineEdit_3.setText(sum)
            if self.radioButton_3.isChecked():
                sum = str(number1 / number2)
                self.lineEdit_3.setText(sum)
            if self.radioButton_2.isChecked():
                sum = str(number1 * number2)
                self.lineEdit_3.setText(sum)
        elif self.i < 4:
            self.lineEdit_3.setText("Вы должны ввести число!")



#class Planner(QtWidgets.QMainWindow, Ui_Plan):

    #def __init__(self):
        #super().__init__()
        #self.setupUi(self)



def main():
    app = QtWidgets.QApplication([])
    application = MainWindow()
    application.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()