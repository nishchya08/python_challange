# Aggregator = Represent a relationship where one object (the whole)
#                contain references to one or more INDEPENDENT objects (the parts)

class Library:
    def __init__(self,name):
        self.name = name
        self.books = []

    def add_book(self,book):
        self.books.append(book)

    def list_books(self):
        return[f"{book.title} by {book.author}" for book in self.books]

class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author

library = Library("New York public Library")
book1 = Book("Harry Poter...", "J.k, Rowling")
book2 = Book("The shoe dog...", "Phil Knight")
book3 = Book("The color of magic...", "Terry pratchet")

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

print(library.name)

for book in library.list_books():
    print(book)