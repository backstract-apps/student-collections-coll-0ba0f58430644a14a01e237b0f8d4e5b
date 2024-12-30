from fastapi import APIRouter, Depends, HTTPException, UploadFile, Form
from sqlalchemy.orm import Session
from typing import List
import service, models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get('/student/')
async def get_student(db: Session = Depends(get_db)):
    return await service.get_student(db)

@router.get('/student/user_id')
async def get_student_user_id( user_id: int , db: Session = Depends(get_db)):
    return await service.get_student_user_id(db , user_id)

@router.post('/student/')
async def post_student( user_id: int, name: str, email: str, password: str, role: str , db: Session = Depends(get_db)):
    return await service.post_student(db , user_id, name, email, password, role)

@router.put('/student/user_id/')
async def put_student_user_id( user_id: str, name: str, email: str, password: str, role: str , db: Session = Depends(get_db)):
    return await service.put_student_user_id(db , user_id, name, email, password, role)

@router.delete('/student/user_id')
async def delete_student_user_id( user_id: int , db: Session = Depends(get_db)):
    return await service.delete_student_user_id(db , user_id)

