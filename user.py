from db import get_connection

def take_quiz(user_id):
    """Allow users to take a quiz with proper input validation."""
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM quizzes")
    quizzes = cursor.fetchall()

    if not quizzes:
        print("No quizzes are available at the moment. Please check back later.")
        connection.close()
        return

    print("Available Quizzes:")
    for quiz in quizzes:
        print(f"{quiz[0]}. {quiz[1]}")

    while True:
        try:
            quiz_id = int(input("Enter the number of the quiz you want to take: "))
            if any(quiz[0] == quiz_id for quiz in quizzes):
                break
            else:
                print("Invalid quiz ID. Please select from the list above.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    while True:
        difficulty = input("Select difficulty level (easy, medium, hard, or leave blank for all): ").strip().lower()
        if difficulty in ['', 'easy', 'medium', 'hard']:
            break
        else:
            print("Invalid input. Please enter 'easy', 'medium', 'hard', or leave blank.")

    if difficulty:
        cursor.execute("SELECT * FROM questions WHERE quiz_id = ? AND difficulty = ?", (quiz_id, difficulty))
    else:
        cursor.execute("SELECT * FROM questions WHERE quiz_id = ?", (quiz_id,))
    questions = cursor.fetchall()

    if not questions:
        print("No questions are available for the selected quiz and difficulty level.")
        connection.close()
        return

    score = 0
    for question in questions:
        print("\n" + question[2])
        print(f"1. {question[3]}")
        print(f"2. {question[4]}")
        print(f"3. {question[5]}")
        print(f"4. {question[6]}")
        while True:
            try:
                answer = int(input("Enter your answer (1-4): "))
                if answer in [1, 2, 3, 4]:
                    break
                else:
                    print("Invalid input. Please enter a number between 1 and 4.")
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 4.")

        if answer == question[7]:
            print("Correct!")
            score += 1
        else:
            print("Wrong. The correct answer was:", question[7])

    cursor.execute('''
    INSERT INTO scores (user_id, quiz_id, score) VALUES (?, ?, ?)
    ''', (user_id, quiz_id, score))
    connection.commit()
    connection.close()

    print(f"\nYou scored {score}/{len(questions)}.")



def view_scores(user_id):
    """Allow users to view their scores."""
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute('''
    SELECT quizzes.name, scores.score FROM scores
    JOIN quizzes ON scores.quiz_id = quizzes.id
    WHERE scores.user_id = ?
    ''', (user_id,))
    scores = cursor.fetchall()
    connection.close()

    if scores:
        for quiz_name, score in scores:
            print(f"Quiz: {quiz_name}, Score: {score}")
    else:
        print("No scores available.")
