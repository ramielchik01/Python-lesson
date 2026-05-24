from fastapi import FastAPI

app = FastAPI()

# Path Parametr
@app.get('/users/{user_id}')
def get_user(user_id: int):
    return {user_id }

#Query Parametr 
@app.get('/users1Query')
def get_userQuery(limit: int=10, skip: int=0):
    return {'limit': limit, 'skip': skip}

# Body parameters 