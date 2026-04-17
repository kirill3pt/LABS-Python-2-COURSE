class Book:
    _counter = 1

    def __init__(self, author, title):
        if not title:
            raise ValueError("Название книги не может быть пустым")

        self.author = author
        self.title = title
        self.code = Book._counter
        Book._counter += 1

    def __str__(self):
        parts = self.author.split()
        short_author = f"{parts[0][0]}.{parts[1]}" if len(parts) > 1 else self.author
        return f"[{self.code}] {short_author} '{self.title}'"

    def tag(self):
        words = self.title.split()
        return [w for w in words if w[0].isupper()]


class Library:
    def __init__(self, number, address):
        self.number = number
        self.address = address
        self.books = []

    def __iadd__(self, book):
        self.books.append(book)
        return self

    def __iter__(self):
        return iter(self.books)


# --- функция для меню ---
def run():
    number = int(input("Номер библиотеки: "))
    address = input("Адрес: ")

    lib = Library(number, address)

    while True:
        print("\n1 - добавить книгу")
        print("2 - показать книги")
        print("0 - выход")

        choice = input("Выбор: ")

        if choice == "1":
            author = input("Автор: ")
            title = input("Название: ")

            try:
                lib += Book(author, title)
            except ValueError as e:
                print("Ошибка:", e)

        elif choice == "2":
            for book in lib:
                print("print(book):")
                print(book)
                print("print(book.tag()):")
                print(book.tag())

        elif choice == "0":
            break