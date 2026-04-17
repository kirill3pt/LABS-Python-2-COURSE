import sys
import re
import os
from datetime import datetime
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QListWidget, QFileDialog,
    QMessageBox, QAction, QStatusBar, QLabel
)

LOG_FILE = "script18.log"
PATTERN = r"\(\d{3}\)\d{7}|\(\d{3}\)\d{3}-\d{2}-\d{2}"


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Скрипт 18. Искатель строк")
        self.resize(700, 500)

        self.list_widget = QListWidget()
        self.setCentralWidget(self.list_widget)

        # --- статус-бар ---
        self.status = QStatusBar()
        self.setStatusBar(self.status)

        self.status_left = QLabel("Готово")
        self.status_right = QLabel("")

        self.status.addWidget(self.status_left, 3)  
        self.status.addWidget(self.status_right, 2) 

        self.init_menu()

        # проверка лога
        if not os.path.exists(LOG_FILE):
            QMessageBox.information(
                self,
                "Информация",
                "Файл лога не найден. Файл будет создан автоматически"
            )

    def init_menu(self):
        menubar = self.menuBar()

        # --- Файл ---
        file_menu = menubar.addMenu("Файл")

        open_action = QAction("Открыть...", self)
        open_action.triggered.connect(self.open_file)
        file_menu.addAction(open_action)

        # --- Лог ---
        log_menu = menubar.addMenu("Лог")

        export_action = QAction("Экспорт...", self)
        export_action.triggered.connect(self.export)
        log_menu.addAction(export_action)

        add_log_action = QAction("Добавить в лог", self)
        add_log_action.triggered.connect(self.add_to_log)
        log_menu.addAction(add_log_action)

        view_log_action = QAction("Просмотр", self)
        view_log_action.triggered.connect(self.view_log)
        log_menu.addAction(view_log_action)

    # --- функции ---

    def format_size(self, size):
        return f"{size:,}".replace(",", " ") + " байт"

    def open_file(self):
        path, _ = QFileDialog.getOpenFileName(self, "Открыть файл", "", "Text (*.txt);;All (*)")
        if not path:
            return

        with open(path, "r", encoding="utf-8", errors="ignore") as f:
            lines = f.readlines()

        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        for line_number, line in enumerate(lines, start=1):
            for match in re.finditer(PATTERN, line):
                p = match.group()
                position = match.start() + 1

                self.list_widget.addItem(
                    f"Строка: {line_number}, позиция: {position}, найдено: {p}"
                )

        size = os.path.getsize(path)
        self.status_left.setText(f"Обработан файл {path}")
        self.status_right.setText(self.format_size(size))

    def export(self):
        path, _ = QFileDialog.getSaveFileName(self, "Экспорт", "", "Text (*.txt)")
        if not path:
            return

        with open(path, "w", encoding="utf-8") as f:
            for i in range(self.list_widget.count()):
                f.write(self.list_widget.item(i).text() + "\n")

    def add_to_log(self):
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            for i in range(self.list_widget.count()):
                f.write(self.list_widget.item(i).text() + "\n")

    def view_log(self):
        reply = QMessageBox.question(
            self,
            "Подтверждение",
            "Вы действительно хотите открыть лог? Данные последних поисков будут потеряны!",
            QMessageBox.Yes | QMessageBox.No
        )

        if reply == QMessageBox.No:
            return

        self.list_widget.clear()

        if os.path.exists(LOG_FILE):
            with open(LOG_FILE, "r", encoding="utf-8") as f:
                for line in f:
                    self.list_widget.addItem(line.strip())

        self.status_left.setText("Открыт лог")
        self.status_right.setText("")

def app():
    import sys
    from PyQt5.QtWidgets import QApplication

    app = QApplication.instance()
    if app is None:
        app = QApplication(sys.argv)

    window = MainWindow()
    window.show()
    app.exec_()