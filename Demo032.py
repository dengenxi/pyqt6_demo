import sys
from PyQt6.QtWidgets import (QWidget, QVBoxLayout, QLabel, QLineEdit, QApplication)
from PyQt6.QtCore import Qt

class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        vbox = QVBoxLayout()

        self.lbl = QLabel(self)
        qle = QLineEdit(self)
        qle.textChanged[str].connect(self.on_changed)

        vbox.addWidget(self.lbl)
        vbox.addWidget(qle)
        vbox.setAlignment(Qt.AlignmentFlag.AlignVCenter)

        self.setLayout(vbox)

        self.resize(600, 450)
        self.setWindowTitle('QLineEdit')

        self.show()

    def on_changed(self, text):
        self.lbl.setText(text)
        self.lbl.adjustSize()


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
