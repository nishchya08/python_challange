# Magic methods = dunder methods ( double underscore) __init__, __str__, __repr__, __len__, __getitem__, __setitem__, __delitem__, __iter__, __next__, __contains__, __call__, __eq__, __lt__, __gt__, __le__, __ge__, __add__, __sub__, __mul__, __truediv__, __floordiv__, __mod__, __pow__, __and__, __or__, __xor__, __invert__, __enter__, __exit__
# These are automatically called by many of the python's built in operations
# They allow developers to define or customize the behaviour of objects

class Book:
    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages

    def __str__(self):
        return f"'{self.title}' by {self.author}"
    
    def __eq__(self, other):
        return self.title == other.title and self.author == other.author
    
    def __lt__(self, other):
        return self.num_pages < other.num_pages
    
    def __add__(self, other):
        return f"{self.num_pages + other.num_pages} pages"
    
    def __contains__(self, keyword):
        return keyword in self.title or keyword in self.author
    
    def __getitem__(self, key):
        if key == 'title':
            return self.title
        if key == 'author':
            return self.author
        if key == 'num_pages':
            return self.num_pages
        else:
            return f"{key} was not found"
        
    
book1 = Book("1984", "George Orwell", 328)
book2 = Book("To Kill a Mockingbird", "Harper Lee", 281)
book3 = Book("Shoe Dog", "Phil Knight", 384)

#print(book3)
#print( book1 == book2)
#print( book1 > book2)
#print( book1 + book2)
#print("1984" in book1)
#print(book1['title'])
#print(book2['author'])  # Accessing the author using the __getitem__ method
#print(book2['num_pages'])  # Accessing the number of pages using the __getitem__ method
print(book1['audio'])