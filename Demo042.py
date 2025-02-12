import sys
from PyQt6.QtWidgets import QWidget, QApplication
from PyQt6.QtGui import QPainter, QPainterPath


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Bézier curve')
        self.resize(800, 600)
        self.show()

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        self.draw_bezier_curve(painter)
        painter.end()

    def draw_bezier_curve(self, painter):
        path = QPainterPath()
        path.moveTo(30, 30)
        path.cubicTo(30, 30, 400, 700, 700, 30)

        painter.drawPath(path)


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()


