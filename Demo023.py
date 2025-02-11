import sys
from PyQt6.QtWidgets import (QWidget, QPushButton, QFrame, QColorDialog, QApplication)
from PyQt6.QtGui import QColor


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        col = QColor(0, 0, 0)

        self.btn = QPushButton('选择颜色', self)
        self.move(20, 20)

        self.btn.clicked.connect(self.show_dialog)

        self.frm = QFrame(self)
        self.frm.setStyleSheet("QWidget { background-color: %s }" % col.name())
        self.frm.setGeometry(130, 22, 200, 200)

        self.setWindowTitle('QColorDialog')
        self.resize(600, 450)
        self.show()

    def show_dialog(self):
        col = QColorDialog().getColor()

        if col.isValid():
            self.frm.setStyleSheet("QWidget { background-color: %s }" % col.name())


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
