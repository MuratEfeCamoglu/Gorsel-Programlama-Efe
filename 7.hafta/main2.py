import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(504, 394)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(10, 10, 480, 360))
        self.textEdit.setObjectName("textEdit")
        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 504, 26))
        self.menubar.setObjectName("menubar")
        self.menuYeni = QtWidgets.QMenu(self.menubar)
        self.menuYeni.setObjectName("menuYeni")
        self.menuA = QtWidgets.QMenu(self.menubar)
        self.menuA.setObjectName("menuA")
        self.menuKapat = QtWidgets.QMenu(self.menubar)
        self.menuKapat.setObjectName("menuKapat")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)

        # Actions
        self.actionKes = QtWidgets.QAction(MainWindow)
        self.actionKopyala = QtWidgets.QAction(MainWindow)
        self.actionYap_t_r = QtWidgets.QAction(MainWindow)
        self.actionKal_n = QtWidgets.QAction(MainWindow)
        self.action_talik = QtWidgets.QAction(MainWindow)
        self.actionAlt_izili = QtWidgets.QAction(MainWindow)
        self.actionYeni = QtWidgets.QAction(MainWindow)
        self.actionA = QtWidgets.QAction(MainWindow)
        self.actionKaydet = QtWidgets.QAction(MainWindow)

        self.menuYeni.addAction(self.actionYeni)
        self.menuYeni.addAction(self.actionA)
        self.menuYeni.addAction(self.actionKaydet)
        self.menubar.addAction(self.menuYeni.menuAction())
        self.menubar.addAction(self.menuA.menuAction())
        self.menubar.addAction(self.menuKapat.menuAction())

        self.toolBar.addAction(self.actionKes)
        self.toolBar.addAction(self.actionKopyala)
        self.toolBar.addAction(self.actionYap_t_r)
        self.toolBar.addAction(self.actionKal_n)
        self.toolBar.addAction(self.action_talik)
        self.toolBar.addAction(self.actionAlt_izili)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Not Defteri"))
        self.menuYeni.setTitle(_translate("MainWindow", "Dosya"))
        self.menuA.setTitle(_translate("MainWindow", "Düzen"))
        self.menuKapat.setTitle(_translate("MainWindow", "Çıkış"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "Araç Çubuğu"))

        self.actionKes.setText(_translate("MainWindow", "Kes"))
        self.actionKopyala.setText(_translate("MainWindow", "Kopyala"))
        self.actionYap_t_r.setText(_translate("MainWindow", "Yapıştır"))
        self.actionKal_n.setText(_translate("MainWindow", "Kalın"))
        self.action_talik.setText(_translate("MainWindow", "İtalik"))
        self.actionAlt_izili.setText(_translate("MainWindow", "Altı Çizili"))
        self.actionYeni.setText(_translate("MainWindow", "Yeni"))
        self.actionA.setText(_translate("MainWindow", "Aç"))
        self.actionKaydet.setText(_translate("MainWindow", "Kaydet"))


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Event bağlantıları
        self.ui.actionYeni.triggered.connect(self.new_file)
        self.ui.actionA.triggered.connect(self.open_file)
        self.ui.actionKaydet.triggered.connect(self.save_file)

        self.ui.actionKes.triggered.connect(self.cut_text)
        self.ui.actionKopyala.triggered.connect(self.copy_text)
        self.ui.actionYap_t_r.triggered.connect(self.paste_text)

        self.ui.actionKal_n.triggered.connect(self.bold_text)
        self.ui.action_talik.triggered.connect(self.italic_text)
        self.ui.actionAlt_izili.triggered.connect(self.underline_text)

    # Fonksiyonlar
    def new_file(self):
        self.ui.textEdit.clear()

    def open_file(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Dosya Aç", "", "Text Files (*.txt)")
        if filename:
            with open(filename, 'r', encoding='utf-8') as file:
                self.ui.textEdit.setPlainText(file.read())

    def save_file(self):
        filename, _ = QFileDialog.getSaveFileName(self, "Dosya Kaydet", "", "Text Files (*.txt)")
        if filename:
            with open(filename, 'w', encoding='utf-8') as file:
                file.write(self.ui.textEdit.toPlainText())

    def cut_text(self):
        self.ui.textEdit.cut()

    def copy_text(self):
        self.ui.textEdit.copy()

    def paste_text(self):
        self.ui.textEdit.paste()

    def bold_text(self):
        fmt = self.ui.textEdit.currentCharFormat()
        fmt.setFontWeight(QtGui.QFont.Bold if fmt.fontWeight() != QtGui.QFont.Bold else QtGui.QFont.Normal)
        self.ui.textEdit.setCurrentCharFormat(fmt)

    def italic_text(self):
        fmt = self.ui.textEdit.currentCharFormat()
        fmt.setFontItalic(not fmt.fontItalic())
        self.ui.textEdit.setCurrentCharFormat(fmt)

    def underline_text(self):
        fmt = self.ui.textEdit.currentCharFormat()
        fmt.setFontUnderline(not fmt.fontUnderline())
        self.ui.textEdit.setCurrentCharFormat(fmt)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
