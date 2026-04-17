import sys
import re
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QLineEdit, QTextEdit, QPushButton,
    QCheckBox, QRadioButton, QSpinBox, QLabel, QButtonGroup
)


class StringFormatter:
    def __init__(self, text):
        self.text = text

    def remove_short(self, n):
        words = re.split(r"[,\s]+", self.text)
        self.text = " ".join([w for w in words if len(w) >= n])

    def mask_digits(self):
        self.text = re.sub(r"\d", "*", self.text)

    def spaced(self):
        self.text = " ".join(self.text)

    def sort_words(self, mode):
        words = re.split(r"[,\s]+", self.text)

        if mode == "len":
            words.sort(key=len)
        else:
            words.sort()

        self.text = " ".join(words)


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("StringFormatter Demo")

        layout = QVBoxLayout()

        # --- input ---
        self.input = QLineEdit()
        layout.addWidget(QLabel("Введите строку"))
        layout.addWidget(self.input)

        # --- checkbox 1 ---
        self.cb1 = QCheckBox("Удалить слова меньше n = ")
        self.spin = QSpinBox()
        self.spin.setRange(1, 100)

        h1 = QHBoxLayout()
        h1.addWidget(self.cb1)
        h1.addWidget(self.spin)
        layout.addLayout(h1)

        # --- checkbox 2 ---
        self.cb2 = QCheckBox("Заменить цифры на *")
        layout.addWidget(self.cb2)

        # --- checkbox 3 ---
        self.cb3 = QCheckBox("Вставить пробелы между символами")
        layout.addWidget(self.cb3)

        # --- sort ---
        self.cb4 = QCheckBox("Сортировать слова")

        self.radio_len = QRadioButton("По размеру")
        self.radio_lex = QRadioButton("Лексикографически")
        self.radio_len.setChecked(True)

        self.group = QButtonGroup()
        self.group.addButton(self.radio_len)
        self.group.addButton(self.radio_lex)

        layout.addWidget(self.cb4)
        layout.addWidget(self.radio_len)
        layout.addWidget(self.radio_lex)

        # --- button ---
        self.btn = QPushButton("Форматировать")
        self.btn.clicked.connect(self.process)
        layout.addWidget(self.btn)

        # --- result ---
        self.result = QTextEdit()
        layout.addWidget(QLabel("Результат"))
        layout.addWidget(self.result)

        self.setLayout(layout)

    def process(self):
        text = self.input.text()
        sf = StringFormatter(text)

        # 1. сначала работа со словами
        if self.cb1.isChecked():
            sf.remove_short(self.spin.value())

        if self.cb4.isChecked():
            mode = "len" if self.radio_len.isChecked() else "lex"
            sf.sort_words(mode)

        # 2. потом замена цифр
        if self.cb2.isChecked():
            sf.mask_digits()

        # 3. только в самом конце символы
        if self.cb3.isChecked():
            sf.spaced()

        self.result.setText(sf.text)


def run():
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    app.exec_()


if __name__ == "__main__":
    run()