class Library:

    def __init__(self):
        self.books = {}
        self.patrons = {}

    def add_book(self):
        book_id = input("Enter Book ID: ")
        book_name = input("Enter Book Name: ")
        self.books[book_id] = {"name": book_name, "status": "Available"}
        print("Book Added Successfully")

    def register(self):
        patron_id = input("Enter Patron ID: ")
        patron_name = input("Enter Patron Name: ")
        self.patrons[patron_id] = patron_name
        print("Patron Registered Successfully")

    def borrow(self):
        book_id = input("Enter Book ID: ")
        if book_id in self.books and self.books[book_id]["status"] == "Available":
            self.books[book_id]["status"] = "Borrowed"
            print("Book Borrowed Successfully")
        else:
            print("Book Not Available")

    def return_book(self):
        book_id = input("Enter Book ID: ")
        if book_id in self.books:
            self.books[book_id]["status"] = "Available"
            print("Book Returned Successfully")
        else:
            print("Book Not Found")

    def display(self):
        for book_id, book in self.books.items():
            print(book_id, "-", book["name"], "-", book["status"])

        for patron_id, patron_name in self.patrons.items():
            print(patron_id, "-", patron_name)
lib = Library()
while True:
    print("1. Add Book")
    print("2. Register Patron")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. Display")
    print("6. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        lib.add_book()
    elif choice == "2":
        lib.register()
    elif choice == "3":
        lib.borrow()
    elif choice == "4":
        lib.return_book()
    elif choice == "5":
        lib.display()
    elif choice == "6":
        print("Thank You!")
        break
    else:
        print("Invalid Choice")