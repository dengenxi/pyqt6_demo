import sys
from PyQt6.QtWidgets import QMainWindow, QMenu, QApplication
from PyQt6.QtGui import QAction


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        menubar = self.menuBar()
        file_menu = menubar.addMenu("File")

        imp_menu = QMenu('Import', self)
        imp_act = QAction('Import Mail', self)
        imp_menu.addAction(imp_act)

        new_act = QAction('New', self)

        file_menu.addAction(new_act)
        file_menu.addMenu(imp_menu)

        self.setWindowTitle("子菜单")
        self.resize(600, 450)
        self.show()


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
