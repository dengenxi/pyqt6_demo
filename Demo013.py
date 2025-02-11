import sys
from PyQt6.QtWidgets import QMainWindow, QLabel, QApplication


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        label1 = QLabel('日月同生', self)
        label1.move(15, 10)

        label2 = QLabel('千灵重元', self)
        label2.move(35, 50)

        label3 = QLabel('天地无量乾坤圈', self)
        label3.move(55, 90)

        self.resize(600, 450)
        self.setWindowTitle('绝对定位')
        self.center()
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = self.screen().availableGeometry().center()

        qr.moveCenter(cp)
        self.move(qr.topLeft())


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
