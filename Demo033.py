import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (QWidget, QHBoxLayout, QLabel, QFrame, QSplitter, QApplication)
from PyQt6.QtGui import QFont


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        hbox = QHBoxLayout()


        top_left = QFrame(self)
        top_left.setFrameShape(QFrame.Shape.StyledPanel)
        top_left.setFixedHeight(200)

        label1 = QLabel('两', self)
        inner_box1 = QHBoxLayout()
        inner_box1.addWidget(label1)
        inner_box1.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        top_left.setLayout(inner_box1)
        top_left.setFont(QFont('LXGW WenKai Screen', 50))

        top_right = QFrame(self)
        top_right.setFrameShape(QFrame.Shape.StyledPanel)

        label2 = QLabel('仪', self)
        inner_box2 = QHBoxLayout()
        inner_box2.addWidget(label2)
        inner_box2.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        top_right.setLayout(inner_box2)
        top_right.setFont(QFont('LXGW WenKai Screen', 50))

        bottom = QFrame(self)
        bottom.setFrameShape(QFrame.Shape.StyledPanel)

        label3 = QLabel('太极')
        inner_box3 = QHBoxLayout()
        inner_box3.addWidget(label3)
        inner_box3.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        bottom.setLayout(inner_box3)
        bottom.setFont(QFont('LXGW WenKai Screen', 80))

        splitter1 = QSplitter(Qt.Orientation.Horizontal)
        splitter1.addWidget(top_left)
        splitter1.addWidget(top_right)

        splitter2 = QSplitter(Qt.Orientation.Vertical)
        splitter2.addWidget(splitter1)
        splitter2.addWidget(bottom)

        hbox.addWidget(splitter2)
        self.setLayout(hbox)

        self.setWindowTitle('QSplitter')
        self.resize(600, 450)
        self.show()


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
