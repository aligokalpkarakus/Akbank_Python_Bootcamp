class Library:

    def __init__(self):

        self.file = open("books.txt", "a+")

    def __del__(self):

        self.file.close()

    def list_books(self):
        self.file.seek(0)
        list_lines = self.file.read().splitlines()
        for element in list_lines:
            print("book name: " + element.split()[0].strip(",") + " " + "author: " + element.split()[1].strip(","))

    def add_book(self):

        book_name = input("Enter the name of the book: ")
        book_author = input("Enter the name of the author: ")
        book_year = input("Enter the year the book was published: ")
        book_page = input("Enter the number of pages: ")
        line = book_name + ", " + book_author + ", " + book_year + ", " + book_page + "\n"
        self.file.write(line)

    def remove_book(self):
        book_to_be_deleted = input("Enter the name of the book: ")
        self.file.seek(0)
        list_lines = self.file.read().splitlines()
        for element in list_lines:
            if element.split()[0].strip(",") == book_to_be_deleted:
                index = list_lines.index(element)
                list_lines.remove(list_lines[index])

        with open("books.txt", "w") as file:
            for element2 in list_lines:
                self.file.write(element2 + "\n")


lib = Library()


def display_menu():
    print("*** MENU***")
    print("1) List Books")
    print("2) Add Book")
    print("3) Remove Book")
    print("4) Quit")


while True:

    display_menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        lib.list_books()
    elif choice == "2":
        lib.add_book()
    elif choice == "3":
        lib.remove_book()
    elif choice == "4":
        print("Exiting the program.")
        break
    else:
        print("Please enter a valid option.")









