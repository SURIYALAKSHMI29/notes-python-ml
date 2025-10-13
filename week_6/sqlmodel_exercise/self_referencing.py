"""
Exercise 4: Self-referencing Table
Scenario: Employees and Managers.
Task:
    Create Employee model: id, name, manager_id → foreign key to Employee
    Add relationship manager and subordinates
Allows querying who reports to whom.
"""


from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List

class Employee(SQLModel, table=True):
    id: Optional[int] = Field(primary_key = True, default = None)
    name: str
    manager_id: Optional[int] = Field(foreign_key="employee.id", default = None)
    manager: Optional["Employee"] = Relationship(back_populates="subordinates")
    subordinates: List["Employee"] = Relationship(back_populates="manager")