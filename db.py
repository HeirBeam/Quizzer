import sqlite3

def get_connection():
    """Create or return a database connection."""
    connection = sqlite3.connect("quiz_app.db")
    return connection

def setup_database():
    """Setup the database schema for a fresh start."""
    connection = get_connection()
    cursor = connection.cursor()

    # Create the `users` table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL,
        is_admin INTEGER DEFAULT 0
    )
    ''')

    # Create the `quizzes` table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS quizzes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL
    )
    ''')

    # Create the `questions` table with a `difficulty` column
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS questions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        quiz_id INTEGER NOT NULL,
        question TEXT NOT NULL,
        option1 TEXT NOT NULL,
        option2 TEXT NOT NULL,
        option3 TEXT NOT NULL,
        option4 TEXT NOT NULL,
        correct_option INTEGER NOT NULL,
        difficulty TEXT CHECK(difficulty IN ('easy', 'medium', 'hard')) DEFAULT 'medium',
        FOREIGN KEY (quiz_id) REFERENCES quizzes (id)
    )
    ''')

    # Create the `scores` table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS scores (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        quiz_id INTEGER NOT NULL,
        score INTEGER NOT NULL,
        FOREIGN KEY (user_id) REFERENCES users (id),
        FOREIGN KEY (quiz_id) REFERENCES quizzes (id)
    )
    ''')

    connection.commit()
    connection.close()
