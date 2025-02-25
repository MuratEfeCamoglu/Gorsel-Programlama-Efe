import sys
from PyQt5 import QtWidgets
from panel import Ui_Dialog  # panel.py dosyanı import ediyoruz

class ResumeApp(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)  # UI'yi başlat

        # Butonları bağlama
        self.ui.buttonBox.accepted.connect(self.save_resume)  # "OK" butonu ile kayıt işlemi
        self.ui.buttonBox.rejected.connect(self.close)  # "Cancel" butonu pencereyi kapatır

    def save_resume(self):
        """ Kullanıcının girdiği verileri al ve göster """
        first_name = self.ui.Bugra.text()
        last_name = self.ui.lineEdit.text()
        age_range = self.ui.comboBox.currentText()
        
        # Seçili programlama dillerini al
        languages = []
        if self.ui.checkBox.isChecked():
            languages.append("C#")
        if self.ui.checkBox_2.isChecked():
            languages.append("Java")
        if self.ui.checkBox_3.isChecked():
            languages.append("Python")
        if self.ui.checkBox_4.isChecked():
            languages.append("C")
        
        languages_text = ", ".join(languages) if languages else "Yok"

        # Bilgileri ekrana mesaj olarak göster
        message = (
            f"İsim: {first_name}\n"
            f"Soyisim: {last_name}\n"
            f"Yaş Aralığı: {age_range}\n"
            f"Bildiği Diller: {languages_text}"
        )
        QtWidgets.QMessageBox.information(self, "Özgeçmiş Kaydı", message)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = ResumeApp()
    window.show()
    sys.exit(app.exec_())
