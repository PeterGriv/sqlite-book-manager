from db import create_tables
from operations import add_book, get_all_books, get_book_by_id, delete_book_by_id, update_book_by_id

def main():
    create_tables()
    print("Table was created!")
    add_book("Dirty Glory", "Pete Greig", 2019, 3)
    add_book("Amerikáni", "Tomáš Hudák", 2025, 4)
    book = get_book_by_id(2)
    if book:
        print("")
        print(f"id: {book[0]}")
        print(f"title: {book[1]}")
        print(f"author: {book[2]}")
        print(f"year: {book[3]}")
        print(f"rating: {book[4]}")
        print("")
    else: 
        print(f"Book not found") 
    print(update_book_by_id(2, 1))
    print(get_all_books())


if __name__ == "__main__":
    main()