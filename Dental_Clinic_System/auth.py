import sqlite3
from database import get_connection


def login():

    username = input("Enter username: ")
    password = input("Enter password: ")

    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT user_id, username, role
            FROM Users
            WHERE username = ? AND password = ?
        """, (username, password))

        user = cursor.fetchone()

        conn.close()

        if user:
            print("Login successful!")
            return user
        else:
            print("Invalid username or password.")
            return None

    except sqlite3.Error as e:
        print("Database error:", e)
        return None


def add_receptionist():

    username = input("Enter receptionist username: ")
    password = input("Enter receptionist password: ")

    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO Users(username, password, role)
            VALUES (?, ?, 'Receptionist')
        """, (username, password))

        conn.commit()
        conn.close()

        print("Receptionist added successfully.")

    except sqlite3.IntegrityError:
        print("Username already exists.")

    except sqlite3.Error as e:
        print("Database error:", e)