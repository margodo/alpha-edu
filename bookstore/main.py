import sqlite3
# Класс Bookstore
# Этот класс должен содержать методы для:
# Добавления новой книги.
# Удаления книги.
# Обновления данных книги (например, количества, цены, и т. д.).
# Поиска книг по различным критериям (по названию, автору, году и жанру).

class Bookstore:
    def __init__(self, name, location):
        try:
            self.connection = sqlite3.connect(name)
            self.cursor = sqlite3.Connection.cursor()
            print(f"Connection to '{self.name}' was succesful!")
        except sqlite3.Error as error:
            print(f"Error while connecting: {error}")
        self.name = name
        self.location = location
        self.books = []

    def add_book(self, book):
        pass

    def delete(self, book):
        pass

    def update_books(self):
        pass
    
    def search_book(self):
        pass

class Buyer:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def find_book(self, book):
        pass

class Book:

    def __init__(self, title, author, year, genre, price=2000):
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre
        self.price = price