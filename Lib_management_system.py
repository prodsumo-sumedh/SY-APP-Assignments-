class Library:
    def __init__(self):
        self.Books = {}
        self.patrons = {}

    def add_books(self, book):
        self.Books[book.Book_ID] = book
        print(f"{book.Book_name} Book added successfully")

    def Register_patrons(self, patron):
        self.patrons[patron.patron_id] = patron
        print(f"{patron.patron_name} registered successfully")

    def Borrowing_books(self, patron_id, Book_ID):
        patron_id = patron_id.strip()
        Book_ID = Book_ID.strip()

        if patron_id not in self.patrons:
            print(f"\n[Error] Patron ID '{patron_id}' is not registered.")
            return
        
        if Book_ID not in self.Books:
            print(f"\n[Error] Book ID '{Book_ID}' is not available.")
            return

        patron = self.patrons[patron_id]
        book = self.Books[Book_ID]

        if book.is_available:
            book.is_available = False
            patron.Books_borrowed.append(book)
            print(f"\n[Success] '{book.Book_name}' borrowed successfully by {patron.patron_name}")
        else:
            print("\n[Sorry] This book is not available at this moment.")

    def return_books(self, patron_id, Book_ID):
        patron_id = patron_id.strip()
        Book_ID = Book_ID.strip()

        if patron_id not in self.patrons:
            print(f"\n[Error] I cannot find Patron ID: '{patron_id}'")
            return
            
        if Book_ID not in self.Books:
            print(f"\n[Error] I cannot find Book ID: '{Book_ID}'")
            return

        book = self.Books[Book_ID]
        patron = self.patrons[patron_id]

        if book in patron.Books_borrowed:
            book.is_available = True
            patron.Books_borrowed.remove(book)
            print(f"\n[Success] '{book.Book_name}' returned successfully by {patron.patron_name}")
        else:
            print(f"\n[Error] {patron.patron_name} did not borrow '{book.Book_name}'")


class Books:
    def __init__(self, Book_ID, Book_name, Author):
        self.Book_ID = Book_ID
        self.Book_name = Book_name
        self.Author = Author
        self.is_available = True


class patrons:
    def __init__(self, patron_id, patron_name):
        self.patron_id = patron_id
        self.patron_name = patron_name
        self.Books_borrowed = []


def main():
    My_library = Library()
    
    # Pre-loading data
    My_library.add_books(Books("1022", "Atomic Habits", "James Clear"))
    My_library.add_books(Books("1023", "How to Win Friends and Influence People", "Dale Carnegie"))
    My_library.add_books(Books("1024", "The 7 Habits of Highly Effective People", "Stephen R. Covey"))
    My_library.add_books(Books("1025", "The Power of Now", "Eckhart Tolle"))
    My_library.add_books(Books("1026", "Think and Grow Rich", "Napoleon Hill"))
    My_library.add_books(Books("1027", "Can't Hurt me", "David Goggins"))

    My_library.Register_patrons(patrons("ADT25SOCB1367", "Anuj Kumar"))

    while True:
        print("\n=== LIBRARY MANAGEMENT MENU ===")
        print("1. Add a New Book")
        print("2. Register a New Patron")
        print("3. Borrow a Book")
        print("4. Return a Book")
        print("5. Exit")
        
        choice = input("\nEnter your choice (1-5): ")
        
        if choice == '1':
            Book_name = input("Enter book title: ")
            Author = input("Enter book author: ")
            Book_ID = input("Enter book ID: ")
            My_library.add_books(Books(Book_ID, Book_name, Author))

        elif choice == '2':
            patron_name = input("Enter patron name: ")
            patron_id = input("Enter patron ID: ")
            My_library.Register_patrons(patrons(patron_id, patron_name))
            
        elif choice == '3':
            patron_id = input("Enter Patron ID: ")
            Book_ID = input("Enter Book ID to borrow: ")
            My_library.Borrowing_books(patron_id, Book_ID)
            
        elif choice == '4':
            patron_id = input("Enter Patron ID: ")
            Book_ID = input("Enter Book ID to return: ")
            My_library.return_books(patron_id, Book_ID)
            
        elif choice == '5':
            print("\nExiting the Library System. Goodbye!")
            break
            
        else:
            print("\nInvalid choice. Please select a number from 1 to 5.")


if __name__ == "__main__":
    main()