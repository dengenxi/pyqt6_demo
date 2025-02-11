import sys
from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6.QtGui import QIcon, QAction


class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def quit(self):
        QApplication.instance().quit()

    def initUI(self):

        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&文件')

        exitAct = QAction('&退出', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip("退出应用")
        exitAct.triggered.connect(self.quit)

        newTabAct = QAction("&新建标签页", self)
        newTabAct.setShortcut('Ctrl+N')

        newWindowAct = QAction("&新建窗口", self)
        newWindowAct.setShortcut('Ctrl+Shift+N')

        openAct = QAction("&打开", self)
        openAct.setShortcut('Ctrl+o')

        saveAct = QAction("&保存", self)
        saveAct.setShortcut('Ctrl+S')

        saveAsAct = QAction("&另存为", self)
        saveAsAct.setShortcut('Ctrl+Shift+S')

        saveAllAct = QAction("&全部保存", self)
        saveAllAct.setShortcut('Ctrl+Alt+S')

        pageSettingAct = QAction("&页面设置", self)

        printAct = QAction("&打印", self)
        printAct.setShortcut('Ctrl+P')

        closeTabAct = QAction("&关闭选项卡", self)
        closeTabAct.setShortcut('Ctrl+W')

        closeWindowAct = QAction("&关闭窗口", self)
        closeWindowAct.setShortcut('Ctrl+Shift+W')

        fileMenu.addAction(newTabAct)
        fileMenu.addAction(newWindowAct)
        fileMenu.addAction(openAct)
        fileMenu.addAction(saveAct)
        fileMenu.addAction(saveAsAct)
        fileMenu.addAction(saveAllAct)
        fileMenu.addSeparator()
        fileMenu.addAction(pageSettingAct)
        fileMenu.addAction(printAct)
        fileMenu.addSeparator()
        fileMenu.addAction(closeTabAct)
        fileMenu.addAction(closeWindowAct)
        fileMenu.addAction(exitAct)

        editMenu = menubar.addMenu('&编辑')

        rollbackAct = QAction('&撤销', self)
        rollbackAct.setShortcut('Ctrl+Z')

        cutAct = QAction('&剪切', self)
        cutAct.setShortcut('Ctrl+X')

        copyAct = QAction('&复制', self)
        copyAct.setShortcut('Ctrl+C')

        pasteAct = QAction('&粘贴', self)
        pasteAct.setShortcut('Ctrl+V')

        deleteAct = QAction('&删除', self)
        deleteAct.setShortcut('Del')

        searchAct = QAction('&查找', self)
        searchAct.setShortcut('Ctrl+F')

        findNextAct = QAction('&查找下一个', self)
        findNextAct.setShortcut('F3')

        findPreAct = QAction('&查找上一个', self)
        findPreAct.setShortcut('Shift+F3')

        replaceAct = QAction('&替换', self)
        replaceAct.setShortcut('Ctrl+H')

        gotoAct = QAction('&转到', self)
        gotoAct.setShortcut('Ctrl+G')

        selectAllAct = QAction('&全选', self)
        selectAllAct.setShortcut('Ctrl+A')

        dateTimeAct = QAction('&时间/日期', self)
        dateTimeAct.setShortcut('F5')

        fontAct = QAction('&字体', self)

        editMenu.addAction(rollbackAct)
        editMenu.addSeparator()
        editMenu.addAction(cutAct)
        editMenu.addAction(copyAct)
        editMenu.addAction(pasteAct)
        editMenu.addAction(deleteAct)
        editMenu.addSeparator()
        editMenu.addAction(searchAct)
        editMenu.addAction(findNextAct)
        editMenu.addAction(findPreAct)
        editMenu.addAction(replaceAct)
        editMenu.addAction(gotoAct)
        editMenu.addSeparator()
        editMenu.addAction(selectAllAct)
        editMenu.addAction(dateTimeAct)
        editMenu.addSeparator()
        editMenu.addAction(fontAct)

        lookMenu = menubar.addMenu("&查看")

        zoomMenu = lookMenu.addMenu('&缩放')

        zoom_plus_act = QAction('&放大', zoomMenu)
        zoom_plus_act.setShortcut('Ctrl++')

        zoom_sub_act = QAction('&缩小', zoomMenu)
        zoom_sub_act.setShortcut('Ctrl+-')

        change_default_act = QAction('&还原默认缩放', zoomMenu)
        change_default_act.setShortcut('Ctrl+0')

        zoomMenu.addAction(zoom_plus_act)
        zoomMenu.addAction(zoom_sub_act)
        zoomMenu.addAction(change_default_act)

        statusbarAct = QAction('状态栏', self, checkable=True)
        statusbarAct.setChecked(True)

        auto_wrap_act = QAction('自动换行', self, checkable=True)
        auto_wrap_act.setChecked(True)

        lookMenu.addMenu(zoomMenu)
        lookMenu.addAction(statusbarAct)
        lookMenu.addAction(auto_wrap_act)

        self.setWindowTitle("简单菜单")
        self.center()
        self.resize(600, 450)
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