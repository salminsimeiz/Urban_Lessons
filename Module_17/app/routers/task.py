from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from Module_17.app.backend.db_dependns import get_db
from typing import Annotated
from Module_17.app.models.task import Task
from Module_17.app.models.user import User
from Module_17.app.schemas import CreateTask, UpdateTask
from sqlalchemy import insert, select, update, delete
from slugify import slugify
from sqlalchemy.exc import IntegrityError


router = APIRouter(prefix='/task', tags=['task'])


@router.get('/')
async def all_tasks(db: Annotated[Session, Depends(get_db)]):
    tasks = db.scalars(select(Task)).all()
    return tasks


@router.get('/task_id')
async def task_by_id(db: Annotated[Session, Depends(get_db)], task_id: int):
    task = db.scalar(select(Task).where(Task.id == task_id))
    if task is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task was not found")
    return task


@router.post('/create')
async def create_task(db: Annotated[Session, Depends(get_db)], create_task: CreateTask, user_id: int):
    user = db.scalar(select(User).where(User.id == user_id))
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User was not found")
    else:
        try:
            db.execute(insert(Task).values(title=create_task.title,
                                           content=create_task.content,
                                           priority=create_task.priority,
                                           completed=create_task.completed,
                                           user_id=user_id,
                                           slug=slugify(create_task.title)))
            db.commit()
            return {'status_code': status.HTTP_201_CREATED, 'transaction': 'Successful'}
        except IntegrityError:
            return {'status_code': status.HTTP_304_NOT_MODIFIED, 'reason': 'UNIQUE constraint failed'}


@router.put('/update')
async def update_task(db: Annotated[Session, Depends(get_db)], update_task: UpdateTask, user_id: int, task_id: int):
    user = db.scalar(select(User).where(User.id == user_id))
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User was not found")
    else:
        task = db.scalar(select(Task).where(Task.id == task_id))
        if task is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task was not found")
        else:
            db.execute(update(Task).where(Task.id == task_id).values(content=update_task.content,
                                                                     priority=update_task.priority,
                                                                     completed=update_task.completed))
            db.commit()
            return {'status_code': status.HTTP_200_OK, 'transaction': 'Task update is successful!'}


@router.delete('/delete')
async def delete_task(db: Annotated[Session, Depends(get_db)], task_id: int):
    task = db.scalar(select(Task).where(Task.id == task_id))
    if task is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task was not found")
    db.execute(delete(Task).where(Task.id == task_id))
    db.commit()
    return {'status_code': status.HTTP_200_OK, 'transaction': 'Task delete is successful!'}
