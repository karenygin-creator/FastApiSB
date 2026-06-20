from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy.orm import Session

from auth import get_current_user
from database import get_db
from models import User, Note
from schemas import UserResponce, NoteResponce, NoteCreate

router=APIRouter(prefix="/notes", tags=["Notes"])
@router.post("/", response_model=NoteResponce)
def create_notes(note_data:NoteCreate,db:Session=Depends(get_db),current_user:User=Depends(get_current_user)):
    new_note=Note(
        name=note_data.name,
        note=note_data.note,
        user_id=current_user.id
    )
    db.add(new_note)
    db.commit()
    db.refresh(new_note)
    return new_note