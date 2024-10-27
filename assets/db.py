import sqlite3

def init_db():
    try:
        conn = sqlite3.connect("expenses.db")
    except sqlite3.Error as e:
        print(e)
    cursor = conn.cursor()
    cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS tbl_expenses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        amount REAL NOT NULL)
    """)
    conn.commit()
    conn.close()
    print("Database initialized and table created")