from PyQt5 import QtWidgets
from PyQt5 import QtCore
from calc import Ui_Calccc
from MainBody import Ui_MainWindow
from Blok import Ui_Blokn
#from Plann import Ui_Plan
import sys



class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.bloknotWindow = None
        self.calcWindow = None
        #self.plannerWindow = None

        self.pushButton.clicked.connect(self.but_1)
        self.pushButton_3.clicked.connect(self.but_2)
        self.pushButton_2.clicked.connect(self.but_4)
        #self.pushButton_4.clicked.connect(self.but_3)


    def but_1(self):
        self.bloknotWindow = Bloknot()
        self.bloknotWindow.show()


    def but_2(self):
        self.calcWindow = Calculator()
        self.calcWindow.show()


    #def but_3(self):
        #self.plannerWindow = Planner()
        #self.plannerWindow.show()


    def but_4(self):
        self.close()
        self.bloknotWindow.close()
        self.calcWindow.close()
        #self.plannerWindow.close()



class Bloknot(QtWidgets.QMainWindow, Ui_Blokn):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(3)
        self.tableWidget.setHorizontalHeaderLabels(["Наименование", "Цена", "Доходы/расходы"])
        self.tableWidget.horizontalHeaderItem(0).setToolTip("Наименование вашей записи ")
        self.tableWidget.horizontalHeaderItem(1).setToolTip("Необходимые затраты / прибыль ")
        self.tableWidget.horizontalHeaderItem(2).setToolTip("Доходы/расходы ")

        self.tableWidget.horizontalHeaderItem(0).setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.horizontalHeaderItem(1).setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.horizontalHeaderItem(2).setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.resizeColumnsToContents()

        self.tableWidget.setItem(0, 0, QtWidgets.QTableWidgetItem("Стол"))
        self.tableWidget.setItem(0, 1, QtWidgets.QTableWidgetItem("5000"))
        self.tableWidget.setItem(0, 2, QtWidgets.QTableWidgetItem("Расход"))
        self.tableWidget.setItem(1, 0, QtWidgets.QTableWidgetItem("Стул"))
        self.tableWidget.setItem(1, 1, QtWidgets.QTableWidgetItem("3000"))
        self.tableWidget.setItem(1, 2, QtWidgets.QTableWidgetItem("Расход"))
        self.tableWidget.setItem(2, 0, QtWidgets.QTableWidgetItem("Зарплата"))
        self.tableWidget.setItem(2, 1, QtWidgets.QTableWidgetItem("40000"))
        self.tableWidget.setItem(2, 2, QtWidgets.QTableWidgetItem("Доход"))

        self.pushButton_3.clicked.connect(self.addRow)
        self.pushButton_4.clicked.connect(self.deleteRow)


    def addRow(self):
        numRows = self.tableWidget.rowCount()
        self.tableWidget.insertRow(numRows)


    def deleteRow(self):
        numRows = self.tableWidget.rowCount()
        self.tableWidget.removeRow(numRows - 1)



class Calculator(QtWidgets.QMainWindow, Ui_Calccc):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

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