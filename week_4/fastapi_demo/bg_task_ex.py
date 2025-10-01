from fastapi import BackgroundTasks, FastAPI

app = FastAPI()


def send_email(email: str):
    print(f"Sending email to {email}")


@app.post("/send")
def send_notification(email: str, background_tasks: BackgroundTasks):
    # add task to background
    background_tasks.add_task(send_email, email)
    return {"message": "Email will be sent in background"}
