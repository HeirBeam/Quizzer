import getpass
from db import get_connection

def create_account():
    """Allow users to create a new account."""
    username = input("Enter a username: ")
    password = getpass.getpass("Enter a password: ")
    wants_admin = input("Do you want admin privileges? (yes/no): ").strip().lower() == "yes"

    if wants_admin:
        # Validate existing admin credentials
        print("Admin verification required.")
        admin_username = input("Enter an existing admin's username: ")
        admin_password = getpass.getpass("Enter the admin's password: ")

        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute('''
        SELECT * FROM users WHERE username = ? AND password = ? AND is_admin = 1
        ''', (admin_username, admin_password))
        admin = cursor.fetchone()

        if not admin:
            print("Invalid admin credentials. Cannot grant admin privileges.")
            connection.close()
            return
        connection.close()

    # Proceed with account creation
    connection = get_connection()
    cursor = connection.cursor()
    try:
        cursor.execute('''
        INSERT INTO users (username, password, is_admin) VALUES (?, ?, ?)
        ''', (username, password, int(wants_admin)))
        connection.commit()
        print("Account created successfully!")
    except Exception as e:
        print("Error creating account:", e)
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
