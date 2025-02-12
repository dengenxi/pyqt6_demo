import sys
from PyQt6.QtWidgets import QWidget, QApplication
from PyQt6.QtGui import QColor, QFont, QPainter
from PyQt6.QtCore import Qt


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.text = "Лев Николаевич Толстой\nАнна Каренина"

        self.resize(600, 450)
        self.setWindowTitle('Drawing Text')
        self.show()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.draw_text(event, qp)
        qp.end()

    def draw_text(self, event, qp):
        qp.setPen(QColor(168, 34, 3))
        qp.setFont(QFont('LXGW WenKai Screen', 30))
        qp.drawText(event.rect(), Qt.AlignmentFlag.AlignCenter, self.text)


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
