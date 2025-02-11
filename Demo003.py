import sys
from PyQt6.QtWidgets import (QWidget, QToolTip, QPushButton, QApplication)
from PyQt6.QtGui import QFont


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        QToolTip.setFont(QFont('LXGW WenKai Screen', 20))

        self.setToolTip("因为我们都太年轻，不知道天高地厚。")

        btn = QPushButton('我是按钮', self)
        btn.setToolTip('还吃，收你们来了!')
        btn.resize(btn.sizeHint())
        btn.setFont(QFont('LXGW WenKai Screen', 10))
        btn.move(50, 50)

        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle("Tooltips")
        self.show()


def main():
    app = QApplication(sys.argv)

    ex = Example()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
