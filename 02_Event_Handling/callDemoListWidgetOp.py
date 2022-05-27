import sys

from PyQt5.QtWidgets import QApplication, QDialog, QInputDialog

from demoListWidgetOp import Ui_Dialog

class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButtonAdd.clicked.connect(self.addItem)
        self.ui.pushButtonEdit.clicked.connect(self.editItem)
        self.ui.pushButtonDelete.clicked.connect(self.deleteItem)
        self.ui.pushButtonDeleteAll.clicked.connect(self.deleteAllItems)
        self.show()

    def addItem(self):
        self.ui.listWidgetNames.addItem(self.ui.lineEditName.text())
        self.ui.lineEditName.setText("")

    def editItem(self):
        row = self.ui.listWidgetNames.currentRow()
        text, success = QInputDialog.getText(self, "Edit", "Enter new text")
        if success and text:
            self.ui.listWidgetNames.takeItem(row)
            self.ui.listWidgetNames.insertItem(row, text)

    def deleteItem(self):
        self.ui.listWidgetNames.takeItem(self.ui.listWidgetNames.currentRow())

    def deleteAllItems(self):
        self.ui.listWidgetNames.clear()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec())
