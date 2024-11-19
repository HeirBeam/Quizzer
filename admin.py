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
    """Admin function to add questions to a quiz with input validation."""
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

    while True:
        try:
            quiz_id = int(input("Enter the number of the quiz to add questions to: "))
            if any(quiz[0] == quiz_id for quiz in quizzes):
                break
            else:
                print("Invalid quiz ID. Please select from the list above.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    question = input("Enter the question: ")
    option1 = input("Enter option 1: ")
    option2 = input("Enter option 2: ")
    option3 = input("Enter option 3: ")
    option4 = input("Enter option 4: ")

    while True:
        try:
            correct_option = int(input("Enter the correct option number (1-4): "))
            if correct_option in [1, 2, 3, 4]:
                break
            else:
                print("Invalid input. Please enter a number between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")

    while True:
        difficulty = input("Enter the difficulty level (easy, medium, hard): ").strip().lower()
        if difficulty in ['easy', 'medium', 'hard']:
            break
        else:
            print("Invalid input. Please enter 'easy', 'medium', or 'hard'.")

    cursor.execute('''
    INSERT INTO questions (quiz_id, question, option1, option2, option3, option4, correct_option, difficulty)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', (quiz_id, question, option1, option2, option3, option4, correct_option, difficulty))
    connection.commit()
    print("Question added successfully.")
    connection.close()

