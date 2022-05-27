import sys

from PyQt5.QtWidgets import QApplication, QDialog

from demoComputeRoomRent import Ui_Dialog


class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.roomTypes = dict(
            Suite=40,
            Luxery=30,
            Deluxe=20,
            Standard=10
        )
        self.updateComboBox()
        self.ui.pushButton.clicked.connect(self.computeRoomRent)
        self.show()

    def updateComboBox(self):
        for room in self.roomTypes:
            self.ui.comboBox.addItem(room)

    def computeRoomRent(self):
        date = str(self.ui.calendarWidget.selectedDate().toPyDate())
        numberOfDays = self.ui.spinBox.value()
        roomType = self.ui.comboBox.currentText()
        roomRate = self.roomTypes[roomType]
        cost = roomRate * numberOfDays
        text = f'${cost} for {numberOfDays} nights in a {roomType} room on {date}'
        self.ui.labelResult.setText(text)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec())
