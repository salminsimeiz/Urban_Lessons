from fastapi import FastAPI
from Module_17.app.routers import user
from Module_17.app.routers import task

app = FastAPI()


@app.get('/')
async def wellcome():
    return {'message': 'Wellcome to Taskmanager'}


app.include_router(task.router)
app.include_router(user.router)
