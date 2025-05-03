# -*- coding: utf-8 -*-
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem, QTableWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit, QTextEdit
from sorubankasi_ui import Ui_MainWindow
from sorubankasi1_ui import Ui_MainWindow as Ui_AddQuestionWindow
from Ui_soruekle2 import Ui_SoruEkleme
import sys
import json
import os
from PyQt5.QtPrintSupport import QPrinter, QPrintDialog
from PyQt5.QtGui import QTextDocument

class AddQuestionWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_AddQuestionWindow()
        self.ui.setupUi(self)
        self.parent = parent

        # Buton bağlantısı
        self.ui.pushButton.clicked.connect(self.add_question)

        # Radyo butonlarını grupla
        self.answer_options = [
            self.ui.radioButton,
            self.ui.radioButton_2,
            self.ui.radioButton_3,
            self.ui.radioButton_4,
            self.ui.radioButton_5
        ]

    def add_question(self):
        # Soru metnini al
        question_text = self.ui.textEdit.toPlainText().strip()

        # Yanıt seçeneklerini al
        answers = [
            self.ui.lineEdit.text().strip(),
            self.ui.lineEdit_2.text().strip(),
            self.ui.lineEdit_3.text().strip(),
            self.ui.lineEdit_4.text().strip(),
            self.ui.lineEdit_5.text().strip()
        ]

        # Doğru cevabı kontrol et
        correct_answer = None
        for i, radio in enumerate(self.answer_options):
            if radio.isChecked():
                correct_answer = i
                break

        # Validasyon
        if not question_text:
            QMessageBox.warning(self, "Uyarı", "Soru metni boş olamaz!")
            return

        if not any(answers):
            QMessageBox.warning(self, "Uyarı", "En az bir cevap seçeneği girilmelidir!")
            return

        if correct_answer is None:
            QMessageBox.warning(self, "Uyarı", "Doğru cevap seçilmelidir!")
            return

        # Yeni soru oluştur
        new_question = {
            "question": question_text,
            "answers": answers,
            "correct": correct_answer
        }

        # Ana pencereye soruyu ekle
        if self.parent:
            self.parent.add_question_to_bank(new_question)

        # Önizleme alanına ekle
        preview_text = f"Soru: {question_text}\n"
        for i, answer in enumerate(answers):
            prefix = "✓" if i == correct_answer else " "
            preview_text += f"{prefix} {i+1}. {answer}\n"

        self.ui.textEdit_2.append(preview_text + "\n")

        # Formu temizle
        self.ui.textEdit.clear()
        self.ui.lineEdit.clear()
        self.ui.lineEdit_2.clear()
        self.ui.lineEdit_3.clear()
        self.ui.lineEdit_4.clear()
        self.ui.lineEdit_5.clear()
        for radio in self.answer_options:
            radio.setChecked(False)

class SoruListelemeWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_SoruEkleme()
        self.ui.setupUi(self)
        self.parent = parent

        # QTableWidget'ın size policy'sini ayarla
        self.ui.tableQuestions.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)

        # Layout'un stretch'ini ayarla (isteğe bağlı)
        self.ui.verticalLayout.setStretch(0, 1)

        # Yazdır butonu bağlantısı
        self.ui.pushButton.clicked.connect(self.print_selected_question)  # Düzeltildi!

        # Soru bankasını yükle ve tabloyu güncelle
        self.load_questions()

    def load_questions(self):
        if self.parent and hasattr(self.parent, 'questions'):
            self.questions = self.parent.questions
            self.update_table()

    def update_table(self):
        self.ui.tableQuestions.setRowCount(len(self.questions))

        for row, question in enumerate(self.questions):
            self.ui.tableQuestions.setItem(row, 0, QtWidgets.QTableWidgetItem(question["question"]))

            for col in range(5):
                answer = question["answers"][col] if col < len(question["answers"]) else ""
                item = QtWidgets.QTableWidgetItem(answer)

                # Doğru cevabı işaretle
                if col == question["correct"]:
                    item.setBackground(QtGui.QColor(200, 255, 200))

                self.ui.tableQuestions.setItem(row, col + 1, item)

    def print_selected_question(self):
        selected_row = self.ui.tableQuestions.currentRow()
        if selected_row >= 0:
            question_data = self.questions[selected_row]
            question_text = question_data["question"]
            answers = question_data["answers"]
            correct_answer_index = question_data["correct"]

            text_to_print = f"Soru: {question_text}\n\n"
            for i, answer in enumerate(answers):
                prefix = "✓ " if i == correct_answer_index else "  "
                text_to_print += f"{prefix}{chr(65 + i)}. {answer}\n"  # A, B, C...

            printer = QPrinter(QPrinter.HighResolution)
            dialog = QPrintDialog(printer, self)
            if dialog.exec_() == QPrintDialog.Accepted:
                document = QTextDocument()
                document.setPlainText(text_to_print)
                document.print_(printer)
        else:
            QMessageBox.warning(self, "Uyarı", "Lütfen yazdırmak için bir soru seçin.")


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.questions = []
        self.load_questions()

        # Buton bağlantıları
        self.ui.pushButton.clicked.connect(self.open_add_question_window)
        self.ui.pushButton_2.clicked.connect(self.open_show_questions_window)

    def load_questions(self):
        # JSON dosyasından soruları yükle
        if os.path.exists("sorubankasi.json"):
            try:
                with open("sorubankasi.json", "r", encoding="utf-8") as f:
                    self.questions = json.load(f)
            except:
                self.questions = []

    def save_questions(self):
        # Soruları JSON dosyasına kaydet
        with open("sorubankasi.json", "w", encoding="utf-8") as f:
            json.dump(self.questions, f, ensure_ascii=False, indent=2)

    def add_question_to_bank(self, question):
        self.questions.append(question)
        self.save_questions()

    def open_add_question_window(self):
        self.add_window = AddQuestionWindow(self)
        self.add_window.show()

    def open_show_questions_window(self):
        self.show_window = SoruListelemeWindow(self)
        self.show_window.show()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())