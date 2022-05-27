import sys

from PyQt5.QtWidgets import QApplication, QFileDialog, QMainWindow

from demoFileDialog import Ui_MainWindow

class MyForm(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.actionOpen.triggered.connect(self.openFileDialog)
        self.ui.actionSave.triggered.connect(self.saveFileDialog)
        self.show()

    def openFileDialog(self):
        filename, ok = QFileDialog.getOpenFileName(self, "Open file")
        if filename and ok:
            with open(filename) as f:
                data = f.read()
                self.ui.textEdit.setText(data)

    def saveFileDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        filename, ok = QFileDialog.getSaveFileName(self, "Save file",
                                                   "",
                                                   "All Files(*);;Text Files(*.txt)",
                                                   options=options)
        if ok:
            with open(filename, 'w') as f:
                f.write(self.ui.textEdit.toPlainText())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec())
