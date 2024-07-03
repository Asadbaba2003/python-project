class Book:
    def __init__(self, title, author, price, quantity):
        self.title = title
        self.author = author
        self.price = price
        self.quantity = quantity

    def get_title(self):
        return self.title

    def get_price(self):
        return self.price

    def get_quantity(self):
        return self.quantity

    def set_quantity(self, quantity):
        self.quantity = quantity

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Price: ${self.price}, Quantity: {self.quantity}"


class Bookstore:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def display_books(self):
        print("Books in the Bookstore:")
        for book in self.books:
            print(book)

    def find_book(self, title):
        for book in self.books:
            if book.get_title().lower() == title.lower():
                return book
        return None

    def update_quantity(self):
        search_title = input("Enter the title of the book to update quantity: ").strip()
        found_book = self.find_book(search_title)

        if found_book:
            try:
                new_quantity = int(input("Enter the new quantity: "))
                found_book.set_quantity(new_quantity)
                print("Quantity updated successfully.")
            except ValueError:
                print("Invalid quantity. Please enter a number.")
        else:
            print("Book not found.")


def search_for_book(bookstore):
    search_title = input("Enter the title of the book: ").strip()
    found_book = bookstore.find_book(search_title)

    if found_book:
        print(f"Book found: {found_book}")
    else:
        print("Book not found.")


def main():
    bookstore = Bookstore()

    # Adding books to the bookstore
    book1 = Book("To Kill a Mockingbird", "Harper Lee", 19.99, 50)
    book2 = Book("1984", "George Orwell", 29.99, 30)
    book3 = Book("One Hundred Years of Solitude", "Gabriel García Márquez", 29.99, 30)
    book4 = Book("Pride and Prejudice", "Jane Austen", 29.99, 30)
    book5 = Book("The Great Gatsby", "F. Scott Fitzgerald", 29.99, 30)
    book6 = Book("The Catcher in the Rye", "J.D. Salinger", 29.99, 30)

    bookstore.add_book(book1)
    bookstore.add_book(book2)
    bookstore.add_book(book3)
    bookstore.add_book(book4)
    bookstore.add_book(book5)
    bookstore.add_book(book6)

    while True:
        print("\n1. Display Books")
        print("2. Search for a Book")
        print("3. Update Book Quantity")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            bookstore.display_books()
        elif choice == '2':
            search_for_book(bookstore)
        elif choice == '3':
            bookstore.update_quantity()
        elif choice == '4':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")


if __name__ == "__main__":
    main()
