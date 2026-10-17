 Student CRUD Application

A Student Database CRUD Application built using Python, FastAPI, and SQLite.

# Features

- Create a new student
- View all students
- View a student by ID
- Update student details
- Delete a student

# Technologies Used

- Python
- FastAPI
- SQLite
- Uvicorn

# Project Setup

1. Clone or download this project.
2. Open the project folder in the terminal.
3. Create and activate a virtual environment.
4. Install dependencies:

```bash
pip install -r requirements.txt
```

# Run the Application

```bash
python -m uvicorn main:app --reload
```

Open the API documentation in your browser:

http://127.0.0.1:8000/docs

# Database

The application uses SQLite to store student records. The database table is created automatically when the application starts.

# CRUD Operations

- POST `/students`
- GET `/students`
- GET `/students/{student_id}`
- PUT `/students/{student_id}`
- DELETE `/students/{student_id}`
