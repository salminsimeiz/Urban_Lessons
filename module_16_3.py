
from fastapi import FastAPI, Path, HTTPException
from typing import Annotated


app = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}


@app.get('/users')
async def get_users() -> dict:
    return users


@app.post('/user/{username}/{age}')
async def post_user(username: Annotated[str, Path(min_length=5,
                                                  max_length=20,
                                                  description="Enter username",
                                                  example="UrbanUser")],
                    age: Annotated[int, Path(ge=18,
                                             le=120,
                                             description="Enter age",
                                             example=24)]
                    ) -> str:
    user_id = str(int(max(enumerate(users))[1])+1)
    users[user_id] = f'Имя: {username}, возраст: {age}'
    return f'User {user_id} is registered'


@app.put('/user/{user_id}/{username}/{age}')
async def update_user(user_id: Annotated[str, Path(min_length=1,
                                                   max_length=3,
                                                   description="Enter id",
                                                   example="6")],
                      username: Annotated[str, Path(min_length=5,
                                                    max_length=20,
                                                    description="Enter username",
                                                    example="UrbanUser")],
                      age: Annotated[int, Path(ge=18,
                                               le=120,
                                               description="Enter age",
                                               example=24)]
                      ) -> str:
    if user_id in users:
        users[user_id] = f'Имя: {username}, возраст: {age}'
        return f'The user {user_id} has been updated'
    raise HTTPException(status_code=404, detail="id not found")


@app.delete('/user/{user_id}')
async def delete_user(user_id: Annotated[str, Path(min_length=1,
                                                   max_length=3,
                                                   description="Enter id",
                                                   example="6")]
                      ) -> str:
    if user_id in users:
        del users[user_id]
        return f'The user {user_id} has been deleted'
    raise HTTPException(status_code=404, detail="id not found")
