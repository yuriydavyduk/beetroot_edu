from datetime import date


class Author:
    def __init__(self, name, country, birthday):
        self.name = name
        self.country = country
        self.birthday = birthday
        self.books = []

    def __repr__(self):
        return f'"{self.name}" from "{self.country}" born on "{self.birthday}" have "{len(self.books)}" books'

    def __str__(self):
        return f'"{self.name}" from "{self.country}" born on "{self.birthday}" have "{len(self.books)}" books'


class Book:
    count = 0

    def __init__(self, name, year, author: Author):
        self.name = name
        self.year = year
        self.author = author
        Book.count += 1

    def __repr__(self):
        return f'{self.name}, year: {self.year}, author: {self.author.name}'

    def __str__(self):
        return f'{self.name}, year: {self.year}, author: {self.author.name}'


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.authors = []

    def __repr__(self):
        return f'Library: {self.name} - {len(self.books)} books and {len(self.authors)} authors'

    def __str__(self):
        return f'Library: {self.name} - {len(self.books)} books and {len(self.authors)} authors'

    def new_book(self, name: str, year: int, author: Author):
        book = Book(name, year, author)

        self.books.append(book)
        author.books.append(book)

        if author not in self.authors:
            self.authors.append(author)

        return book

    def group_by_author(self, author: Author):
        author_books = []
        for book in self.books:
            if book.author == author:
                author_books.append(book)

        return author_books

    def group_by_year(self, year: int):
        year_books = []
        for book in self.books:
            if book.year == year:
                year_books.append(book)

        return year_books


library = Library('Abetka')

Tsepova = Author('Tsepova', 'Ukraine', date(1980, 5, 6))
Shevchenko = Author('Taras Shevchenko', 'Ukraine', date(1814, 3, 9))

abc = library.new_book('ABC book', 2002, Tsepova)
kobzar = library.new_book('Kobzar', 2002, Shevchenko)
haydamaki = library.new_book('Haydamaki', 2020, Shevchenko)

print(Shevchenko)
print(kobzar)
print(library.group_by_author(Shevchenko))
print(library.group_by_year(2020))
print(Book.count)
