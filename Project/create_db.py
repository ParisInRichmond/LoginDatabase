#!/usr/bin/env python3
import sqlite3

# Connect to the SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('users.db')

# Create a cursor object to interact with the database
cursor = conn.cursor()

# Create a table to store user credentials
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
)
''')

# Insert an initial user (username: testuser, password: testpass)
try:
    cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", ('testuser', 'testpass'))
except sqlite3.IntegrityError:
    # If the user already exists, just pass
    pass

# Commit changes and close the connection
conn.commit()
conn.close()


git 