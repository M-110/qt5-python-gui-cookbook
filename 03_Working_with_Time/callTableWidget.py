import sys

from PyQt5.QtWidgets import QApplication, QDialog, QTableWidgetItem

from demoTableWidget import Ui_Dialog

class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.updateContent()
        self.show()

    def updateContent(self):
        data = dict(
            Suite=40,
            Luxery=30,
            Deluxe=20,
            Standard=10
        )
        for i, (k, v) in enumerate(data.items()):
            self.ui.tableWidget.setItem(i, 0, QTableWidgetItem(k))
            self.ui.tableWidget.setItem(i, 1, QTableWidgetItem(str(v)))



if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec())
