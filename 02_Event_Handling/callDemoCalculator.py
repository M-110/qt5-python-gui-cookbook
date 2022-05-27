import sys

from PyQt5.QtWidgets import QApplication, QDialog

from demoCalculator import Ui_Dialog

class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButtonPlus.clicked.connect(self.add)
        self.ui.pushButtonMinus.clicked.connect(self.subtract)
        self.ui.pushButtonMultiply.clicked.connect(self.multiply)
        self.ui.pushButtonDivide.clicked.connect(self.divide)
        self.show()

    def get_values(self):
        try:
            a = int(self.ui.lineEditA.text())
        except ValueError:
            a = 0
            self.ui.lineEditA.setText("0")
        try:
            b = int(self.ui.lineEditB.text())
        except ValueError:
            b = 0
            self.ui.lineEditB.setText("0")
        return a, b

    def add(self):
        a, b = self.get_values()
        self.ui.labelResult.setText(str(a + b))

    def subtract(self):
        a, b = self.get_values()
        self.ui.labelResult.setText(str(a - b))

    def multiply(self):
        a, b = self.get_values()
        self.ui.labelResult.setText(str(a * b))

    def divide(self):
        a, b = self.get_values()
        if b == 0:
            self.ui.labelResult.setText("NaN")
        else:
            self.ui.labelResult.setText(str(a // b))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec())
