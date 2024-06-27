#!/usr/bin/env python3

import cgi
import cgitb
import sqlite3

cgitb.enable()

# Print the HTTP headers
print("Content-type: text/html\n")

# Get the form data
form = cgi.FieldStorage()
username = form.getvalue("username")
password = form.getvalue("password")

# Debugging: print form data
print(f"<p>Username: {username}</p>")
print(f"<p>Password: {password}</p>")

if not username or not password:
    print("Please provide both username and password. <a href='../login.html'>Try again</a>")
else:
    # Connect to the SQLite database
    conn = sqlite3.connect('users.db')  # Adjust path if necessary
    cursor = conn.cursor()

    # Debugging: check database file path
    print(f"<p>Database connected: {'../users.db'}</p>")

    # Check if the user exists
    cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
    user = cursor.fetchone()

    # Debugging: print query result
    print(f"<p>User found: {user}</p>")

    conn.close()

    if user:
        # If user exists, redirect to homepage
        print('<meta http-equiv="refresh" content="0; url=../homepage.html" />')
    else:
        # If user does not exist, show error
        print("Invalid username or password. <a href='../login.html'>Try again</a>")
