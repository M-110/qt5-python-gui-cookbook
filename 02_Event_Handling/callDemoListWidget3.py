import sys

from PyQt5.QtWidgets import QApplication, QDialog

from demoListWidget3 import Ui_Dialog

class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButtonAdd.clicked.connect(self.addItem)
        self.show()

    def addItem(self):
        self.ui.listWidgetNames.addItem(self.ui.lineEditName.text())
        self.ui.lineEditName.setText("")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec())
