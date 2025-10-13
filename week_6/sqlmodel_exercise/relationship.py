"""
Exercise 2: One-to-Many Relationship
Scenario: A Library has many Books.
Task:
    Create Library model: id, name
    Create Book model: id, title, library_id → foreign key to Library
Add relationships so you can access library.books and book.library.

Exercise 3: Many-to-Many Relationship
Scenario: Students can enroll in multiple Courses and each course has many students.
Task:
    Create Student model: id, name, age
    Create Course model: id, name
    Create StudentCourseLink model for linking
Add relationships so you can access student.courses and course.students
"""

from typing import List, Optional
from sqlmodel import SQLModel, Field, Relationship

# One-to-Many Relationship
class Library(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str
    books: List["Book"] = Relationship(back_populates="library")  

class Book(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    title: str
    library_id: Optional[int] = Field(default=None, foreign_key="library.id")
    library: Optional[Library] = Relationship(back_populates="books") 


# Many-to-many Relationship
class StudentCourseLink(SQLModel, table = True):
    student_id: Optional[int] = Field(default=None, foreign_key="student.id", primary_key=True)
    course_id: Optional[int] = Field(default=None, foreign_key="course.id", primary_key=True)
    # primary_key = True on both columns
    # Together, form a composite primary key

class Student(SQLModel, table=True):
    id: int = Field(primary_key=True, default=None)
    name: str
    age: int
    courses: List["Course"] = Relationship(back_populates="students", link_model=StudentCourseLink)


class Course(SQLModel, table = True):
    id: int = Field(primary_key=True, default=None)
    name: str
    students: List["Student"] = Relationship(back_populates="courses", link_model=StudentCourseLink)


