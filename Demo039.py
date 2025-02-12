import sys
from PyQt6.QtWidgets import QWidget, QApplication
from PyQt6.QtGui import QPainter, QColor


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Colors')
        self.resize(800, 600)
        self.show()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.draw_rectangles(qp)
        qp.end()

    def draw_rectangles(self, qp):
        color = QColor(0, 0, 0)
        color.setNamedColor('#d4d4d4')
        qp.setPen(color)

        qp.setBrush(QColor(200, 0, 0))
        qp.drawRect(60, 200, 200, 200)

        qp.setBrush(QColor(255, 80, 0, 160))
        qp.drawRect(300, 200, 200, 200)

        qp.setBrush(QColor(25, 0, 90, 200))
        qp.drawRect(540, 200, 200, 200)


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
