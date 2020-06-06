from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.Qt import Qt

from scheduler.designs import schedulerMainWindowDesign, newRoomDialogDesign


class SchedulerUI(QtWidgets.QMainWindow, schedulerMainWindowDesign.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.scene = QtWidgets.QGraphicsScene()
        self.canvasGraphicsView.setScene(self.scene)
        self.scale = 1

        self.room_width = 0
        self.room_height = 0
        self.new_room_dialog()
        self.scene.setSceneRect(0, 0, self.room_width, self.room_height)
        self.draw_grid()

        self.newElementBtn.clicked.connect(self.new_element)
        self.colorPickingBtn.clicked.connect(self.pick_color)
        self.acceptBtn.clicked.connect(self.apply_changes)
        self.deleteBtn.clicked.connect(self.delete_selected_element)
        self.copyBtn.clicked.connect(self.copy_selected)
        self.exitBtn.clicked.connect(self.exit)

        self.default_pen = QtGui.QPen(Qt.black, 1)
        self.selected_pen = QtGui.QPen(Qt.black, 3)

        self.selected_item = None
        self.colorView.setScene(QtWidgets.QGraphicsScene())

    def draw_grid(self):
        pen = QtGui.QPen(QtGui.QColor(170, 180, 255), 1, Qt.SolidLine)

        for x in range(self.room_width//10+1):
            xc = x * 10
            self.scene.addLine(xc, 0, xc, self.room_height, pen)
        for y in range(self.room_height//10+1):
            yc = y * 10
            self.scene.addLine(0, yc, self.room_width, yc, pen)

    def new_room_dialog(self):
        dialog_window = NewRoomDialog(self)
        dialog_window.show()
        dialog_window.exec()

    def new_element(self):
        x = 0
        y = 0
        width = 100
        height = 100
        color = Qt.gray
        name = 'Новый элемент'
        el = self.create_element(x, y, width, height, color, name)
        self.select_item(el)

    def create_element(self, x, y, width, height, color, name):
        el = Element(x, y, width, height, color, self.default_pen, name, self)
        self.scene.addItem(el)
        return el

    def create_room(self, width, height):
        self.room_width = width
        self.room_height = height
        pen = QtGui.QPen(Qt.black, 3, Qt.DashLine)
        el = self.scene.addRect(0, 0, width, height, pen, QtGui.QBrush(Qt.NoBrush))
        el.setZValue(10)

    def change_scale(self, scale):
        self.canvasGraphicsView.scale(scale, scale)

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Equal:
            self.change_scale(1.10)
        elif e.key() == Qt.Key_Minus:
            self.change_scale(0.90)

    def select_item(self, item):
        if self.selected_item:
            self.selected_item.setPen(self.default_pen)
        if item:
            item.setPen(self.selected_pen)

            self.widget.setEnabled(True)
            self.nameLineEdit.setText(item.name)
            self.widthSpinBox.setValue(item.rect().width())
            self.heightSpinBox.setValue(item.rect().height())
            self.colorView.setBackgroundBrush(item.brush())

            self.xSpinBox.setValue(item.x())
            self.xSpinBox.setMaximum(self.room_width - item.rect().width())
            self.ySpinBox.setValue(item.y())
            self.ySpinBox.setMaximum(self.room_height - item.rect().height())

            self.itemSelectingLabel.setEnabled(False)

            self.selected_item = item
        else:
            self.widget.setEnabled(False)
            self.nameLineEdit.setText('')
            self.widthSpinBox.setValue(100)
            self.heightSpinBox.setValue(100)
            self.colorView.setBackgroundBrush(Qt.white)
            self.xSpinBox.setValue(0)
            self.ySpinBox.setValue(0)

            self.itemSelectingLabel.setEnabled(True)

            self.selected_item = None

    def pick_color(self):
        color = QtWidgets.QColorDialog.getColor()
        self.colorView.setBackgroundBrush(color)

    def apply_changes(self):
        x = self.xSpinBox.value()
        y = self.ySpinBox.value()
        width = self.widthSpinBox.value()
        height = self.heightSpinBox.value()
        color = self.colorView.backgroundBrush()
        name = self.nameLineEdit.text()

        el = self.create_element(x, y, width, height, color, name)
        self.delete_selected_element()
        self.select_item(el)

    def delete_selected_element(self):
        self.scene.removeItem(self.selected_item.text)
        self.scene.removeItem(self.selected_item)
        self.select_item(None)

    def copy_selected(self):
        width = self.selected_item.rect().width()
        height = self.selected_item.rect().height()
        color = self.selected_item.brush()
        name = self.selected_item.name

        el = self.create_element(0, 0, width, height, color, name)
        self.select_item(el)

    def mouseDoubleClickEvent(self, e):
        self.select_item(None)

    def exit(self):
        self.close()


class Element(QtWidgets.QGraphicsRectItem):
    def __init__(self, x, y, width, height, color, pen, name, main_window):
        super().__init__(0, 0, width, height)
        self.setPos(x, y)
        self.setBrush(color)
        self.setPen(pen)
        self.main_window = main_window
        self.name = name

        self.text = QtWidgets.QGraphicsSimpleTextItem(name)
        font = QtGui.QFont('Arial', 10)
        self.text.setFont(font)
        if self.text.boundingRect().width() <= self.rect().width():
            main_window.scene.addItem(self.text)
            self.text.setParentItem(self)
            self.text.setPos(self.x() / 1000 + self.rect().width() / 2 - self.text.boundingRect().width() / 2,
                             self.y() / 1000 + self.rect().height() / 2 - 10)
            if QtGui.QColor(color).value() > 150:
                self.text.setBrush(Qt.black)
            else:
                self.text.setBrush(Qt.white)

    def mouseDoubleClickEvent(self, e):
        self.main_window.select_item(self)

    def mousePressEvent(self, event):
        pass

    def mouseMoveEvent(self, event):
        orig_cursor_position = event.lastScenePos()
        updated_cursor_position = event.scenePos()

        orig_position = self.scenePos()

        updated_cursor_x = updated_cursor_position.x() - orig_cursor_position.x() + orig_position.x()
        updated_cursor_y = updated_cursor_position.y() - orig_cursor_position.y() + orig_position.y()
        if 0 <= updated_cursor_x <= self.main_window.room_width - self.rect().width() \
                and 0 <= updated_cursor_y <= self.main_window.room_height - self.rect().height():
            self.setPos(QtCore.QPointF(updated_cursor_x, updated_cursor_y))

        if self.main_window.selected_item == self:
            self.main_window.xSpinBox.setValue(self.x())
            self.main_window.ySpinBox.setValue(self.y())

    def mouseReleaseEvent(self, event):
        x = self.x()
        y = self.y()
        x = round_to_tens(x)
        y = round_to_tens(y)

        self.setPos(x, y)
        if self.main_window.selected_item == self:
            self.main_window.xSpinBox.setValue(self.x())
            self.main_window.ySpinBox.setValue(self.y())


class NewRoomDialog(QtWidgets.QDialog, newRoomDialogDesign.Ui_newRoomDialog):
    def __init__(self, main_window):
        QtWidgets.QDialog.__init__(self)
        self.setupUi(self)
        self.main_window = main_window

        self.acceptBtn.clicked.connect(self.accept_data)

    def accept_data(self):
        width = self.widthSpinBox.value()
        height = self.heightSpinBox.value()
        width = round_to_tens(width)
        height = round_to_tens(height)
        self.main_window.create_room(width, height)
        self.close()

def round_to_tens(n):
    if n % 10 >= 5:
        n = n // 10 * 10 + 10
    else:
        n = n // 10 * 10
    return n
