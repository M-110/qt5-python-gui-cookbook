import sys
import time

from PyQt5.QtWidgets import QApplication, QDialog

from demoProgressBar import Ui_Dialog

class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.updateBar)
        self.show()

    def updateBar(self):
        x = 0
        while x < 100:
            time.sleep(.05)
            x += 1
            self.ui.progressBar.setValue(x)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec())
