from sqlite3 import connect

conn = connect("database.db")
cursor = conn.cursor()

cursor.executescript(
    """
    PRAGMA foreign_keys = ON;

    CREATE TABLE IF NOT EXISTS users (
        username TEXT PRIMARY KEY,
        password TEXT(128) NOT NULL,
        balance DECIMAL(10, 2) DEFAULT 0.00,
        login_attempts INTEGER DEFAULT 0,
        login_lockout TEXT
    );

    CREATE TABLE IF NOT EXISTS transactions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        amount DECIMAL(10, 2) NOT NULL,
        type TEXT NOT NULL,
        timestamp TEXT DEFAULT (datetime('now', 'localtime')),
        FOREIGN KEY (username) REFERENCES users (username)
    );
    """
)


conn.commit()
conn.close()
