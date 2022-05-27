import sys

from PyQt5.QtWidgets import QDialog, QApplication

from lineEditClass import Ui_Dialog

class Student:
    def __init__(self, name):
        self.name = name

    def print_name(self):
        print(self.name)

class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.displayMessage)

    def displayMessage(self):
        student = Student(self.ui.lineEdit.text())
        self.ui.labelResult.setText(f'Hello {student.name}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec())
