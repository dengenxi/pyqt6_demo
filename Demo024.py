import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QSizePolicy, QLabel, QFontDialog,
                             QApplication)


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        hbox = QHBoxLayout()
        vbox = QVBoxLayout()

        btn = QPushButton('选择字体', self)
        btn.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)

        vbox.addWidget(btn)

        btn.clicked.connect(self.show_dialog)

        self.lbl = QLabel('终会与你同行', self)
        self.lbl.setStyleSheet("font-size: 100px;")

        vbox.addWidget(self.lbl)
        hbox.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        vbox.setAlignment(Qt.AlignmentFlag.AlignVCenter)
        hbox.addLayout(vbox)
        self.setLayout(hbox)

        self.setWindowTitle('QFontDialog')
        self.setStyleSheet("font-size: 20px;")
        self.resize(600, 450)
        self.show()

    def show_dialog(self):
        font, ok = QFontDialog.getFont()

        if ok:
            self.lbl.setFont(font)


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
