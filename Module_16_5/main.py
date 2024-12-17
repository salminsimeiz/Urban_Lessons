from fastapi import FastAPI, HTTPException, Path, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel, ValidationError
from typing import List, Annotated


class User(BaseModel):
    id: int
    username: str
    age: int


app = FastAPI(swagger_ui_parameters={"tryItOutEnabled": True}, debug=True)
templates = Jinja2Templates(directory="templates")

users: List[User] = []


@app.get("/")
async def get_main_page(request: Request) -> HTMLResponse:
    return templates.TemplateResponse("users.html", {"request": request, "users": users})


@app.get('/user/{user_id}', response_class=HTMLResponse)
async def get_users(request: Request, user_id: Annotated[int, Path(ge=0, description="Enter existing id")]):
    for user in users:
        if user.id == user_id:
            return templates.TemplateResponse("users.html", {"request": request, "user": user})
    else:
        raise HTTPException(status_code=404, detail="User not found")


@app.post('/')
async def create_user(request: Request, username: str = Form(), age: int = Form()) -> HTMLResponse:
    new_id = max(u.id for u in users) + 1 if users else 1
    new_user = User(id=new_id, username=username, age=age)
    users.append(new_user)
    return templates.TemplateResponse("users.html", {"request": request, "users": users})


@app.put('/user/{user_id}/{username}/{age}', response_model=User)
async def update_user(user_id: Annotated[int, Path(ge=0, description="Enter existing id")],
                      username: Annotated[str, Path(min_length=5, max_length=15,
                                                    description="Enter username",
                                                    example="Urban_admin")],
                      age: Annotated[int, Path(ge=18, le=100, description="Enter age", example=20)]) -> User:
    for user in users:
        if user.id == user_id:
            user.username = username
            user.age = age
            return user
    raise HTTPException(status_code=404, detail="user was not found")


@app.delete('/user/{user_id}', response_model=User)
async def delete_user(user_id: int) -> User:
    for i, user in enumerate(users):
        if user.id == user_id:
            return users.pop(i)
    raise HTTPException(status_code=404, detail="user was not found")
