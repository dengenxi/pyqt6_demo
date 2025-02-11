import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (QWidget, QHBoxLayout, QVBoxLayout, QCheckBox, QApplication)
from PyQt6.QtGui import QFont


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):

        hbox = QHBoxLayout()

        cb = QCheckBox('显示标题', self)
        cb.move(20, 20)
        cb.toggle()
        cb.stateChanged.connect(self.change_title)

        hbox.addWidget(cb)
        hbox.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        vbox = QVBoxLayout()
        vbox.setAlignment(Qt.AlignmentFlag.AlignVCenter)
        vbox.addLayout(hbox)
        self.setLayout(vbox)

        self.resize(600, 450)
        self.setFont(QFont('LXGW Wenkai Screen'))
        self.setWindowTitle('QCheckBox')
        self.show()

    def change_title(self, state):
        if state == Qt.CheckState.Checked.value:
            self.setWindowTitle('QCheckBox')
        else:
            self.setWindowTitle(' ')


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
