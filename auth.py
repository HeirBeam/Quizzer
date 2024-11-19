import getpass
import sqlite3
from db import get_connection

from db import get_connection

def create_account():
    """Allow users to create a new account with proper input validation."""
    username = input("Enter a username: ")
    password = getpass.getpass("Enter a password: ")

    # Check if this is the first admin account
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT COUNT(*) FROM users WHERE is_admin = 1")
    admin_count = cursor.fetchone()[0]

    if admin_count == 0:
        print("No admin accounts exist. You can create the first admin account without verification.")
        wants_admin = True
    else:
        # Validate admin privileges request
        while True:
            wants_admin = input("Do you want admin privileges? (yes/no): ").strip().lower()
            if wants_admin in ['yes', 'no']:
                wants_admin = wants_admin == 'yes'
                break
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")

        if wants_admin:
            # Validate existing admin credentials
            print("Admin verification required.")
            admin_username = input("Enter an existing admin's username: ")
            admin_password = getpass.getpass("Enter the admin's password: ")

            cursor.execute('''
            SELECT * FROM users WHERE username = ? AND password = ? AND is_admin = 1
            ''', (admin_username, admin_password))
            admin = cursor.fetchone()

            if not admin:
                print("Invalid admin credentials. Cannot grant admin privileges.")
                connection.close()
                return

    # Proceed with account creation
    try:
        cursor.execute('''
        INSERT INTO users (username, password, is_admin) VALUES (?, ?, ?)
        ''', (username, password, int(wants_admin)))
        connection.commit()
        print("Account created successfully!")
    except sqlite3.IntegrityError:
        print("Error: Username already exists. Please choose a different username.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        connection.close()


def login():
    """Allow users to log in."""
    username = input("Enter your username: ")
    password = getpass.getpass("Enter your password: ")

    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute('''
    SELECT * FROM users WHERE username = ? AND password = ?
    ''', (username, password))
    user = cursor.fetchone()
    connection.close()

    if user:
        return {"id": user[0], "username": user[1], "is_admin": bool(user[3])}
    else:
        print("Invalid username or password.")
        return None
