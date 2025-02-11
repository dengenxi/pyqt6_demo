import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (QWidget, QVBoxLayout, QPushButton, QLabel, QInputDialog, QApplication)
from PyQt6.QtGui import QFont


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        vbox = QVBoxLayout()

        self.btn = QPushButton('弹窗', self)
        self.btn.clicked.connect(self.show_dialog)

        self.le = QLabel(self)

        vbox.addWidget(self.btn)
        vbox.addSpacing(20)
        vbox.addWidget(self.le)
        vbox.setAlignment(Qt.AlignmentFlag.AlignVCenter)

        self.setLayout(vbox)

        self.setWindowTitle('QInputDialog')
        self.setFont(QFont('LXGW WenKai Screen', 20))
        self.resize(450, 350)
        self.show()

    def show_dialog(self):
        text, ok = QInputDialog.getText(self, '敏感操作', '请输入你的密码')

        if ok:
            if text == '123456':
                self.le.setText('验证通过')
                self.le.setStyleSheet("""
                    color: green;
                    font-size: 20px;
                    font-family: 'LXGW WenKai Screen';
                """)
            else:
                self.le.setText('验证不通过')
                self.le.setStyleSheet("""
                    color: red;
                    font-size: 20px;
                    font-family: 'LXGW WenKai Screen';
                """)

def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
