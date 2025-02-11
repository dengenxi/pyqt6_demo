import sys
from PyQt6.QtWidgets import (QWidget, QCalendarWidget, QLabel, QVBoxLayout, QApplication)
from PyQt6.QtCore import QDate


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        vbox = QVBoxLayout()

        calendar = QCalendarWidget(self)
        calendar.setGridVisible(True)
        calendar.clicked[QDate].connect(self.show_date)

        vbox.addWidget(calendar)

        self.lbl = QLabel(self)
        date = calendar.selectedDate()
        self.lbl.setText(date.toString('yyyy-MM-dd'))

        vbox.addWidget(self.lbl)

        self.setLayout(vbox)

        self.resize(350, 300)
        self.setWindowTitle('Calendar')
        self.show()

    def show_date(self, date):
        self.lbl.setText(date.toString('yyyy-MM-dd'))


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
