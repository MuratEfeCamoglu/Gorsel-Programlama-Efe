# main.py
from PyQt5 import QtWidgets
import sys

from login_ui import Ui_MainWindow as LoginUI  # İlk arayüz (login ekranı)
from soru_ui import Ui_MainWindow as SoruEkleUI  # İkinci arayüz (soru ekleme)

class SoruEkleWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = SoruEkleUI()
        self.ui.setupUi(self)

class LoginWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = LoginUI()
        self.ui.setupUi(self)

        # Butona tıklanınca ikinci pencereyi aç
        self.ui.pushButton.clicked.connect(self.show_soru_ekle)

    def show_soru_ekle(self):
        self.soru_ekle_window = SoruEkleWindow()
        self.soru_ekle_window.show()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    login = LoginWindow()
    login.show()
    sys.exit(app.exec_())
