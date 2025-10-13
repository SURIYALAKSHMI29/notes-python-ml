# Table of Contents

1. [SQLModel](#sqlmodel)
2. [Model Definition](#model-definition)
3. [Database Engine](#database-engine)
4. [Create Tables](#create-tables)
5. [Sessions](#sessions)
6. [Relationships](#relationships)
---

# SQLModel

- Combines the pydantic(for data validation) and SQLAlchemy
    - So only one model is required
    - Fully typed model
    - Has automatic Data validation
- Includes synchronous support → helpful to handle multiple requests concurrently
- Works well with alembic - database migration

### Usecase:

- Define databases tables as python classes
- Can use those classes as,
    - Database models to store data
    - Request / Response models to handle API data

## Model Definition

To define a class that represents a database table

```python
from sqlmodel import SQLModel, Field

class Student(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    age: int
    department: str
```

- *table=True* → makes it a database table.
- *Field(…)* → used for special attributes (like primary keys).
- Type hints (like *int*, *str*) → used for validation and database schema.

## Database Engine

This connects SQLModel to your database.

```python
from sqlmodel import create_engine

engine = create_engine("sqlite:///students.db")  # file-based database
```

## Create Tables

```python
SQLModel.metadata.create_all(engine)
```

- SQLModel collects all table definitions (via metadata)
- It sends *CREATE TABLE IF NOT EXISTS* SQL commands to your database
- If the tables already exist, it won’t recreate them (safe to run multiple times)

## Sessions

- A session is the connection to the database

```python
from sqlmodel import Session, select

# Insert
with Session(engine) as session:
    student = Student(name="Alice", age=21, department="CSE")
    session.add(student)
    session.commit()
    session.refresh(student)  # fetch updated data (with id)
    print(student)

# Select
with Session(engine) as session:
    result = session.exec(select(Student)).all()
    print(result)
```

# Relationships

- Relationships should be specified
- One-to-Many relationship
    
    ```python
    class Team(SQLModel, table=True):
    	...
    	heroes: list["Hero"] = Relationship(back_populates="team")
    
    class Hero(SQLModel, table=True):
    	...
    	team: Optional[Team] = Relationship(back_populated="heroes")
    ```
    
- Many-to-Many Relationship
    
    ```python
    class Mission(SQLModel, table=True):
    	...
    	heroes: list["Hero"] = Relationship(
    		back_populates="missions", link_model="HeroMissionLink"
    	)
    
    class Hero(SQLModel, table = True):
    	...
    	missions: list["Mission"] = Relationship(
    		back_populates="heroes", link_model="HeroMissionLink"
    	)
    
    class HeroMissionModel(SQLModel, table=True):
    	hero_id: Optional[int] = Field(
    		default=None, foreign_key="hero.id", primary_key=True
    	)
    	mission_id: Optional[int] = Field(
    		default=None, foreign_key="mission.id", primary_key=True
    	)
    ```
    
    - We cannot store a list missions in each hero, and list of heroes in each mission
    - Creating a common table that links them → efficient, reduces redundancy
