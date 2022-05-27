import sys

from PyQt5.QtWidgets import QApplication, QDialog

from demoComboBox import Ui_Dialog

class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.comboBox.currentIndexChanged.connect(self.updateText)
        self.show()

    def updateText(self):
        text = self.ui.comboBox.currentText()
        self.ui.labelResult.setText(text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec())
