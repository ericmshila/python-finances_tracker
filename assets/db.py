import sqlite3

def init_db():
    try:
        conn = sqlite3.connect("transactions.db")
    except sqlite3.Error as e:
        print(e)
    cursor = conn.cursor()
    # Create Income Database if does not exist
    cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS tbl_expenses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL UNIQUE,
        amount REAL NOT NULL)
    """)
    # Create Income Database if does not exist
    cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS tbl_income (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL UNIQUE,
        amount REAL NOT NULL)
    """)
    conn.commit()
    conn.close()
    print("Database initialized and table created")