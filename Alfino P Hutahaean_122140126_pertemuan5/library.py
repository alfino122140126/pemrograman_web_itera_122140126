from abc import ABC, abstractmethod

# Abstract class
class LibraryItem(ABC):
    def __init__(self, item_id, title, year):
        self._id = item_id             # Protected attribute
        self._title = title            # Protected attribute
        self._year = year              # Protected attribute

    @abstractmethod
    def display_info(self):
        pass

    @property
    def title(self):  # Encapsulation with property
        return self._title

    @property
    def id(self):
        return self._id


# Subclass 1: Book
class Book(LibraryItem):
    def __init__(self, item_id, title, year, author):
        super().__init__(item_id, title, year)
        self._author = author

    def display_info(self):  # Polymorphism: override method
        print(f"[BOOK] ID: {self._id} | Title: {self._title} | Author: {self._author} | Year: {self._year}")


# Subclass 2: Magazine
class Magazine(LibraryItem):
    def __init__(self, item_id, title, year, issue):
        super().__init__(item_id, title, year)
        self._issue = issue

    def display_info(self):  # Polymorphism: override method
        print(f"[MAGAZINE] ID: {self._id} | Title: {self._title} | Issue: {self._issue} | Year: {self._year}")


# Class Library untuk menyimpan koleksi
class Library:
    def __init__(self):
        self.__items = []  # Private attribute

    def add_item(self, item):
        self.__items.append(item)

    def show_items(self):
        if not self.__items:
            print("Perpustakaan kosong.")
        else:
            for item in self.__items:
                item.display_info()

    def search_by_title(self, title):
        results = [item for item in self.__items if item.title.lower() == title.lower()]
        return results

    def search_by_id(self, item_id):
        for item in self.__items:
            if item.id == item_id:
                return item
        return None


# Contoh penggunaan sistem
if __name__ == "__main__":
    library = Library()

    # Tambah item
    book1 = Book("IF220", "Python OOP", 2022, "Alfino")
    book2 = Book("IF221", "Algoritma", 2022, "Suori")
    magazine1 = Magazine("MT22", "Tekno Monthly", 2023, "April")

    library.add_item(book1)
    library.add_item(book2)
    library.add_item(magazine1)

    print("=== Daftar Koleksi Perpustakaan ===")
    library.show_items()

    print("\n=== Cari Judul: 'Python OOP' ===")
    for result in library.search_by_title("Python OOP"):
        result.display_info()

    print("\n=== Cari ID: 'IF220' ===")
    item = library.search_by_id("IG220")
    if item:
        item.display_info()
    else:
        print("Item tidak ditemukan.")
