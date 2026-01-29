import sqlite3
from pathlib import Path

DB_PATH = Path("data") / "book_manager.db"

def get_connection() -> sqlite3.Connection:
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    return sqlite3.connect(DB_PATH)

def create_tables() -> None:
    query =  """
    CREATE TABLE IF NOT EXISTS books (
    id integer PRIMARY KEY, 
    title text NOT NULL, 
    author text NOT NULL, 
    year integer NOT NULL,
    rating integer CHECK (rating BETWEEN 1 AND 5)
    );
    """
    conn = get_connection()
    try:
        conn.execute(query)
        conn.commit()
    finally: 
        conn.close()
