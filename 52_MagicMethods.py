# Magic Methods --> Dunder methods (double underscore) __init__, __str__ , __eq__
#                   They are automatically called by many of python's built-in operations.
#                   They allow developers to define or customize the behavior of objects


class Book:

    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Pages: {self.num_pages}"

    def __eq__(self, other):
        return self.title == other.title and self.author == other.author

    def __lt__(self, other):
        return self.num_pages < other.num_pages

    def __gt__(self, other):
        return self.num_pages > other.num_pages

    def __add__(self, other):
        return self.num_pages + other.num_pages

    def __contains__(self, keyword):
        return keyword in self.title

    def __getitem__(self, key):
        if key == 'title':
            return self.title
        elif key == 'author':
            return self.author
        elif key == 'num_pages':
            return self.num_pages
        else:
            return f"Key '{key}' is not valid"


book1 = Book("Hello World", "____", 576)
book2 = Book("Hello Ji", "----", 1000)
book3 = Book("Chalooo", "*****", 2000)

print(book1)
print(book2 == book3)
print(book1 < book2)
print(book3 > book2)
print(book1 + book2)

print("Hello Ji" in book2)

print(book1['title'])
