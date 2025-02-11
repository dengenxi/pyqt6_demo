import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (QMainWindow, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QApplication)
from PyQt6.QtGui import QFont


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        hbox = QHBoxLayout()

        btn1 = QPushButton('哪吒', self)
        btn1.setFixedHeight(40)
        btn2 = QPushButton('敖丙', self)
        btn2.setFixedHeight(40)

        btn1.clicked.connect(self.buttonClick)
        btn2.clicked.connect(self.buttonClick)

        # btn1.move(100, 20)
        # btn2.move(200, 20)

        hbox.addWidget(btn1)
        hbox.addWidget(btn2)
        hbox.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        vbox = QVBoxLayout()
        vbox.addLayout(hbox)
        vbox.setAlignment(Qt.AlignmentFlag.AlignVCenter)

        widget = QWidget(self)
        widget.setLayout(vbox)
        self.setCentralWidget(widget)

        self.resize(600, 450)
        self.setWindowTitle('事件触发者')
        self.statusBar().showMessage("暂无点击事件")
        self.setFont(QFont('LXGW WenKai Screen', 14))
        self.show()

    def buttonClick(self):
        sender = self.sender()

        msg = f"{sender.text()} 被点击了"
        self.statusBar().showMessage(msg)


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
