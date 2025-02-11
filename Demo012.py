import sys
from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6.QtGui import QIcon, QAction, QPixmap
import images


class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def quit(self):
        QApplication.instance().quit()

    def initUI(self):

        exit_act = QAction(QIcon(QPixmap(':icon/exit.png')), '&退出', self)
        exit_act.setShortcut('Ctrl+Q')
        exit_act.triggered.connect(self.quit)

        toolbar = self.addToolBar('退出软件')
        toolbar.addAction(exit_act)

        self.setWindowTitle('工具栏')
        self.resize(600, 400)
        self.show()


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
