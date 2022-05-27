import sys

from PyQt5.QtWidgets import QApplication, QDialog

from demoCalendar import Ui_Dialog

class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.calendarWidget.selectionChanged.connect(self.displayDate)
        self.show()

    def displayDate(self):
        self.ui.dateEdit.setDate(self.ui.calendarWidget.selectedDate())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec())
