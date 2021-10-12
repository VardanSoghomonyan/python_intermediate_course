class Book:
    def __init__(self, author="Heghinak", title="Stekhcagorcutyun"):
        self.__author = author
        self.__title = title

    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, author):
        if len(author) > 1:
            self.__author = author
        else:
            print("Book author length is 1. Try another name.")

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title):
        if len(title) > 3:
            self.__title = title
        else:
            print("Book title length is less than 4. Try another name.")

    def print_book_info(self):
        print("The book name is: ", self.title, ", that is written by: ", self.author)


book = Book()
book.print_book_info()
book.author = "L"
book.print_book_info()
book.author = "Li"
book.print_book_info()
book.title = "Max"
book.print_book_info()
book.title = "Maxim"
book.print_book_info()
print()

book1 = Book("Garegin Nzhdeh", "Ceghakronutyun")
book1.print_book_info()
print(book1.__dict__)
