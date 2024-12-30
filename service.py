from sqlalchemy.orm import Session
from typing import List
from fastapi import UploadFile
import models, schemas
import boto3

from pathlib import Path

async def get_student(db: Session):

    student_all = db.query(models.Student).all()
    res = {
        'student_all': student_all,
    }
    return res

async def get_student_user_id(db: Session, user_id: int):

    student_one = db.query(models.Student).filter(models.Student.user_id == user_id).first()
    res = {
        'student_one': student_one,
    }
    return res

async def post_student(db: Session, user_id: int, name: str, email: str, password: str, role: str):

    record_to_be_added = {'user_id': user_id, 'name': name, 'email': email, 'password': password, 'role': role}
    new_student = models.Student(**record_to_be_added)
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    student_inserted_record = new_student
    res = {
        'student_inserted_record': student_inserted_record,
    }
    return res

async def put_student_user_id(db: Session, user_id: str, name: str, email: str, password: str, role: str):

    student_edited_record = db.query(models.Student).filter(models.Student.user_id == user_id).first()
    for key, value in {'user_id': user_id, 'name': name, 'email': email, 'password': password, 'role': role}.items():
          setattr(student_edited_record, key, value)
    db.commit()
    db.refresh(student_edited_record)
    student_edited_record = student_edited_record

    res = {
        'student_edited_record': student_edited_record,
    }
    return res

async def delete_student_user_id(db: Session, user_id: int):

    student_deleted = None
    record_to_delete = db.query(models.Student).filter(models.Student.user_id == user_id).first()

    if record_to_delete:
          db.delete(record_to_delete)
          db.commit()
          student_deleted = record_to_delete
    res = {
        'student_deleted': student_deleted,
    }
    return res

