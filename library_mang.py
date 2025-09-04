from abc import ABC, abstractmethod

class LibraryItem(ABC):
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._available = True  # Encapsulation

    def is_available(self):
        return self._available

    def set_availability(self, status):
        self._available = status

    @abstractmethod
    def borrow(self):
        pass

    @abstractmethod
    def return_item(self):
        pass

    def display_info(self):
        status = "Available" if self._available else "Not Available"
        print(f"{self.title} by {self.author} [{status}]")


class Book(LibraryItem):
    def borrow(self):
        if self._available:
            self._available = False
            print(f"'{self.title}' borrowed successfully.")
        else:
            print(f"'{self.title}' is already borrowed.")

    def return_item(self):
        self._available = True
        print(f"'{self.title}' returned.")


class Magazine(LibraryItem):
    def borrow(self):
        if self._available:
            self._available = False
            print(f"'{self.title}' borrowed successfully.")
        else:
            print(f"'{self.title}' is already borrowed.")

    def return_item(self):
        self._available = True
        print(f"'{self.title}' returned.")


def main():
    book1 = Book("Python Basics", "John Doe")
    mag1 = Magazine("Tech Monthly", "Jane Smith")

    for item in (book1, mag1):
        item.display_info()
        item.borrow()
        item.display_info()
        item.return_item()
        print()

if __name__ == "__main__":
    main()
