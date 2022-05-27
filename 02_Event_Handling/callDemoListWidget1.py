import sys

from PyQt5.QtWidgets import QApplication, QDialog

from demoListWidget1 import Ui_Dialog

class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.listWidgetColors.itemClicked.connect(self.displayText)
        self.show()

    def displayText(self):
        self.ui.labelResult.setText(self.ui.listWidgetColors.currentItem().text())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec())
