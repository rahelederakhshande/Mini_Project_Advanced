from abc import ABC, abstractmethod
from datetime import datetime


class Person(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def edit_profile(self, new_name, new_age):
        self.name = new_name or self.name
        self.age = new_age or self.name

    @abstractmethod
    def describe_role(self):
        pass


class Librarian(Person):
    librarian_counter = 1

    def __init__(self, name, age):
        super().__init__(name, age)
        self.librarian_id = Librarian.generate_unique_id()
        Librarian.librarian_counter += 1

    @staticmethod
    def generate_unique_id():
        return Librarian.librarian_counter

    def describe_role(self):
        print("I am a librarian.")


class Member(Person):
    member_counter = 1

    def __init__(self, name, age):
        super().__init__(name, age)
        self.member_id = Member.generate_unique_id()
        Member.member_counter += 1
        self.books_borrowed = []

    @staticmethod
    def generate_unique_id():
        return Member.member_counter

    def borrow_book(self, book):
        if book.check_availability():
            self.books_borrowed.append(book)
            book.is_borrowed = True
            print(f"{self.name} has borrowed '{book.title}' in Date time: {datetime.now()}")
        else:
            print(f"Sorry, '{book.title}' is not available for borrowing.")

    def return_book(self, book):
        if book in self.books_borrowed:
            self.books_borrowed.remove(book)
            book.is_borrowed = False
            print(f"{self.name} has returned '{book.title}'.")
        else:
            print(f"{self.name} did not borrow '{book.title}' from the library.")

    def describe_role(self):
        print("I am a library member.")


class Book:
    book_counter = 1

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.date_created_book = datetime.now()
        self.book_id = Book.generate_unique_id()
        Book.book_counter += 1
        self.is_borrowed = False

    @staticmethod
    def generate_unique_id():
        return Book.book_counter

    def check_availability(self):
        return not self.is_borrowed


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.members = []
        self.librarians = []
        self.reservations = []

    def add_book(self, title, author):
        new_book = Book(title, author)
        self.books.append(new_book)
        print(f"Book '{title}' by {author} added to the library.")

    def register_member(self, name, age):
        new_member = Member(name, age)
        self.members.append(new_member)
        print(f"Member {name} registered with ID {new_member.member_id}.")

    def hire_librarian(self, name, age):
        new_librarian = Librarian(name, age)
        self.librarians.append(new_librarian)
        print(f"Librarian {name} hired with ID {new_librarian.librarian_id}.")

    

    def manage_reservation(self, member, book):
        reservation_id = len(self.reservations) + 1
        reservation_date = datetime.now()
        new_reservation = Reservation(reservation_id, member, book, reservation_date)
        self.reservations.append(new_reservation)
        print(f"Reservation created with ID {reservation_id} for {member.name} and '{book.title}' ")
        print(f"{new_reservation.reservation_date}.")


class Reservation:
    reservation_counter = 1

    def __init__(self, member, book, reservation_date):
        self.reservation_id = Reservation.generate_unique_id()
        self.member = member
        self.book = book
        self.reservation_date = reservation_date
        self.status = "Active"

    @classmethod
    def generate_unique_id(cls):
        id_ = 'R' + str(cls.reservation_counter)
        cls.reservation_counter += 1
        return id_

    def cancel_reservation(self):
        self.status = "Cancelled"
        print(f"Reservation {self.reservation_id} for {self.member.name} and '{self.book.title}' cancelled.")


if __name__ == "__main__":
    my_library = Library("My Awesome Library")

    while True:
        print("\n========= Library Management System =========")
        print("1. Add Book")
        print("2. Register Member")
        print("3. Hire Librarian")
        print("4. Borrow Book")
        print("5. Return Book")
        print("6. Manage Reservation")
        print("7. Display Information")
        print("8. Exit")

        choice = input("Enter your choice (1-8): ")

        if choice == "1":
            title = input("Enter the title of the book: ")
            author = input("Enter the author of the book: ")
            my_library.add_book(title, author)

        elif choice == "2":
            name = input("Enter the member's name: ")
            age = int(input("Enter the member's age: "))
            my_library.register_member(name, age)

        elif choice == "3":
            name = input("Enter the librarian's name: ")
            age = int(input("Enter the librarian's age: "))
            my_library.hire_librarian(name, age)

        elif choice == "4":
            member_id = int(input("Enter the member's ID: "))
            book_id = int(input("Enter the book's ID: "))

            member = next((m for m in my_library.members if m.member_id == member_id), None)
            book = next((b for b in my_library.books if b.book_id == book_id), None)

            if member and book:
                member.borrow_book(book)
            else:
                print("Invalid member or book ID.")

        elif choice == "5":
            member_id = int(input("Enter the member's ID: "))
            book_id = int(input("Enter the book's ID: "))
            # member = next((m for m in my_library.members if m.member_id == member_id), None)
            # book = next((b for b in my_library.books if b.book_id == book_id), None)
            member = None
            for m in my_library.members:
                if m.member_id == member_id:
                    member = m

            book = None
            for b in my_library.books:
                if b.book_id == book_id:
                    book = b

            if member and book:
                member.return_book(book)
            else:
                print("Invalid member or book ID.")

        elif choice == "6":
            member_id = int(input("Enter the member's ID: "))
            book_id = int(input("Enter the book's ID: "))
            # member = next((m for m in my_library.members if m.member_id == member_id), None)
            # book = next((b for b in my_library.books if b.book_id == book_id), None)

            member = None
            for m in my_library.members:
                if m.member_id == member_id:
                    member = m

            book = None
            for b in my_library.books:
                if b.book_id == book_id:
                    book = b

            if member and book:
                my_library.manage_reservation(member, book)
            else:
                print("Invalid member or book ID.")

        elif choice == "7":
            print("\n========= Library Information =========")
            print("Available Books:")
            for book in my_library.books:
                print(f"{book.title} by {book.author}")

            print("\nMembers:")
            for member in my_library.members:
                print(f"ID: {member.member_id}, Name: {member.name}, Age: {member.age}")

            print("\nLibrarians:")
            for librarian in my_library.librarians:
                print(f"ID: {librarian.librarian_id}, Name: {librarian.name}, Age: {librarian.age}")

            print("\nReservations:")
            for reservation in my_library.reservations:
                print(f"ID: {reservation.reservation_id}, Member: {reservation.member.name}, "
                    f"Book: {reservation.book.title}, Status: {reservation.status}")

        elif choice == "8":
            print("Exiting the Library Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 8.")

