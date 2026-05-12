import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, 
    QPushButton, QListWidget, QHBoxLayout, QInputDialog
)
from sqlalchemy import (
    create_engine, Column, Integer, String, ForeignKey, func
)
from sqlalchemy.orm import sessionmaker, relationship, declarative_base

Base = declarative_base()

# ---------------- MODELS ----------------
class Author(Base):
    __tablename__ = "authors"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    country = Column(String)
    born = Column(Integer)
    died = Column(Integer)
    books = relationship("Book", back_populates="author")


class Book(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    pages = Column(Integer)
    author_id = Column(Integer, ForeignKey("authors.id"))
    author = relationship("Author", back_populates="books")


# ---------------- DATABASE ----------------
engine = create_engine("sqlite:///library_sqlalchemy.db")
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# ---------------- GUI ----------------
class LibraryGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Библиотека SQLAlchemy")
        self.resize(600, 500)

        layout = QVBoxLayout()

        btn_add_author = QPushButton("Добавить автора")
        btn_add_author.clicked.connect(self.add_author)

        btn_add_book = QPushButton("Добавить книгу")
        btn_add_book.clicked.connect(self.add_book)

        layout.addWidget(btn_add_author)
        layout.addWidget(btn_add_book)

        layout.addWidget(QLabel("Фильтры:"))

        btn_filter_birth = QPushButton("Авторы, родившиеся между X и Y")
        btn_filter_birth.clicked.connect(self.filter_birth)

        btn_filter_russia = QPushButton("Книги авторов из России")
        btn_filter_russia.clicked.connect(self.filter_russia)

        btn_filter_pages = QPushButton("Книги с страниц > N")
        btn_filter_pages.clicked.connect(self.filter_pages)

        btn_filter_books_count = QPushButton("Авторы с книгами > N")
        btn_filter_books_count.clicked.connect(self.filter_books_count)

        layout.addWidget(btn_filter_birth)
        layout.addWidget(btn_filter_russia)
        layout.addWidget(btn_filter_pages)
        layout.addWidget(btn_filter_books_count)

        # --- Списки для вывода ---
        layout.addWidget(QLabel("Результаты:"))
        self.result_list = QListWidget()
        layout.addWidget(self.result_list)

        self.setLayout(layout)

    # ---------------- ADD AUTHOR ----------------
    def add_author(self):
        name, ok = QInputDialog.getText(self, "Автор", "Имя")
        if not ok or not name:
            return
        country, ok = QInputDialog.getText(self, "Автор", "Страна")
        if not ok: country = ""
        born, ok = QInputDialog.getInt(self, "Автор", "Год рождения", 1900)
        if not ok: born = 1900
        died, ok = QInputDialog.getInt(self, "Автор", "Год смерти", 2000)
        if not ok: died = 2000

        author = Author(name=name, country=country, born=born, died=died)
        session.add(author)
        session.commit()
        self.result_list.addItem(f"Добавлен автор: {name}")

    # ---------------- ADD BOOK ----------------
    def add_book(self):
        authors = session.query(Author).all()
        if not authors:
            self.result_list.addItem("Нет авторов, сначала добавьте автора!")
            return
        author_names = [a.name for a in authors]
        author_index, ok = QInputDialog.getItem(
            self, "Книга", "Выберите автора", author_names, 0, False
        )
        if not ok: return
        author = authors[author_names.index(author_index)]

        title, ok = QInputDialog.getText(self, "Книга", "Название")
        if not ok or not title: return
        pages, ok = QInputDialog.getInt(self, "Книга", "Количество страниц", 100)
        if not ok: pages = 100

        book = Book(title=title, pages=pages, author=author)
        session.add(book)
        session.commit()
        self.result_list.addItem(f"Добавлена книга: {title} ({author.name})")

    # ---------------- FILTERS ----------------
    def filter_birth(self):
        x, ok1 = QInputDialog.getInt(self, "Фильтр", "X (год рождения)")
        y, ok2 = QInputDialog.getInt(self, "Фильтр", "Y (год рождения)")
        if not (ok1 and ok2): return
        authors = session.query(Author).filter(Author.born >= x, Author.born <= y).all()
        self.result_list.clear()
        for a in authors:
            self.result_list.addItem(f"{a.name} ({a.born}-{a.died})")

    def filter_russia(self):
        books = session.query(Book).join(Author).filter(Author.country=="Russia").all()
        self.result_list.clear()
        for b in books:
            self.result_list.addItem(f"{b.title} - {b.author.name}")

    def filter_pages(self):
        n, ok = QInputDialog.getInt(self, "Фильтр", "N (кол-во страниц)")
        if not ok: return
        books = session.query(Book).filter(Book.pages > n).all()
        self.result_list.clear()
        for b in books:
            self.result_list.addItem(f"{b.title} ({b.pages} стр.) - {b.author.name}")

    def filter_books_count(self):
        n, ok = QInputDialog.getInt(self, "Фильтр", "N (мин. кол-во книг)")
        if not ok: return
        authors = session.query(Author).all()
        self.result_list.clear()
        for a in authors:
            if len(a.books) > n:
                self.result_list.addItem(f"{a.name} - {len(a.books)} книг")


# ---------------- MAIN ----------------
def run():
    app = QApplication(sys.argv)
    window = LibraryGUI()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    run()
