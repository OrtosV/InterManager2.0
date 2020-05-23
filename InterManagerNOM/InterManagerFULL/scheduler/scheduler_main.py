import sys
from PyQt5 import QtWidgets, QtGui
from PyQt5.Qt import Qt

from scheduler.designs import schedulerMainWindowDesign, newElementDialogDesign


class SchedulerUI(QtWidgets.QMainWindow, schedulerMainWindowDesign.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.scene = QtWidgets.QGraphicsScene()
        # self.scene.setSceneRect(0, 0, 100, 100)
        self.canvasGraphicsView.setScene(self.scene)
        self.scale = 1

        self.newElementBtn.clicked.connect(self.new_element_dialog)
        self.pen = QtGui.QPen(Qt.black)

    def new_element_dialog(self):
        dialog_window = NewElementDialog(self)
        dialog_window.show()
        dialog_window.exec()

    def create_element(self, width, height, color):
        el = self.scene.addRect(0, 0, width, height, self.pen, QtGui.QBrush(color))
        el.setFlag(QtWidgets.QGraphicsItem.ItemIsMovable)

    def change_scale(self, scale):
        self.canvasGraphicsView.scale(scale, scale)

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_9:
            self.change_scale(1.25)
            print(self.scale)
        elif e.key() == Qt.Key_8:
            self.change_scale(0.75)
            print(self.scale)


class NewElementDialog(QtWidgets.QDialog, newElementDialogDesign.Ui_newElementDialog):
    def __init__(self, main_window):
        QtWidgets.QDialog.__init__(self)
        self.setupUi(self)
        self.main_window = main_window

        self.buttonBox.accepted.connect(self.accept_data)
        self.buttonBox.rejected.connect(self.reject_data)

        self.colorView.setScene(QtWidgets.QGraphicsScene())
        self.set_color(Qt.red)
        self.colorPickingBtn.clicked.connect(self.pick_color)

    def pick_color(self):
        self.set_color(QtWidgets.QColorDialog.getColor())

    def set_color(self, color):
        self.color = color
        brush = QtGui.QBrush(color)
        self.colorView.setBackgroundBrush(brush)

    def accept_data(self):
        width = self.widthSpinBox.value()
        height = self.heightSpinBox.value()
        self.main_window.create_element(width, height, self.color)
        self.close()

    def reject_data(self):
        self.close()
