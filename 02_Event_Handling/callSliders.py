import sys

from PyQt5.QtWidgets import QApplication, QDialog

from demoSliders import Ui_Dialog

class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.horizontalScrollBarSugar.valueChanged.connect(self.setSugar)
        self.ui.verticalScrollBarPulseRate.valueChanged.connect(self.setPulse)
        self.ui.horizontalSliderBloodPressure.valueChanged.connect(
            self.setBloodPressure)
        self.ui.verticalSliderCholesterolLevel.valueChanged.connect(
            self.setCholesterol)
        self.show()

    def setSugar(self, value):
        self.ui.lineEditResult.setText(f"Sugar Level: {value}")

    def setPulse(self, value):
        self.ui.lineEditResult.setText(f"Pulse Rate: {value}")

    def setBloodPressure(self, value):
        self.ui.lineEditResult.setText(f"Blood Pressure: {value}")

    def setCholesterol(self, value):
        self.ui.lineEditResult.setText(f"Cholesterol: {value}")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec())
