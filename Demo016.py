import sys
from PyQt6.QtWidgets import (QWidget, QMessageBox, QLabel, QLineEdit, QTextEdit, QPushButton, QHBoxLayout, QVBoxLayout, QGridLayout,
                             QApplication)
from PyQt6.QtGui import QFont


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def form(self):
        msg = QMessageBox()
        msg.setWindowTitle("你好")
        msg.setFont(QFont('LXGW WenKai Screen', 20))
        msg.setText(f"电影名：{self.title_edit.text()}\n导演：{self.director_edit.text()}\n描述：{self.description_edit.toPlainText().title()}")
        msg.exec()

    def quit(self):
        QApplication.instance().quit()

    def init_ui(self):
        ok_button = QPushButton('确定', self)
        ok_button.setFixedSize(80, 45)
        ok_button.setFont(QFont('LXGW WenKai Screen', 16, QFont.Weight.Bold))
        ok_button.setStyleSheet("""
            QPushButton {
                background-color: #409eff;
                border: none;
                border-radius: 6px;
                color: white;
                text-align: center;
                text-decoration: none;
                display: inline-block;
                cursor: pointer;
            }
            QPushButton:hover {
                background-color: rgb(121.3, 187.1, 255);
            }
            QPushButton:pressed {
                background-color: rgb(51.2, 126.4, 204);
            }
        """)
        ok_button.clicked.connect(self.form)
        cancel_button = QPushButton('取消', self)
        cancel_button.setFixedSize(80, 45)
        cancel_button.setFont(QFont('LXGW WenKai Screen', 16, QFont.Weight.Bold))
        cancel_button.setStyleSheet("""
            QPushButton {
                background-color: #909399;
                border: none;
                border-radius: 6px;
                color: white;
                text-align: center;
                text-decoration: none;
                display: inline-block;
                cursor: pointer;
            }
            QPushButton:hover {
                background-color: rgb(177.3, 179.4, 183.6);
            }
            QPushButton:pressed {
                background-color: rgb(115.2, 117.6, 122.4);
            }
        """)
        cancel_button.clicked.connect(quit)

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(ok_button)
        hbox.addWidget(cancel_button)

        title = QLabel("电影名：")
        title.setFont(QFont('LXGW WenKai Screen', 16))
        director = QLabel("导演：")
        director.setFont(QFont('LXGW WenKai Screen', 16))
        description = QLabel("简介：")
        description.setFont(QFont('LXGW WenKai Screen', 16))

        self.title_edit = QLineEdit()
        self.title_edit.setFixedHeight(40)
        self.director_edit = QLineEdit()
        self.director_edit.setFixedHeight(40)
        self.description_edit = QTextEdit()

        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(title, 1, 0)
        grid.addWidget(self.title_edit, 1, 1)

        grid.addWidget(director, 2, 0)
        grid.addWidget(self.director_edit, 2, 1)

        grid.addWidget(description, 3, 0)
        grid.addWidget(self.description_edit, 3, 1)

        vbox = QVBoxLayout()
        vbox.addLayout(grid)
        vbox.addSpacing(20)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

        self.setFont(QFont('LXGW WenKai Screen', 16))
        self.resize(600, 450)
        self.setWindowTitle('示例：回复')
        # self.center()
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
