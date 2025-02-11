import sys
from PyQt6.QtWidgets import QApplication, QWidget


def main():

    app = QApplication(sys.argv)

    w = QWidget()
    w.resize(800, 600)
    w.move(300, 150)

    w.setWindowTitle("嘻嘻哈哈")
    w.show()

    sys.exit(app.exec())


if __name__ == '__main__':
    main()