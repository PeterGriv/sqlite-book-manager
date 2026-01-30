# SQLite Book Manager

Simple Python application for managing a small book collection using an **SQLite database**.

This project demonstrates:
- basic SQL operations (CRUD)
- working with SQLite in Python
- separation of concerns (database, operations, main logic)
- clean and readable procedural code
- basic error handling

---

## Features

- Create a local SQLite database
- Add new books
- List all books
- Retrieve a book by ID
- Update book rating
- Delete a book by ID

---

## Requirements

- Python 3.9+
- No external dependencies (uses Python standard library only)

---

## Setup

Clone the repository and navigate to the project directory.

The database file is created automatically when the application runs.

---

## Usage

Run the main application:

```bash
python main.py
``` 
Example operations performed in the application:
	•	creating the database table
	•	inserting sample books
	•	querying all books
	•	updating book rating
	•	deleting a book


## Database schema 

```sql
CREATE TABLE books (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    year INTEGER NOT NULL,
    rating INTEGER CHECK (rating BETWEEN 1 AND 5)
);
```

## Project structure 

.
├── main.py          # Application entry point
├── db.py            # Database connection and table creation
├── operations.py    # CRUD operations
└── data/            # SQLite database file (ignored by git)


## Notes

	•	The database file is stored locally and excluded from version control.
	•	This project focuses on clarity and correctness rather than user interface.
	•	All database operations are executed using parameterized queries.