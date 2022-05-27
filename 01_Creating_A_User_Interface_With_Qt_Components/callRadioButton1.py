import sys

from PyQt5.QtWidgets import QDialog, QApplication

from demoRadioButton1 import Ui_Dialog


class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.radioButtonPython.toggled.connect(self.displayLanguage)
        self.ui.radioButtonCSharp.toggled.connect(self.displayLanguage)
        self.ui.radioButtonCpp.toggled.connect(self.displayLanguage)
        self.show()

    def displayLanguage(self):
        language = ''
        if self.ui.radioButtonPython.isChecked():
            language = "Python"
        if self.ui.radioButtonCSharp.isChecked():
            language = "C#"
        if self.ui.radioButtonCpp.isChecked():
            language = "C++"
        self.ui.labelOutput.setText(language)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())

