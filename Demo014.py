import sys
from PyQt6.QtWidgets import (QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QApplication)


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def quit(self):
        QApplication.instance().quit()

    def initUI(self):

        ok_button = QPushButton('确定', self)
        cancel_button = QPushButton('取消', self)

        ok_button.clicked.connect(self.quit)
        cancel_button.clicked.connect(self.quit)

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(ok_button)
        hbox.addWidget(cancel_button)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

        self.resize(600, 450)
        self.setWindowTitle('QHBoxLayout')
        self.show()


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
