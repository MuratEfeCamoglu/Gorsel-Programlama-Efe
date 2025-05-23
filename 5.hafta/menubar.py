from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys

class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        layout = QGridLayout()
        self.setLayout(layout)

        # create menu
        menubar = QMenuBar()
        layout.addWidget(menubar, 0, 0)
        actionFile = menubar.addMenu("File")
        actionFile.addAction("Efe")
        actionFile.addAction("Open")
        actionFile.addSeparator()
        actionFile.addAction("Save")
        actionFile.addSeparator()
        actionFile.addAction("Quit")
        menubar.addMenu("Edit")
        menubar.addMenu("View")
        menubar.addMenu("Help")

        # add textbox
        tbox = QPlainTextEdit()
        layout.addWidget(tbox, 1, 0) 
        
app = QApplication(sys.argv)
screen = Window()
screen.show()
sys.exit(app.exec_())