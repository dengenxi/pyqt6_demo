import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QFrame, QApplication)
from PyQt6.QtGui import QColor


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        hbox1 = QHBoxLayout()
        vbox = QVBoxLayout()

        self.color = QColor(0, 0, 0)

        red_button = QPushButton('Red', self)
        red_button.setCheckable(True)
        red_button.clicked[bool].connect(self.set_color)

        green_button = QPushButton('Green', self)
        green_button.setCheckable(True)
        green_button.clicked[bool].connect(self.set_color)

        blue_button = QPushButton('Blue', self)
        blue_button.setCheckable(True)
        blue_button.clicked[bool].connect(self.set_color)

        hbox1.addWidget(red_button)
        hbox1.addWidget(green_button)
        hbox1.addWidget(blue_button)
        hbox1.setAlignment(Qt.AlignmentFlag.AlignJustify)

        self.square = QFrame(self)
        self.square.setGeometry(200, 10, 200, 200)
        self.square.setStyleSheet("QWidget { background-color: %s }" % self.color.name())

        vbox.addWidget(self.square)
        vbox.addLayout(hbox1)
        self.setLayout(vbox)

        self.resize(600, 450)
        self.setWindowTitle('切换按钮')
        self.show()

    def set_color(self, pressed):
        source = self.sender()

        if pressed:
            val = 255
        else:
            val = 0

        if source.text() == 'Red':
            self.color.setRed(val)
        elif source.text() == 'Green':
            self.color.setGreen(val)
        else:
            self.color.setBlue(val)

        self.square.setStyleSheet("QFrame { background-color: %s }" % self.color.name())


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
