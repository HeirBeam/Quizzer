
# Advanced Quiz Application

This is an advanced Quiz Application with user authentication, admin roles, and score tracking. It uses Python and SQLite for backend logic and data storage.

## Features

- **User Authentication**: Users can log in or create accounts securely.
- **Admin Role**:
  - The first admin can register without verification.
  - Subsequent admin accounts require an existing admin's credentials for verification.
- **Quiz Functionality**:
  - Users can take quizzes and view their scores.
  - Admins can create quizzes and add questions.
- **Database**: SQLite is used to manage all data, including users, quizzes, questions, and scores.
- **Role-Based Access Control**: Non-admin users can only take quizzes and view their scores.

## Project Structure

```
quiz_app/
│
├── main.py           # Entry point of the application
├── db.py             # Database connection and SQL queries
├── auth.py           # Authentication logic
├── admin.py          # Admin-related functions
├── user.py           # User-related functions (e.g., taking quizzes, viewing scores)
└── models.py         # Classes or helpers for quiz and question logic (if needed)
```

## Requirements

- Python 3.x

## How to Run

1. Clone the repository:

   ```bash
   git clone <your-repo-link>
   cd quiz_app
   ```

2. Run the application:

   ```bash
   python main.py
   ```

3. Follow the on-screen instructions to:
   - Log in or create an account.
   - Admins can create quizzes and add questions.
   - Users can take quizzes and view their scores.

## Notes

- The first admin account does not require admin verification.
- Admin privileges can only be granted with valid credentials from an existing admin.

## Example Workflow

1. **First Admin Registration**:
   - Register the first admin by creating an account with admin privileges. No verification is required.
2. **Subsequent Admins**:
   - To register as an admin, provide an existing admin's username and password during account creation.
3. **Users**:
   - Users can register without admin privileges and take quizzes.
   - Users can view their scores.

## Learning Goals

This project demonstrates:

- Role-based access control.
- User authentication with admin validation.
- Database-backed application logic using SQLite.
- Modularized Python programming for a command-line application.
