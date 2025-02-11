import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (QWidget, QLabel, QGridLayout, QApplication)
from PyQt6.QtGui import QFont


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):

        grid = QGridLayout()

        x = 0
        y = 0

        self.text = f'x: {x}, y: {y}'

        self.label = QLabel(self.text, self)

        grid.addWidget(self.label, 0, 0, Qt.AlignmentFlag.AlignTop)

        self.setMouseTracking(True)
        self.setLayout(grid)

        self.setWindowTitle('事件对象')
        self.resize(600, 450)
        self.setFont(QFont('LXGW WenKai Screen', 20))
        self.show()

    def mouseMoveEvent(self, event):
        x = int(event.position().x())
        y = int(event.position().y())

        text = f'x: {x}, y: {y}'
        self.label.setText(text)

def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
