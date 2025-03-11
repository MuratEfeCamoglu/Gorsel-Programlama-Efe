from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt  # Qt.CaseInsensitive için eklendi
import sys

class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        layout = QGridLayout()
        self.setLayout(layout)

        # auto complete options                                                 
        names = ["Apple", "Alps", "Berry", "Cherry","Deniz","Efe" ]
        completer = QCompleter(names)
        # Büyük/küçük harf duyarsızlığı için:
        completer.setCaseSensitivity(Qt.CaseInsensitive)

        # create line edit and add auto complete                                
        self.lineedit = QLineEdit()
        self.lineedit.setCompleter(completer)
        layout.addWidget(self.lineedit, 0, 0)

app = QApplication(sys.argv)
screen = Window()
screen.show()
sys.exit(app.exec_())