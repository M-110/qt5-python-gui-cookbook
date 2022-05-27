import sys

from PyQt5.QtWidgets import QDialog, QApplication

from demoRadioButton2 import Ui_Dialog


class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.radioButtonMedium.toggled.connect(self.displaySelected)
        self.ui.radioButtonLarge.toggled.connect(self.displaySelected)
        self.ui.radioButtonXL.toggled.connect(self.displaySelected)
        self.ui.radioButtonXXL.toggled.connect(self.displaySelected)
        self.ui.radioButtonDebitCard.toggled.connect(self.displaySelected)
        self.ui.radioButtonNetBanking.toggled.connect(self.displaySelected)
        self.ui.radioButtonCash.toggled.connect(self.displaySelected)
        self.show()

    def displaySelected(self):
        selected1 = ''
        selected2 = ''
        if self.ui.radioButtonMedium.isChecked():
            selected1 = 'Medium'
        if self.ui.radioButtonLarge.isChecked():
            selected1 = 'Large'
        if self.ui.radioButtonXL.isChecked():
            selected1 = 'XL'
        if self.ui.radioButtonXXL.isChecked():
            selected1 = 'XXL'
        if self.ui.radioButtonDebitCard.isChecked():
            selected2 = 'Debit/Credit Card'
        if self.ui.radioButtonNetBanking.isChecked():
            selected2 = 'NetBanking'
        if self.ui.radioButtonCash.isChecked():
            selected2 = 'Cash on Delivery'
        self.ui.labelSelected.setText(f'{selected1} - {selected2}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())

