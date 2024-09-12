class Books:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True
    
    def borrow(self):
        if self.available:
            self.available = False
        else:
            print(f"Lo siento, el libro {self.title} no esta disponible en estos momentos")

    def returnBook(self):
        if not self.available:
            self.available = True
        else:
            print(f"El libro {self.title} ya esta disponible")

        
class student:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.borrowedBooks = []
    
    def borrowBooks(self, book):
        if book.available:
            book.borrow()
            self.borrowedBooks.append(book)
            print(f'El libro {book.title} ha sido prestado')
        else:
            print(f'En estos momentos el libro {book.title} no esta disponible')

    def returnBooks(self, book):
        if book in self.borrowedBooks:
            book.returnBook()
            self.borrowedBooks.remove(book)
        else:
            print(f'El libro {book.title} no esta/ha sido prestado')
        
class Library:
    def __init__(self):
        self.books = []
        self.students = []

    def addBook(self, book):
        self.books.append(book)
        print(f'El libro {book.title}, ha sido agregado')

    def registerStudent(self, student):
        self.students.append(student)
        print(f'El usuario {student.name} ha sido registrado.')

    def showAvailablesBooks(self):
        print(f"Libros disponibles: ")
        for book in self.books:
            if book.available:
                print(f"Title: {book.title}, Author: {book.author}")


book1 = Books('Minecraft', 'Notch')
book2 = Books('Roblox', 'Roblox')
book3 = Books('Fortnite', 'Epic Games')
library = Library()
library.addBook(book1)
library.addBook(book2)
library.addBook(book3)


student1 = student('Calvin', 2325)
student2 = student('Javier', 1234)
student3 = student('Tito', 1998)


library.registerStudent(student1)
library.registerStudent(student2)
library.registerStudent(student3)

student1.borrowBooks(book1)

library.showAvailablesBooks()