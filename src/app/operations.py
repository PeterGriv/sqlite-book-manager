from db import get_connection

def add_book(
        title: str,
        author: str, 
        year: int,
        rating: int) -> None:
    query = """
    INSERT INTO books (title, author, year, rating)
    VALUES (?, ?, ?, ?);
        """
    conn = get_connection()
    try:
        conn.execute(query, (title, author, year, rating))
        conn.commit()
    except Exception as e:
        print(f"Problem with inserting book: {e}")
    finally:
        conn.close()


def get_all_books(): 
    query = """
    SELECT id, title, author, year, rating 
    FROM books;"""
    conn = get_connection()
    try:
        rows = conn.execute(query).fetchall()
        return rows
    except Exception as e:
        print(f"Problem with getting all books: {e}")
    finally: 
        conn.close()


def get_book_by_id(book_id: int): 
    query = """
    SELECT id, title, author, year, rating 
    FROM books
    WHERE id = ?;"""
    
    conn = get_connection()
    try:
        row = conn.execute(query, (book_id,)).fetchone()
        return row
    except Exception as e:
        print(f"Problem with getting book: {e}")
    finally: 
        conn.close()


def delete_book_by_id(book_id: int): 
    query = """
    DELETE
    FROM books
    WHERE id = ?;"""
    
    conn = get_connection()
    try:
        conn.execute(query, (book_id,))
        conn.commit()
    except Exception as e:
        print(f"Problem with deleting book: {e}")
    finally: 
        conn.close()


def update_book_by_id(book_id: int, rating: int) -> None: 
    query = """
    UPDATE books 
    SET rating = ?
    WHERE id = ?;"""
    
    conn = get_connection()
    try:
        conn.execute(query, (rating, book_id))
        conn.commit()
    except Exception as e:
        print(f"Problem with updating book: {e}")
    finally: 
        conn.close()