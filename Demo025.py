import sys
from PyQt6.QtWidgets import (QMainWindow, QFileDialog, QLabel, QTextEdit, QApplication)
from PyQt6.QtGui import (QIcon, QAction, QPixmap)
from pathlib import Path
import images


class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.init_ui()

    def quit(self):
        QApplication.instance().quit()

    def create_new_file_handle(self):
        self.setCentralWidget(self.text_edit)

    def create_file_menu(self, menubar):
        open_file = QAction(QIcon(QPixmap(":icon/open.png")), '&打开文件', self)
        open_file.setShortcut('Ctrl+O')
        open_file.setStatusTip('打开新文件')
        open_file.triggered.connect(self.show_dialog)

        new_file_act = QAction(QIcon(QPixmap(":icon/file.png")), '&新建文件', self)
        new_file_act.setShortcut('Ctrl+N')
        new_file_act.setStatusTip('创建一个新文件')
        new_file_act.triggered.connect(self.create_new_file_handle)

        save_act = QAction(QIcon(QPixmap(":icon/save.png")), '&保存文件', self)
        save_act.setShortcut('Ctrl+S')
        save_act.setStatusTip('保存当前文件')

        close_act = QAction(QIcon(QPixmap(":icon/exit.png")), '&退出软件', self)
        close_act.setStatusTip('退出软件')
        close_act.triggered.connect(self.quit)

        file_menu = menubar.addMenu("&文件")
        file_menu.addAction(new_file_act)
        file_menu.addAction(open_file)
        file_menu.addAction(save_act)
        file_menu.addSeparator()
        file_menu.addAction(close_act)

        toolbar = self.addToolBar('Open')
        toolbar.addAction(open_file)
        toolbar.addAction(save_act)
        toolbar.addSeparator()
        toolbar.addAction(close_act)

    def create_about_menu(self, menubar):
        about_menu = menubar.addMenu("&关于")

        author_act = QAction(QIcon(QPixmap(":icon/dragon.png")), '&作者：浩熙欢妳', self)
        about_qq_act = QAction(QIcon(QPixmap(":icon/qq.png")), '扣扣：776063641', self)
        about_douyin_act = QAction(QIcon(QPixmap(":icon/douyin.png")), '抖音：coderqin', self)

        about_menu.addAction(author_act)
        about_menu.addSeparator()
        about_menu.addAction(about_qq_act)
        about_menu.addAction(about_douyin_act)

    def init_ui(self):
        self.text_edit = QTextEdit()

        # self.setCentralWidget(self.text_edit)
        self.statusBar()

        menubar = self.menuBar()

        self.create_file_menu(menubar)
        self.create_about_menu(menubar)

        label = QLabel('我命由我不由天')
        self.statusBar().addWidget(label)

        self.setWindowTitle('HaoNote')
        self.setWindowIcon(QIcon(QPixmap(":icon/dragon.png")))
        self.resize(600, 450)
        self.show()

    def show_dialog(self):
        self.setCentralWidget(self.text_edit)

        home_dir = str(Path.home())
        fname = QFileDialog.getOpenFileName(self, '打开文件', home_dir)

        if fname[0]:
            with open(fname[0], 'r') as f:
                data = f.read()
                self.text_edit.setText(data)


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
