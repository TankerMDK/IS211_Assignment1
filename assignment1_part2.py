class Book:
    def __init__(self, author="", title=""):
        self.author = author
        self.title = title

    """
    Step 2b: added the instance attribute, author and title for the object.
    """

    def display(self):
        print(f" {self.title}, written by {self.author}")

    """
    Step 2c: the display function prints the title and author of the book.
    """


book1 = Book("J. K. Rowling", "Harry Potter and the Goblet of Fire")
book2 = Book("Walter Scott", "Of Mice and Men")
"""
Step 3: instatiating the book objects.
"""

if __name__ == "__main__":
    book1.display()
    book2.display()
    """
    Step 4: calling the display function on the book objects.
    """