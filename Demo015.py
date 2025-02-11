import sys
from PyQt6.QtWidgets import (QWidget, QGridLayout, QPushButton, QApplication)
from PyQt6.QtGui import QFont


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        grid = QGridLayout()
        self.setLayout(grid)

        names = ['Cls', 'Bck', '', 'Close',
                 '7', '8', '9', '/',
                 '4', '5', '6', '*',
                 '1', '2', '3', '-',
                 '0', '.', '=', '+']

        positions = [(i, j) for i in range(5) for j in range(4)]

        for position, name in zip(positions, names):
            if name == '':
                continue

            button = QPushButton(name)
            button.setStyleSheet("""
                QPushButton {
                background-color: #4CAF50; /* 背景颜色 */
                border-style: outset;
                border-width: 2px;
                border-radius: 10px; /* 设置圆角 */
                border-color: beige;
                color: #fff;
                font-family: 'LXGW WenKai Screen';
                font: bold 25px;
                min-width: 8em;
                height: 80px;
                padding: 6px;
            }
            QPushButton:hover {
                background-color: #45a049; /* 鼠标悬停时的背景颜色 */
            }
            QPushButton:pressed {
                background-color: #3e8e41; /* 鼠标按下时的背景颜色 */
            }
            """)
            grid.addWidget(button, *position)

        self.setWindowTitle('QGridLayout')
        self.setGeometry(200, 200, 600, 450)
        self.show()


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
