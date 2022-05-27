import sys

from PyQt5.QtWidgets import QApplication, QDialog

from demoSpinner import Ui_Dialog

class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.spinBoxBookAmount.editingFinished.connect(self.updateAmounts)
        self.ui.doubleSpinBoxSugarAmount.editingFinished.connect(
            self.updateAmounts)
        self.show()

    def get_amount(self, lineEdit):
        try:
            return float(lineEdit.text())
        except ValueError as e:
            print(e)
            lineEdit.setText("0")
            return 0

    def updateAmounts(self):
        bookPrice = self.get_amount(self.ui.lineEditBookPrice)
        sugarPrice = self.get_amount(self.ui.lineEditSugarPrice)
        bookAmount = self.ui.spinBoxBookAmount.value()
        sugarAmount = self.ui.doubleSpinBoxSugarAmount.value()
        self.ui.lineEditBookAmount.setText(str(bookAmount))
        self.ui.lineEditSugarAmount.setText(str(sugarAmount))
        self.ui.labelResult.setText(f'${bookPrice * bookAmount + sugarPrice * sugarAmount:.2f}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec())
