import sys

from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QApplication, QColorDialog, QDialog

from demoColorDialog import Ui_Dialog


class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        color = QColor(0, 0, 0)
        self.ui.frame.setStyleSheet(f"QWidget {{ background-color: {color.name()} }}")
        self.ui.pushButton.clicked.connect(self.changeColor)
        self.show()

    def changeColor(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.ui.frame.setStyleSheet(f"QWidget {{ background-color: {color.name()} }}")
            self.ui.label.setText(color.name())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec())
