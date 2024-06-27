#!/usr/bin/env python3
import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('users.db')

# Create a cursor object to interact with the database
cursor = conn.cursor()

# Query to select the initial user
cursor.execute("SELECT * FROM users WHERE username = ?", ('testuser',))

# Fetch the user
user = cursor.fetchone()

conn.close()

# Print the user details
if user:
    print(f"User found: ID={user[0]}, Username={user[1]}, Password={user[2]}")
else:
    print("User not found.")
