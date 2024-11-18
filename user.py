from db import get_connection

def take_quiz(user_id):
    """Allow users to take a quiz."""
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

    quiz_id = int(input("Enter the number of the quiz you want to take: "))
    cursor.execute("SELECT * FROM questions WHERE quiz_id = ?", (quiz_id,))
    questions = cursor.fetchall()

    if not questions:
        print("No questions available for this quiz.")
        connection.close()
        return

    score = 0
    for question in questions:
        print("\n" + question[2])
        print(f"1. {question[3]}")
        print(f"2. {question[4]}")
        print(f"3. {question[5]}")
        print(f"4. {question[6]}")
        answer = int(input("Enter your answer (1-4): "))
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
