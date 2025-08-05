class Book:
    def __init__(self, title, author, quantity):
        self.title = title
        self.author = author
        self.quantity = quantity

    def __str__(self):
        return f"'{self.title}' by {self.author} (Quantity: {self.quantity})"

class Inventory:
    def __init__(self):
        self.books = []

    def add_book(self, title, author, quantity):
        # Check if the book already exists
        for book in self.books:
            if book.title == title and book.author == author:
                book.quantity += quantity
                print(f"Updated '{title}' quantity to {book.quantity}")
                return
        # If not, add new book
        new_book = Book(title, author, quantity)
        self.books.append(new_book)
        print(f"Added '{title}' to inventory.")

    def remove_book(self, title, author, quantity):
        for book in self.books:
            if book.title == title and book.author == author:
                if book.quantity >= quantity:
                    book.quantity -= quantity
                    print(f"Removed {quantity} of '{title}'. New quantity: {book.quantity}")
                    if book.quantity == 0:
                        self.books.remove(book)
                        print(f"'{title}' is now out of stock and removed from inventory.")
                else:
                    print(f"Not enough quantity to remove. Current quantity: {book.quantity}")
                return
        print(f"Book '{title}' by {author} not found in inventory.")

    def search_book(self, title):
        found_books = [book for book in self.books if title.lower() in book.title.lower()]
        if found_books:
            print("Search results:")
            for book in found_books:
                print(book)
        else:
            print(f"No books found with title containing '{title}'.")

    def display_inventory(self):
        if not self.books:
            print("Inventory is empty.")
        else:
            print("Current inventory:")
            for book in self.books:
                print(book)

inventory = Inventory()
inventory.add_book("The Great Gatsby", "F. Scott Fitzgerald", 3)
inventory.add_book("To Kill a Mockingbird", "Harper Lee", 2)
inventory.display_inventory()
inventory.search_book("great")
inventory.remove_book("The Great Gatsby", "F. Scott Fitzgerald", 1)
inventory.display_inventory()