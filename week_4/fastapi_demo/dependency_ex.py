from fastapi import Depends, FastAPI

app = FastAPI()

current_user = "Guest"


def get_current_user():
    return current_user


@app.put("/change-user/{user}")
def change_user(user: str):
    global current_user
    current_user = user
    return {"Message": f"Successfully change current user as {current_user}"}


@app.get("/profile")
def read_profile(user: str = Depends(get_current_user)):
    return {"User": user}
