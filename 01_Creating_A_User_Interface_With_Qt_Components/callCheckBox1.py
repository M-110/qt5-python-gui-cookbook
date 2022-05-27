import sys

from PyQt5.QtWidgets import QDialog, QApplication

from demoCheckBox1 import Ui_Dialog


class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.checkBoxCheese.stateChanged.connect(self.displayAmount)
        self.ui.checkBoxOlives.stateChanged.connect(self.displayAmount)
        self.ui.checkBoxSausage.stateChanged.connect(self.displayAmount)
        self.displayAmount()
        self.show()

    def displayAmount(self):
        total = 10
        if self.ui.checkBoxCheese.isChecked():
            total += 1
        if self.ui.checkBoxSausage.isChecked():
            total += 2
        if self.ui.checkBoxOlives.isChecked():
            total += 1
        self.ui.labelAmount.setText(f'Total: ${total}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())

