
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from database import get_connection, create_table

app = FastAPI()

# Database table create karna
create_table()


# Student ka data aur fields define karna
class StudentCreate(BaseModel):
    name: str
    date_of_birth: str
    email: str | None = None
    phone: str | None = None


# Home API
@app.get("/")
def home():
    return {"message": "Student CRUD API is running!"}


# Naya student add karna
@app.post("/students")
def create_student(student: StudentCreate):
    conn = get_connection()

    try:
        cursor = conn.execute(
            """
            INSERT INTO students (name, date_of_birth, email, phone)
            VALUES (?, ?, ?, ?)
            """,
            (
                student.name,
                student.date_of_birth,
                student.email,
                student.phone
            )
        )

        conn.commit()

        return {
            "message": "Student created successfully",
            "student_id": cursor.lastrowid
        }

    finally:
        conn.close()


# Sabhi students ka data dekhna
@app.get("/students")
def get_students():
    conn = get_connection()

    try:
        cursor = conn.execute("SELECT * FROM students")
        students = cursor.fetchall()

        return [dict(student) for student in students]

    finally:
        conn.close()


# Ek student ko ID se dekhna
@app.get("/students/{student_id}")
def get_student(student_id: int):
    conn = get_connection()

    try:
        cursor = conn.execute(
            "SELECT * FROM students WHERE id = ?",
            (student_id,)
        )

        student = cursor.fetchone()

        if student is None:
            raise HTTPException(
                status_code=404,
                detail="Student not found"
            )

        return dict(student)

    finally:
        conn.close()


# Student ki details update karna
@app.put("/students/{student_id}")
def update_student(student_id: int, student: StudentCreate):
    conn = get_connection()

    try:
        cursor = conn.execute(
            "SELECT * FROM students WHERE id = ?",
            (student_id,)
        )

        existing_student = cursor.fetchone()

        if existing_student is None:
            raise HTTPException(
                status_code=404,
                detail="Student not found"
            )

        conn.execute(
            """
            UPDATE students
            SET name = ?, date_of_birth = ?, email = ?, phone = ?
            WHERE id = ?
            """,
            (
                student.name,
                student.date_of_birth,
                student.email,
                student.phone,
                student_id
            )
        )

        conn.commit()

        return {
            "message": "Student updated successfully",
            "student_id": student_id
        }

    finally:
        conn.close()


# Student ko delete karna
@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    conn = get_connection()

    try:
        cursor = conn.execute(
            "SELECT * FROM students WHERE id = ?",
            (student_id,)
        )

        student = cursor.fetchone()

        if student is None:
            raise HTTPException(
                status_code=404,
                detail="Student not found"
            )

        conn.execute(
            "DELETE FROM students WHERE id = ?",
            (student_id,)
        )

        conn.commit()

        return {
            "message": "Student deleted successfully",
            "student_id": student_id
        }

    finally:
        conn.close()
