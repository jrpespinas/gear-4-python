class Book:
    author: str
    title: str
    genre: str

    def __init__(self, author: str, title: str, genre: str):
        self.author = author
        self.title = title
        self.genre = genre


class MongoDB:
    def __init__(self, db: dict):
        self.__db = db

    def add(self, data: Book):
        self.__db[data.title] = {data.author, data.genre}

    def list(self) -> list:
        return [key for key in self.__db]


class Library:
    def __init__(self, db: MongoDB):
        self.db = db

    def list_books(self):
        print(f"Displaying books: {self.db.list()}")

    def add_book(self, book: Book) -> str:
        print(f"Adding book: {book.title}")
        self.db.add(book)


def main():
    database = {}
    mongo_database = MongoDB(database)
    library = Library(mongo_database)

    library.add_book(
        Book(
            title="Building a Second Brain",
            author="Tiago Forte",
            genre="productivity",
        )
    )

    library.add_book(
        Book(
            title="Range",
            author="David Epstein",
            genre="self-help",
        )
    )

    library.list_books()


if __name__ == "__main__":
    main()
