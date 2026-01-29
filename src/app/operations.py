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
        print("Closing connection")
        conn.close()

