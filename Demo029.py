import sys
from PyQt6.QtWidgets import (QWidget, QProgressBar, QPushButton, QApplication)
from PyQt6.QtCore import QBasicTimer


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.pbar = QProgressBar(self)
        self.pbar.setGeometry(30, 40, 200, 25)

        self.btn = QPushButton('开始', self)
        self.btn.clicked.connect(self.do_action)
        self.btn.move(40, 80)

        self.timer = QBasicTimer()
        self.step = 0

        self.resize(280, 170)
        self.setWindowTitle('QProgressBar')
        self.show()

    def timerEvent(self, event):
        if self.step >= 100:
            self.timer.stop()
            self.btn.setText('完成')
            return
        self.step += 1
        self.pbar.setValue(self.step)

    def do_action(self):
        if self.timer.isActive():
            self.timer.stop()
            self.btn.setText("开始")
        else:
            self.timer.start(100, self)
            self.btn.setText('暂停')


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
