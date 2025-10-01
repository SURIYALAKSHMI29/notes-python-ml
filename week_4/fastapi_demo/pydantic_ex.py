from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str = "Guest"


new_user = User(id="101", name="Suriya")
print(new_user)  # id=101 name='Suriya'
