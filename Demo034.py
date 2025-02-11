import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (QWidget, QFrame, QHBoxLayout, QSplitter, QGridLayout, QLabel, QComboBox, QApplication)
from PyQt6.QtGui import QFont


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_top_left(self):
        self.top_left.setFrameShape(QFrame.Shape.StyledPanel)

        self.top_left_box = QHBoxLayout()

        self.source_combo = QComboBox(self)
        self.source_combo.addItem('北京')
        self.source_combo.addItem('上海')
        self.source_combo.addItem('广州')
        self.source_combo.addItem('深圳')

        self.top_left_box.addWidget(self.source_combo)
        self.top_left.setLayout(self.top_left_box)

    def init_top_right(self):
        self.top_right.setFrameShape(QFrame.Shape.StyledPanel)

        self.top_right_box = QHBoxLayout()
        self.destination_combo = QComboBox(self)

        self.destination_combo.addItem('重庆')
        self.destination_combo.addItem('宜昌')
        self.destination_combo.addItem('成都')
        self.destination_combo.addItem('横店')

        self.top_right_box.addWidget(self.destination_combo)

        self.top_right.setLayout(self.top_right_box)

    def init_bottom(self):
        self.bottom.setFrameShape(QFrame.Shape.StyledPanel)

        self.bottom_box = QHBoxLayout(self)
        self.bottom_box.addWidget(self.source_lbl, 2)
        self.right_label = QLabel('--->')
        self.right_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.bottom_box.addWidget(self.right_label, 1)
        self.bottom_box.addWidget(self.destination_lbl, 2)
        self.bottom.setFont(QFont('LXGW WenKai Screen', 20))

        self.bottom.setLayout(self.bottom_box)

    def init_ui(self):
        hbox = QHBoxLayout()

        self.source_lbl = QLabel("北京", self)
        self.source_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.destination_lbl = QLabel('重庆', self)
        self.destination_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.top_left = QFrame(self)
        self.init_top_left()

        self.top_right = QFrame(self)
        self.init_top_right()

        self.bottom = QFrame(self)
        self.init_bottom()

        splitter1 = QSplitter(Qt.Orientation.Horizontal)
        splitter1.addWidget(self.top_left)
        splitter1.setFixedHeight(200)
        splitter1.addWidget(self.top_right)

        splitter2 = QSplitter(Qt.Orientation.Vertical)
        splitter2.addWidget(splitter1)
        splitter2.addWidget(self.bottom)

        hbox.addWidget(splitter2)

        self.setLayout(hbox)

        self.source_combo.textActivated[str].connect(self.on_source_activated)
        self.destination_combo.textActivated[str].connect(self.on_destination_activated)

        self.resize(600, 450)
        self.setWindowTitle('QComboBox')
        self.show()

    def on_source_activated(self, text):
        self.source_lbl.setText(text)
        self.source_lbl.adjustSize()

    def on_destination_activated(self, text):
        self.destination_lbl.setText(text)
        self.destination_lbl.adjustSize()


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
