from PyQt6.QtCore import QDate, QTime, QDateTime, Qt

now = QDate.currentDate()
print(now.toString(Qt.DateFormat.ISODate))
print(now.toString(Qt.DateFormat.RFC2822Date))

datetime = QTime.currentTime()
print(datetime.toString())

time = QDateTime.currentDateTime()
print(time.toString(Qt.DateFormat.ISODate))
