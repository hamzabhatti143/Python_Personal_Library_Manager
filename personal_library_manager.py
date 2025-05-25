import sys
import inquirer

books = []
def addbook():
    book_title = input("Enter the book title: ")
    author = input("Enter the author: ")
    publication_year = input("Enter the publication year: ")
    genre = input("Enter the genre: ")
    read_this_book = input("Have you read this book? (yes/no): ")
    print("Book added successfully!")

    return {
        "Title": book_title.lower(),
        "Author": author.lower(),
        "Year": publication_year,
        "Genre": genre.lower(),
        "Read": read_this_book.lower() == "yes"
    }

def remove_book():
    title = input("Enter the title of the book to remove: ")

    for book in books:
        if book['Title'] == title.lower():
            print(f"Enter the title of the book to remove: {title}")
            books.remove(book)
            print(f"Book {title} removed successfully")
            return
        print("This Book is not in this list")

def search_book():
    select = [
        inquirer.List(
            'option',
            message= "Search by:",
            choices=["Title", "Author"]
        )
    ]
    users_need = inquirer.prompt(select)
    if users_need['option'] == "Title":
        title = input("Enter Book Title: ")
        for book in books:
            if book['Title'] == title.lower():
                print("Book Found: ")
                print(book)
                return
            print("Book not found")


    elif users_need['option'] == "Author":
        author = input("Enter the Author name: ")
        for book in books:
            if book['Author'] == author.lower():
                print("Author Found: ")
                print(book)
                return
            print("Author not Found")


def display_book():
    if books:
        print("Your Library:\n")
        for book in books:
            print("-", book)

    else:
        print("Book Not Found!")


def display_statics():
    print(f"Total books: {len(books)}\n")

def book_add_to_library():
    book = addbook()
    books.append(book)


while True:
    library = [
        inquirer.List(
            'option',
            message= "Welcome to your Personal Library Manager!",
            choices=["1. Add a Book", "2. Remove a book", "3. Search for a book", "4. Display all books", "5. Display statistics", "6. Exit"]
        )
    ]
    
    user_choices = inquirer.prompt(library)
    selected = user_choices['option']
    
    match selected:
        case "1. Add a Book":
            book_add_to_library()
            
        case "2. Remove a book":
            remove_book()
            
        case "3. Search for a book":
            search_book()
            
        case "4. Display all books":
            display_book()
            
        case "5. Display statistics":
            display_statics()
            
        case "6. Exit":
            print("Library saved to file. Goodbye!")
            sys.exit()