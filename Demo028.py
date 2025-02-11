import sys
from PyQt6.QtWidgets import (QWidget, QHBoxLayout, QSlider, QLabel, QApplication)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap, QFont
import images


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        hbox = QHBoxLayout()

        slider = QSlider(Qt.Orientation.Horizontal, self)
        slider.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        slider.valueChanged[int].connect(self.change_value)

        self.label = QLabel(self)
        self.label.setPixmap(QPixmap(':icon/min.png'))
        self.label.setFixedSize(80, 80)

        self.percent = QLabel(self)
        self.percent.setText(f"{slider.value()}%")

        hbox.addWidget(slider)
        hbox.addWidget(self.percent)
        hbox.addWidget(self.label)
        self.setLayout(hbox)

        self.resize(600, 450)
        self.setWindowTitle('QSlider')
        self.setFont(QFont("LXGW WenKai Screen", 30))
        self.show()

    def change_value(self, value):
        self.percent.setText(f"{value}%")

        if value == 0:
            self.label.setPixmap(QPixmap(':icon/mute.png'))
        elif 0 < value <= 30:
            self.label.setPixmap(QPixmap(':icon/min.png'))
        elif 30 < value <= 80:
            self.label.setPixmap(QPixmap(':icon/med.png'))
        else:
            self.label.setPixmap(QPixmap(':icon/max.png'))

def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
