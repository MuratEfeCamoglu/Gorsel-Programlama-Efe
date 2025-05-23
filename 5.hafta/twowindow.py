import sys
from PyQt5 import QtGui
from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton, QLabel)

class Window2(QMainWindow):                         
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Window22222")

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.title = "First Window"
        self.top = 100
        self.left = 100
        self.width = 680
        self.height = 500

        self.pushButton = QPushButton("Start", self)
        self.pushButton.move(275, 200)
        self.pushButton.setToolTip("<h3>Start the Session</h3>")

        self.pushButton.clicked.connect(self.window2)              

        self.main_window()

    def main_window(self):
        self.label = QLabel("Manager", self)
        self.label.move(285, 175)
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.show()

    def window2(self):                                           
        self.w = Window2()
        self.w.show()
        self.hide()
    def window2(self):                                           
        self.w = Window2()
        self.w.show()
        self.hide()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec())

