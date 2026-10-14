Library_books = []

while True:
    book_title = input("Book title: ").strip()
    book_author = input("Author name: ").strip()

    if book_title == "" or book_author == "":
        print("Book title and author name cannot be empty!")
        continue

    book_info_added = {
        "books_title": book_title,
        "books_author": book_author,
        "availability": True
    }

    Library_books.append(book_info_added)
    print("Book added successfully!")

    more_books = input("Do you want to add more? (yes/no): ").lower()

    if more_books != "yes":
        print("Thank you for adding books!")
        break


while True:
    print("\n----- Library Book Tracker -----")
    print("1. Display all books")
    print("2. Search for a book")
    print("3. Borrow a book")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        if len(Library_books) == 0:
            print("No books available in the library!")

        else:
            for book in Library_books:
                print("\n----- Book Details -----")
                print(f"Book title: {book['books_title']}")
                print(f"Book author: {book['books_author']}")

                if book["availability"] == True:
                    print("Availability: Available")
                else:
                    print("Availability: Borrowed")

    elif choice == "2":
        book_titles = input("Enter book title to search: ").strip()
        found = False

        for book in Library_books:
            if book["books_title"].lower() == book_titles.lower():
                print("\nBook found!")
                print(f"Book title: {book['books_title']}")
                print(f"Book author: {book['books_author']}")

                if book["availability"] == True:
                    print("Availability: Available")
                else:
                    print("Availability: Borrowed")

                found = True

        if found == False:
            print("Book not found in the library!")

    elif choice == "3":
        book_titles = input("Enter book title to borrow: ").strip()
        found = False

        for book in Library_books:
            if book["books_title"].lower() == book_titles.lower():
                found = True

                if book["availability"] == True:
                    book["availability"] = False
                    print("Book borrowed successfully!")
                else:
                    print("Sorry, this book is already borrowed!")

                break

        if found == False:
            print("Book not found in the library!")

    
    elif choice == "4":
        total_books = len(Library_books)
        borrowed_books = 0
        available_books = 0

        for book in Library_books:
            if book["availability"] == False:
                borrowed_books += 1
            else:
                available_books += 1

        print("\n----- Library Summary -----")
        print(f"Total books added: {total_books}")
        print(f"Total books borrowed: {borrowed_books}")
        print(f"Total books available: {available_books}")

        print("\nThank you for visiting! Visit again.")
        break

        break

    else:
        print("Invalid choice! Please enter a number from 1 to 4.")
