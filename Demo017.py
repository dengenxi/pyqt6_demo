import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (QWidget, QLCDNumber, QSlider, QVBoxLayout, QApplication)


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):

        lcd = QLCDNumber(self)
        sld = QSlider(Qt.Orientation.Horizontal, self)

        vbox = QVBoxLayout()
        vbox.addWidget(lcd)
        vbox.addWidget(sld)

        self.setLayout(vbox)
        sld.valueChanged.connect(lcd.display)

        self.setWindowTitle('信号和插槽')
        self.resize(600, 450)
        self.show()


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
