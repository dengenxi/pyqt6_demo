import sys
from PyQt6.QtWidgets import QWidget, QPushButton, QApplication
from PyQt6.QtGui import QFont


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def quit(self):
        QApplication.instance().quit()

    def initUI(self):
        qbtn = QPushButton('退出软件', self)
        qbtn.setFont(QFont('LXGW WenKai Screen', 20))
        qbtn.clicked.connect(quit)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(50, 50)

        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('按钮退出')
        self.show()


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
