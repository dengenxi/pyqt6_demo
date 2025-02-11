import sys
from PyQt6.QtWidgets import (QWidget, QLabel, QHBoxLayout, QApplication)
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt
import images


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        hbox = QHBoxLayout()
        pixmap = QPixmap(':icon/dragon.png')

        lbl = QLabel(self)
        lbl.setPixmap(pixmap)

        hbox.addWidget(lbl)
        hbox.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.setLayout(hbox)

        self.resize(300, 200)
        self.show()


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
