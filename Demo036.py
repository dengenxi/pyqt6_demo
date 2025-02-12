import sys
from PyQt6.QtCore import Qt, QMimeData
from PyQt6.QtWidgets import (QWidget, QPushButton, QApplication)
from PyQt6.QtGui import QDrag


class Button(QPushButton):
    def __init__(self, title, parent):
        super().__init__(title, parent)

    def mouseMoveEvent(self, event):
        if event.buttons() != Qt.MouseButton.RightButton:
            return

        mime_data = QMimeData()

        drag = QDrag(self)
        drag.setMimeData(mime_data)

        drag.setHotSpot(event.position().toPoint() - self.rect().topLeft())

        drop_action = drag.exec(Qt.DropAction.MoveAction)

    def mousePressEvent(self, event):
        super().mousePressEvent(event)

        if event.button() == Qt.MouseButton.LeftButton:
            print('press')


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setAcceptDrops(True)

        self.button = Button('按钮', self)
        self.button.move(100, 65)

        self.setWindowTitle('Click and move')
        self.resize(550, 450)

    def dragEnterEvent(self, event):
        event.accept()

    def dropEvent(self, event):
        position = event.position()
        self.button.move(position.toPoint())

        event.setDropAction(Qt.DropAction.MoveAction)
        event.accept()


def main():
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    app.exec()


if __name__ == '__main__':
    main()

