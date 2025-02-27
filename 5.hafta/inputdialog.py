from PyQt5.QtWidgets import (QWidget, QPushButton, QInputDialog, QApplication, QLabel)
import sys

class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Add button                                                                                                     
        self.btn = QPushButton('Show Input Dialog', self)
        self.btn.move(30, 20)
        self.btn.clicked.connect(self.showDialog)

	# Add label                                                                                                      
        self.le = QLabel(self)
        self.le.move(30, 62)
        self.le.resize(400,22)

        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Input dialog')
        self.show()


    def showDialog(self):
        text, ok = QInputDialog.getText(self, 'Input Dialog', 'Enter text:')
        if ok:
            self.le.setText(str(text))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())