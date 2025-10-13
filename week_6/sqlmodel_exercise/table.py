"""
Exercise 1: Basic Table

Task: Create a Book model with the following columns:
id → primary key
title → string
author → string
published_year → integer
"""

from sqlmodel import SQLModel, Field

class Book(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)  
    title: str
    author: str
    published_year: int | None = None  
