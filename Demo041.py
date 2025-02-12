import sys
from PyQt6.QtWidgets import QWidget, QApplication
from PyQt6.QtGui import QPainter, QBrush
from PyQt6.QtCore import Qt


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.resize(830, 660)
        self.setWindowTitle('Brushes')
        self.show()

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        self.draw_brushes(painter)
        painter.end()

    def draw_brushes(self, painter):
        brush = QBrush(Qt.BrushStyle.SolidPattern)
        painter.setBrush(brush)
        painter.drawRect(20, 15, 250, 200)

        brush.setStyle(Qt.BrushStyle.Dense1Pattern)
        painter.setBrush(brush)
        painter.drawRect(290, 15, 250, 200)

        brush.setStyle(Qt.BrushStyle.Dense2Pattern)
        painter.setBrush(brush)
        painter.drawRect(560, 15, 250, 200)

        brush.setStyle(Qt.BrushStyle.DiagCrossPattern)
        painter.setBrush(brush)
        painter.drawRect(20, 230, 250, 200)

        brush.setStyle(Qt.BrushStyle.Dense5Pattern)
        painter.setBrush(brush)
        painter.drawRect(290, 230, 250, 200)

        brush.setStyle(Qt.BrushStyle.Dense6Pattern)
        painter.setBrush(brush)
        painter.drawRect(560, 230, 250, 200)

        brush.setStyle(Qt.BrushStyle.HorPattern)
        painter.setBrush(brush)
        painter.drawRect(20, 445, 250, 200)

        brush.setStyle(Qt.BrushStyle.VerPattern)
        painter.setBrush(brush)
        painter.drawRect(290, 445, 250, 200)

        brush.setStyle(Qt.BrushStyle.BDiagPattern)
        painter.setBrush(brush)
        painter.drawRect(560, 445, 250, 200)


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
