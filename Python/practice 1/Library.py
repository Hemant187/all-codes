
class Library:

    def __init__(self, listOfBooks):
        self.books = listOfBooks

    def displayAvailableBooks(self):
        print("Books present in this library are:")
        for book in self.books:
            print(" *"+book)
        
    def borrowBook(self, bookname):
        if bookname in self.books:
            print(f"You have been issued {bookname}. please keep it safe and return it within 30 days")
            self.books.remove(bookname)
            return True
        else:
            print("Sorry, this book is issued to someone else. please wait until the book is returned")
            return False
    def returnBook(self,bookname):
        self.books.append(bookname)
        print("Thanks for retuning this book!")


class Student:
    def requestBook(self):
        self.book = input("Enter the name of the book you want to borrow")
        return self.book
    def returnBook(self):
        self.book = input("Enter the name of the book you want to return")
        return self.book

if __name__ == "__main__":
    centralLibrary = Library(["Algorithms","Django","clrs","artmetic","phthon notes"])
    # centralLibrary.displayAvailableBooks()
    Student=Student()
    while(True):
        welcomeMsg = '''
        ====Welcome to central library====
        Please choose an Option:
        1. List all the books 
        2. Request a book
        3. Add/Return a book
        4. Exit the library
        '''
        print(welcomeMsg)
        a = int(input("Enter a choice: "))
        if a == 1:
            centralLibrary.displayAvailableBooks()
        elif a==2:
            centralLibrary.borrowBook(Student.requestBook())
        elif a==3:
            centralLibrary.returnBook(Student.returnBook())
        elif a==4:
            print("Thanks for chossing central library! Have a great day ahead")
            exit()
        else:
            print("Invalid Choice!")

            
       
