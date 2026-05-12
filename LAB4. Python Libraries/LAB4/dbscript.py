import sys
import sqlite3
import hashlib
import json
import xml.etree.ElementTree as ET

from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton,
    QLineEdit, QLabel, QMessageBox, QListWidget,
    QFileDialog, QInputDialog, QComboBox
)

DB = "library.db"


# ---------------- DATABASE ----------------

def init_db():
    conn = sqlite3.connect(DB)
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS users(
        login TEXT,
        password TEXT
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS authors(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        country TEXT,
        born INTEGER,
        died INTEGER
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS books(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        author_id INTEGER,
        title TEXT,
        pages INTEGER,
        publisher TEXT,
        year INTEGER
    )
    """)

    password = hashlib.md5("123".encode()).hexdigest()

    cur.execute("SELECT * FROM users WHERE login='admin'")

    if not cur.fetchone():
        cur.execute(
            "INSERT INTO users VALUES(?, ?)",
            ("admin", password)
        )

    conn.commit()
    conn.close()


# ---------------- LOGIN ----------------

class LoginWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Авторизация")

        layout = QVBoxLayout()

        self.login = QLineEdit()
        self.password = QLineEdit()
        self.password.setEchoMode(QLineEdit.Password)

        btn = QPushButton("Войти")
        btn.clicked.connect(self.check_login)

        layout.addWidget(QLabel("Логин"))
        layout.addWidget(self.login)

        layout.addWidget(QLabel("Пароль"))
        layout.addWidget(self.password)

        layout.addWidget(btn)

        self.setLayout(layout)

    def check_login(self):

        login = self.login.text()

        password = hashlib.md5(
            self.password.text().encode()
        ).hexdigest()

        conn = sqlite3.connect(DB)
        cur = conn.cursor()

        cur.execute(
            "SELECT * FROM users WHERE login=? AND password=?",
            (login, password)
        )

        user = cur.fetchone()

        conn.close()

        if user:
            self.main = MainWindow()
            self.main.show()
            self.close()
        else:
            QMessageBox.warning(
                self,
                "Ошибка",
                "Неверный логин или пароль"
            )


# ---------------- MAIN WINDOW ----------------

class MainWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Библиотека")

        layout = QVBoxLayout()

        self.authors = QListWidget()
        self.books = QListWidget()

        btn_add_author = QPushButton("Добавить автора")
        btn_add_author.clicked.connect(self.add_author)

        btn_add_book = QPushButton("Добавить книгу")
        btn_add_book.clicked.connect(self.add_book)

        btn_export = QPushButton("Экспорт автора")
        btn_export.clicked.connect(self.export_author)

        btn_import = QPushButton("Импорт автора")
        btn_import.clicked.connect(self.import_author)

        btn_delete_author = QPushButton("Удалить автора")
        btn_delete_author.clicked.connect(self.delete_author)

        btn_delete_book = QPushButton("Удалить книгу")
        btn_delete_book.clicked.connect(self.delete_book)

        layout.addWidget(QLabel("Авторы"))
        layout.addWidget(self.authors)

        layout.addWidget(QLabel("Книги"))
        layout.addWidget(self.books)

        layout.addWidget(btn_add_author)
        layout.addWidget(btn_add_book)

        layout.addWidget(btn_delete_author)
        layout.addWidget(btn_delete_book)

        layout.addWidget(btn_export)
        layout.addWidget(btn_import)

        self.setLayout(layout)

        self.load_data()

    # ---------------- LOAD ----------------

    def load_data(self):

        self.authors.clear()
        self.books.clear()

        conn = sqlite3.connect(DB)
        cur = conn.cursor()

        for row in cur.execute("SELECT * FROM authors"):

            self.authors.addItem(
                f"{row[0]} | {row[1]} | {row[2]}"
            )

        for row in cur.execute("SELECT * FROM books"):

            self.books.addItem(
                f"{row[0]} | {row[2]} | {row[3]} стр."
            )

        conn.close()

    # ---------------- ADD AUTHOR ----------------

    def add_author(self):

        name, ok = QInputDialog.getText(
            self,
            "Автор",
            "Имя"
        )

        if not ok:
            return

        country, _ = QInputDialog.getText(
            self,
            "Автор",
            "Страна"
        )

        born, _ = QInputDialog.getInt(
            self,
            "Автор",
            "Год рождения"
        )

        died, _ = QInputDialog.getInt(
            self,
            "Автор",
            "Год смерти"
        )

        conn = sqlite3.connect(DB)
        cur = conn.cursor()

        cur.execute(
            """
            INSERT INTO authors(name,country,born,died)
            VALUES(?,?,?,?)
            """,
            (name, country, born, died)
        )

        conn.commit()
        conn.close()

        self.load_data()

    # ---------------- ADD BOOK ----------------

    def add_book(self):

        dialog = QWidget()
        dialog.setWindowTitle("Добавить книгу")

        layout = QVBoxLayout()

        combo = QComboBox()

        conn = sqlite3.connect(DB)
        cur = conn.cursor()

        authors = []

        for row in cur.execute("SELECT id, name FROM authors"):

            combo.addItem(row[1])
            authors.append(row)

        conn.close()

        title_input = QLineEdit()
        pages_input = QLineEdit()
        publisher_input = QLineEdit()
        year_input = QLineEdit()

        save_btn = QPushButton("Сохранить")

        layout.addWidget(QLabel("Автор"))
        layout.addWidget(combo)

        layout.addWidget(QLabel("Название"))
        layout.addWidget(title_input)

        layout.addWidget(QLabel("Страницы"))
        layout.addWidget(pages_input)

        layout.addWidget(QLabel("Издательство"))
        layout.addWidget(publisher_input)

        layout.addWidget(QLabel("Год"))
        layout.addWidget(year_input)

        layout.addWidget(save_btn)

        dialog.setLayout(layout)

        def save():

            index = combo.currentIndex()
            author_id = authors[index][0]

            conn = sqlite3.connect(DB)
            cur = conn.cursor()

            cur.execute("""
            INSERT INTO books(author_id,title,pages,publisher,year)
            VALUES(?,?,?,?,?)
            """, (
                author_id,
                title_input.text(),
                pages_input.text(),
                publisher_input.text(),
                year_input.text()
            ))

            conn.commit()
            conn.close()

            dialog.close()

            self.load_data()

        save_btn.clicked.connect(save)

        dialog.show()

        self.dialog = dialog

    # ---------------- DELETE AUTHOR ----------------

    def delete_author(self):

        item = self.authors.currentItem()

        if not item:
            return

        author_id = item.text().split("|")[0].strip()

        conn = sqlite3.connect(DB)
        cur = conn.cursor()

        cur.execute(
            "DELETE FROM books WHERE author_id=?",
            (author_id,)
        )

        cur.execute(
            "DELETE FROM authors WHERE id=?",
            (author_id,)
        )

        conn.commit()
        conn.close()

        self.load_data()

    # ---------------- DELETE BOOK ----------------

    def delete_book(self):

        item = self.books.currentItem()

        if not item:
            return

        book_id = item.text().split("|")[0].strip()

        conn = sqlite3.connect(DB)
        cur = conn.cursor()

        cur.execute(
            "DELETE FROM books WHERE id=?",
            (book_id,)
        )

        conn.commit()
        conn.close()

        self.load_data()

    # ---------------- EXPORT ----------------

    def export_author(self):

        item = self.authors.currentItem()

        if not item:
            return

        author_id = item.text().split("|")[0].strip()

        conn = sqlite3.connect(DB)
        cur = conn.cursor()

        cur.execute(
            "SELECT * FROM authors WHERE id=?",
            (author_id,)
        )

        row = cur.fetchone()

        conn.close()

        path, _ = QFileDialog.getSaveFileName(
            self,
            "Сохранить",
            "",
            "JSON (*.json);;XML (*.xml)"
        )

        if not path:
            return

        if path.endswith(".json"):

            data = {
                "name": row[1],
                "country": row[2],
                "years": [row[3], row[4]]
            }

            with open(path, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=4)

        elif path.endswith(".xml"):

            root = ET.Element("author")

            ET.SubElement(root, "name").text = row[1]
            ET.SubElement(root, "country").text = row[2]

            years = ET.SubElement(root, "years")

            years.set("born", str(row[3]))
            years.set("died", str(row[4]))

            tree = ET.ElementTree(root)

            tree.write(path, encoding="utf-8")

    # ---------------- IMPORT ----------------

    def import_author(self):

        path, _ = QFileDialog.getOpenFileName(
            self,
            "Открыть",
            "",
            "JSON (*.json);;XML (*.xml)"
        )

        if not path:
            return

        if path.endswith(".json"):

            with open(path, "r", encoding="utf-8") as f:
                data = json.load(f)

            name = data["name"]
            country = data["country"]

            born = data["years"][0]
            died = data["years"][1]

        else:

            tree = ET.parse(path)
            root = tree.getroot()

            name = root.find("name").text
            country = root.find("country").text

            years = root.find("years")

            born = years.get("born")
            died = years.get("died")

        conn = sqlite3.connect(DB)
        cur = conn.cursor()

        cur.execute("""
        INSERT INTO authors(name,country,born,died)
        VALUES(?,?,?,?)
        """, (
            name,
            country,
            born,
            died
        ))

        conn.commit()
        conn.close()

        self.load_data()


# ---------------- MAIN ----------------

def run():

    init_db()

    app = QApplication(sys.argv)

    window = LoginWindow()
    window.show()

    app.exec_()


if __name__ == "__main__":
    run()