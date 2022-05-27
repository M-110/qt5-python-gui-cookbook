import sys

from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QDialog

from demoFontComboBox import Ui_Dialog


class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        myFont = QFont(self.ui.fontComboBox.currentText(), 15)
        self.ui.textEdit.setFont(myFont)
        self.ui.fontComboBox.currentFontChanged.connect(self.changeFont)
        self.show()

    def changeFont(self):
        myFont = QFont(self.ui.fontComboBox.currentText(), 15)
        self.ui.textEdit.setFont(myFont)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec())
