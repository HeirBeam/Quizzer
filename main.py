from db import setup_database
from auth import create_account, login
from admin import add_quiz, add_question
from user import take_quiz, view_scores

def main():
    setup_database()
    current_user = None

    while True:
        if not current_user:
            print("\n--- Quiz Application ---")
            print("1. Login")
            print("2. Create Account")
            print("3. Exit")
            choice = input("Enter your choice: ")
            if choice == "1":
                current_user = login()
            elif choice == "2":
                create_account()
            elif choice == "3":
                print("Exiting the application.")
                break
            else:
                print("Invalid choice. Please try again.")
        else:
            print(f"\n--- Welcome, {current_user['username']} ---")
            print("1. Take a Quiz")
            print("2. View Scores")
            if current_user["is_admin"]:
                print("3. Add a Quiz")
                print("4. Add Questions")
            print("5. Logout")
            choice = input("Enter your choice: ")

            if choice == "1":
                take_quiz(current_user["id"])
            elif choice == "2":
                view_scores(current_user["id"])
            elif choice == "3" and current_user["is_admin"]:
                add_quiz()
            elif choice == "4" and current_user["is_admin"]:
                add_question()
            elif choice == "5":
                current_user = None
                print("Logged out.")
            else:
                print("Invalid choice or insufficient privileges.")

if __name__ == "__main__":
    main()
