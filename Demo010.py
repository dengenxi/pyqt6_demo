import sys
from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6.QtGui import QAction


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        status_bar = self.statusBar()
        status_bar.showMessage("因为我们都太年轻，不知道天高地厚。")

        menu_bar = self.menuBar()
        view_menu = menu_bar.addMenu("View")

        view_stat_act = QAction('View Statusbar', self, checkable=True)
        view_stat_act.setStatusTip('View Statusbar')
        view_stat_act.setChecked(True)
        view_stat_act.triggered.connect(self.toggleMenu)

        view_menu.addAction(view_stat_act)

        self.setWindowTitle("勾选菜单")
        self.resize(600, 450)
        self.show()

    def toggleMenu(self, state):
        if state:
            self.statusBar().show()
        else:
            self.statusBar().hide()


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
