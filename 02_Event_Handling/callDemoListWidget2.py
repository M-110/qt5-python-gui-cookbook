import sys

from PyQt5.QtWidgets import QApplication, QDialog

from demoListWidget2 import Ui_Dialog

class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.listWidgetColors.itemSelectionChanged.connect(self.displayText)
        self.show()

    def displayText(self):
        self.ui.listWidgetColorsSelected.clear()
        for item in self.ui.listWidgetColors.selectedItems():
            self.ui.listWidgetColorsSelected.addItem(item.text())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec())
