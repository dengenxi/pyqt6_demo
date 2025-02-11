import sys
from PyQt6.QtCore import pyqtSignal, QObject, Qt
from PyQt6.QtWidgets import (QMainWindow, QApplication)


class Community(QObject):
    closeApp = pyqtSignal()


class Example(QMainWindow):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.c = Community()
        self.c.closeApp.connect(self.close)

        self.resize(600, 450)
        self.setWindowTitle('触发信号')
        self.show()

    def mousePressEvent(self, event):
        self.c.closeApp.emit()


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
