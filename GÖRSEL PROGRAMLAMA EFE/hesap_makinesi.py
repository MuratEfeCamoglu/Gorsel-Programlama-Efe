from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

class HesapMakinesi(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hesap Makinesi")
        self.setGeometry(100, 100, 360, 500)
        self.setFixedSize(360, 500)
        self.arayuz()

    def arayuz(self):
        # Sonuç ekranı
        self.ekran = QLineEdit(self)
        self.ekran.setGeometry(10, 10, 340, 50)
        self.ekran.setAlignment(Qt.AlignRight)
        self.ekran.setReadOnly(True)
        font = QFont('Arial', 20)
        self.ekran.setFont(font)

        # Butonlar için pozisyonlar
        butonlar = {
            'C': (10, 70), 'CE': (100, 70), '<-': (190, 70), '/': (280, 70),
            '7': (10, 140), '8': (100, 140), '9': (190, 140), '*': (280, 140),
            '4': (10, 210), '5': (100, 210), '6': (190, 210), '-': (280, 210),
            '1': (10, 280), '2': (100, 280), '3': (190, 280), '+': (280, 280),
            '±': (10, 350), '0': (100, 350), '.': (190, 350), '=': (280, 350)
        }

        # Butonları oluştur
        for buton_text, pos in butonlar.items():
            buton = QPushButton(buton_text, self)
            buton.setGeometry(pos[0], pos[1], 80, 50)
            buton.clicked.connect(self.buton_tikla)
            if buton_text in ['=', '+', '-', '*', '/']:
                buton.setStyleSheet('background-color: orange;')

    def buton_tikla(self):
        buton = self.sender()
        mevcut_text = self.ekran.text()

        if buton.text() == '=':
            try:
                sonuc = eval(mevcut_text)
                self.ekran.setText(str(sonuc))
            except:
                self.ekran.setText('Hata')
        elif buton.text() == 'C':
            self.ekran.clear()
        elif buton.text() == 'CE':
            self.ekran.clear()
        elif buton.text() == '<-':
            self.ekran.setText(mevcut_text[:-1])
        elif buton.text() == '±':
            try:
                sayi = float(mevcut_text)
                self.ekran.setText(str(-sayi))
            except:
                pass
        else:
            self.ekran.setText(mevcut_text + buton.text())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    hesap_makinesi = HesapMakinesi()
    hesap_makinesi.show()
    sys.exit(app.exec_()) 