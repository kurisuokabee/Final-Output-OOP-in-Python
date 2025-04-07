class Author:
    def __init__(self, name):
        self.name = name
     
    def __str__(self):
        return f"{self.name}"

class Book:
    def __init__(self, title, author: Author, year):
        self.title = title
        self.author = author  # Composition: Book HAS-A Author
        self.year = year

    def display_info(self):
        print(f"'{self.title}' by {self.author} - Published in {self.year}")

# Create an Author object
author = Author("Gabrielle Zevin")

# Create a Book object with the Author object inside
book = Book("Tomorrow, and Tomorrow, and Tomorrow", author, 2022)

# Display Book info
book.display_info()
