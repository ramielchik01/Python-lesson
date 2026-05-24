from fastapi import FastAPI

app = FastAPI()

# Path Parametr
@app.get('/users/{user_id}')
def get_user(user_id: int):
    return {user_id }