from db import get_connection

def add_quiz():
    """Admin function to add a new quiz."""
    quiz_name = input("Enter the name of the quiz: ")
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute('''
    INSERT INTO quizzes (name) VALUES (?)
    ''', (quiz_name,))
    connection.commit()
    print("Quiz added successfully.")
    connection.close()

def add_question():
    """Admin function to add questions to a quiz."""
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM quizzes")
    quizzes = cursor.fetchall()

    if not quizzes:
        print("No quizzes are available. Please add a quiz first.")
        connection.close()
        return

    print("Available Quizzes:")
    for quiz in quizzes:
        print(f"{quiz[0]}. {quiz[1]}")

    quiz_id = int(input("Enter the number of the quiz to add questions to: "))
    question = input("Enter the question: ")
    option1 = input("Enter option 1: ")
    option2 = input("Enter option 2: ")
    option3 = input("Enter option 3: ")
    option4 = input("Enter option 4: ")
    correct_option = int(input("Enter the correct option number (1-4): "))

    cursor.execute('''
    INSERT INTO questions (quiz_id, question, option1, option2, option3, option4, correct_option)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (quiz_id, question, option1, option2, option3, option4, correct_option))
    connection.commit()
    print("Question added successfully.")
    connection.close()