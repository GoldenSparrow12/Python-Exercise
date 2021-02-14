"""It is program that manage the library common operation
like, display book,lend book, add book, return book"""


class Library:

    def __init__(self, lst, lib_name):
        self.dict_book = {}
        self.lst_book = lst
        self.lib_name = lib_name

    def display(self):
        """fun which display all book in library"""
        print(f"We have following books in library: {self.lib_name}")
        for book in self.lst_book:
            print(book)

    def lend(self, book_name, user_name):
        """fun are use to lend the book from library"""
        if book_name in self.lst_book:
            if book_name not in self.dict_book.keys():
                self.dict_book.update({book_name: user_name})
                print("You Lend the book..")
            else:
                print(f"Book is already lend by {self.dict_book[book_name]}")
        else:
            print("Please enter the book from the list")

    def add(self, book_name):
        """fun are add the book to the library"""
        if book_name in self.lst_book:
            print(f"We have already a {book_name} book")
        else:
            self.lst_book.append(book_name)
            print("Book has been added to the library!!")

    def returnn(self, book_name):
        """for return the book fun are use"""
        if book_name in self.dict_book.keys():
            self.dict_book.pop(book_name)
            print("Book Return Successful")
        else:
            print("Please enter the correct book")


if __name__ == '__main__':
    books = ["C", "C++", "PYTHON", "JAVA", "PHP"]
    golden = Library(books, "Golden Sparrow")

    while True:
        try:
            print(f'''\tWelcome to library: {golden.lib_name} 
        Choose one of them 
            1.Display Book
            2.Lend Book
            3.Add Book
            4.Return Book
            5.Exit''')
            chose = int(input())

            if chose == 1:
                golden.display()
            elif chose == 2:
                b_n = input("Enter the book name which you want to lend:").upper()
                name = input("Enter your name:")
                golden.lend(b_n, name)
            elif chose == 3:
                book_add = input("Enter Book Name for Add to the library:").upper()
                golden.add(book_add)
            elif chose == 4:
                book_return = input("Enter Book Name for return to the library:").upper()
                golden.returnn(book_return)
            elif chose == 5:
                exit()
        except ValueError:
            print("Please Enter valid option!!!")
