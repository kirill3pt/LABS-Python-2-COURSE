import sys
import hashlib
import json
import xml.etree.ElementTree as ET
from bson import ObjectId
from pymongo import MongoClient
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QLineEdit,
    QLabel, QMessageBox, QListWidget, QFileDialog, QInputDialog, QComboBox
)

# ---------------- DATABASE ----------------
client = MongoClient("mongodb://localhost:27017/")
db = client["library_db"]
users_col = db["users"]
authors_col = db["authors"]
books_col = db["books"]

def init_db():
    # проверка администратора
    if users_col.count_documents({"login": "admin"}) == 0:
        password = hashlib.md5("123".encode()).hexdigest()
        users_col.insert_one({"login": "admin", "password": password})

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
        password = hashlib.md5(self.password.text().encode()).hexdigest()
        user = users_col.find_one({"login": login, "password": password})
        if user:
            self.main = MainWindow()
            self.main.show()
            self.close()
        else:
            QMessageBox.warning(self, "Ошибка", "Неверный логин или пароль")

# ---------------- MAIN WINDOW ----------------
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Библиотека")
        layout = QVBoxLayout()

        self.authors = QListWidget()
        self.books = QListWidget()

        # кнопки
        btn_add_author = QPushButton("Добавить автора")
        btn_add_author.clicked.connect(self.add_author)
        btn_add_book = QPushButton("Добавить книгу")
        btn_add_book.clicked.connect(self.add_book)
        btn_delete_author = QPushButton("Удалить автора")
        btn_delete_author.clicked.connect(self.delete_author)
        btn_delete_book = QPushButton("Удалить книгу")
        btn_delete_book.clicked.connect(self.delete_book)
        btn_export = QPushButton("Экспорт автора")
        btn_export.clicked.connect(self.export_author)
        btn_import = QPushButton("Импорт автора")
        btn_import.clicked.connect(self.import_author)
        btn_queries = QPushButton("Выполнить запросы")
        btn_queries.clicked.connect(self.run_queries)

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
        layout.addWidget(btn_queries)

        self.setLayout(layout)
        self.load_data()

    # ---------------- LOAD DATA ----------------
    def load_data(self):
        self.authors.clear()
        self.books.clear()
        for a in authors_col.find():
            self.authors.addItem(f"{a['_id']} | {a['name']} | {a['country']}")
        for b in books_col.find():
            author = authors_col.find_one({"_id": b["author_id"]})
            self.books.addItem(f"{b['_id']} | {b['title']} | {b['pages']} стр. | Автор: {author['name']}")

    # ---------------- ADD AUTHOR ----------------
    def add_author(self):
        dialog = QWidget()
        dialog.setWindowTitle("Добавить автора")
        layout = QVBoxLayout()

        name_input = QLineEdit()
        country_input = QLineEdit()
        born_input = QLineEdit()
        died_input = QLineEdit()
        save_btn = QPushButton("Сохранить")

        layout.addWidget(QLabel("Имя"))
        layout.addWidget(name_input)
        layout.addWidget(QLabel("Страна"))
        layout.addWidget(country_input)
        layout.addWidget(QLabel("Год рождения"))
        layout.addWidget(born_input)
        layout.addWidget(QLabel("Год смерти"))
        layout.addWidget(died_input)
        layout.addWidget(save_btn)
        dialog.setLayout(layout)

        def save():
            authors_col.insert_one({
                "name": name_input.text(),
                "country": country_input.text(),
                "born": int(born_input.text()),
                "died": int(died_input.text())
            })
            dialog.close()
            self.load_data()

        save_btn.clicked.connect(save)
        dialog.show()
        self.dialog = dialog

    # ---------------- ADD BOOK ----------------
    def add_book(self):
        dialog = QWidget()
        dialog.setWindowTitle("Добавить книгу")
        layout = QVBoxLayout()
        combo = QComboBox()
        authors = list(authors_col.find())
        for a in authors:
            combo.addItem(a["name"])
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
            author_id = authors[combo.currentIndex()]["_id"]
            books_col.insert_one({
                "author_id": author_id,
                "title": title_input.text(),
                "pages": int(pages_input.text()),
                "publisher": publisher_input.text(),
                "year": int(year_input.text())
            })
            dialog.close()
            self.load_data()

        save_btn.clicked.connect(save)
        dialog.show()
        self.dialog = dialog

    # ---------------- DELETE ----------------
    def delete_author(self):
        item = self.authors.currentItem()
        if not item:
            return
        author_id = ObjectId(item.text().split("|")[0].strip())
        books_col.delete_many({"author_id": author_id})
        authors_col.delete_one({"_id": author_id})
        self.load_data()

    def delete_book(self):
        item = self.books.currentItem()
        if not item:
            return
        book_id = ObjectId(item.text().split("|")[0].strip())
        books_col.delete_one({"_id": book_id})
        self.load_data()

    # ---------------- EXPORT / IMPORT ----------------
    def export_author(self):
        item = self.authors.currentItem()
        if not item:
            return
        author_id = ObjectId(item.text().split("|")[0].strip())
        author = authors_col.find_one({"_id": author_id})
        path, _ = QFileDialog.getSaveFileName(self, "Сохранить", "", "JSON (*.json);;XML (*.xml)")
        if not path:
            return
        if path.endswith(".json"):
            data = {"name": author["name"], "country": author["country"], "years": [author["born"], author["died"]]}
            with open(path, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=4)
        elif path.endswith(".xml"):
            root = ET.Element("author")
            ET.SubElement(root, "name").text = author["name"]
            ET.SubElement(root, "country").text = author["country"]
            years = ET.SubElement(root, "years")
            years.set("born", str(author["born"]))
            years.set("died", str(author["died"]))
            tree = ET.ElementTree(root)
            tree.write(path, encoding="utf-8")

    def import_author(self):
        path, _ = QFileDialog.getOpenFileName(self, "Открыть", "", "JSON (*.json);;XML (*.xml)")
        if not path:
            return
        if path.endswith(".json"):
            with open(path, "r", encoding="utf-8") as f:
                data = json.load(f)
            authors_col.insert_one({"name": data["name"], "country": data["country"],
                                    "born": int(data["years"][0]), "died": int(data["years"][1])})
        else:
            tree = ET.parse(path)
            root = tree.getroot()
            name = root.find("name").text
            country = root.find("country").text
            years = root.find("years")
            authors_col.insert_one({"name": name, "country": country,
                                    "born": int(years.get("born")), "died": int(years.get("died"))})
        self.load_data()

    # ---------------- QUERIES ----------------
    def run_queries(self):
        print("\n--- Авторы между X и Y ---")
        X, Y = 1800, 1900
        for a in authors_col.find({"born": {"$gte": X, "$lte": Y}}):
            print(a["name"], a["born"])

        print("\n--- Книги авторов из России ---")
        russian_ids = [a["_id"] for a in authors_col.find({"country": "Russia"})]
        for b in books_col.find({"author_id": {"$in": russian_ids}}):
            print(b["title"])

        print("\n--- Книги с страницами > N ---")
        N = 500
        for b in books_col.find({"pages": {"$gt": N}}):
            print(b["title"], b["pages"])

        print("\n--- Авторы с количеством книг > N ---")
        N = 1
        pipeline = [{"$group": {"_id": "$author_id", "count": {"$sum": 1}}}, {"$match": {"count": {"$gt": N}}}]
        for result in books_col.aggregate(pipeline):
            author = authors_col.find_one({"_id": result["_id"]})
            print(author["name"], result["count"])

# ---------------- MAIN ----------------
def run():
    init_db()
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    app.exec_()

if __name__ == "__main__":
    run()
