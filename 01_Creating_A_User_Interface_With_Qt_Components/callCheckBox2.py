import sys

from PyQt5.QtWidgets import QDialog, QApplication

from demoCheckBox2 import Ui_Dialog


class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        for attributeName, attributeValue in self.ui.__dict__.items():
            if attributeName.startswith("checkBox"):
                attributeValue.stateChanged.connect(self.displayAmount)
        self.ui.groupBoxIceCream.toggled.connect(self.displayAmount)
        self.ui.groupBoxDrinks.toggled.connect(self.displayAmount)
        self.displayAmount()
        self.show()

    def displayAmount(self):
        total = 0
        if self.ui.groupBoxIceCream.isChecked():
            total += self.ui.checkBoxMint.isChecked() * 4
            total += self.ui.checkBoxCookieDough.isChecked() * 2
            total += self.ui.checkBoxBanana.isChecked() * 5
            total += self.ui.checkBoxRainbow.isChecked() * 7
        if self.ui.groupBoxDrinks.isChecked():
            total += self.ui.checkBoxPop.isChecked() * 5
            total += self.ui.checkBoxWater.isChecked()
            total += self.ui.checkBoxJuice.isChecked() * 3

        self.ui.labelAmount.setText(f'Total: ${total}')




if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())

