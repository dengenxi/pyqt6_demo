import sys, random
from PyQt6.QtWidgets import (QWidget, QApplication)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPainter, QColor


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return QColor(r, g, b)


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Points')
        self.resize(800, 550)
        self.show()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.draw_points(qp)
        qp.end()

    def draw_points(self, qp):
        size = self.size()

        for i in range(4150):
            qp.setPen(random_color())
            x = random.randint(1, size.width() - 1)
            y = random.randint(1, size.height() - 1)
            random_color()
            qp.drawPoint(x, y)


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
