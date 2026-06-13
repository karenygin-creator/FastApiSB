from fastapi import APIRouter, HTTPException
from fastapi.params import Depends
from sqlalchemy.orm import Session

from auth import hash_password
from database import get_db
from models import User
from schemas import UserResponce, UserCreate

router=APIRouter(prefix="/users", tags=["Users"])

@router.post("/register", response_model=UserResponce)
def register_user(user_data: UserCreate,db:Session=Depends(get_db)):
    if user_data.password!=user_data.password_repeat:
        raise HTTPException(status_code=400, detail="Пароли не совпадают")
    existing_user = db.query(User).filter(User.name==user_data.name).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Пользователь "
                                                    "с таким именем уже существует")
    new_user = User(name=user_data.name,
                    password=hash_password(user_data.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user