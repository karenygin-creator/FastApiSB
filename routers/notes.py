from fastapi import APIRouter, HTTPException
from fastapi.params import Depends
from sqlalchemy.orm import Session

from auth import get_current_user
from database import get_db
from models import User, Note
from schemas import UserResponce, NoteResponce, NoteCreate, NoteUpdate

router=APIRouter(prefix="/notes", tags=["Notes"])
@router.get("/", response_model=list[NoteResponce])
def get_my_notes(db:Session=Depends(get_db),current_user:User=Depends(get_current_user)):
    notes=db.query(Note).filter(Note.user_id == current_user.id).all()
    return notes
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

@router.put("/{note_id}", response_model=NoteResponce)
def create_notes(note_id:int,note_data:NoteUpdate,db:Session=Depends(get_db),current_user:User=Depends(get_current_user)):
    note=db.query(Note).filter(Note.id==note_id,Note.user_id==current_user.id).first()
    if not note:
        raise HTTPException(status_code=404,detail="Note not found")
    note.name=note_data.name
    note.note=note_data.note
    db.commit()
    db.refresh(note)
    return note



@router.delete("/{note_id}")
def delete_note(note_id:int,db:Session=Depends(get_db),current_user:User=Depends(get_current_user)):
    note=db.query(Note).filter(Note.id==note_id,Note.user_id==current_user.id).first()
    if not note:
        raise HTTPException(status_code=404,detail="Note not found")
    db.delete(note)
    db.commit()
    return {"message": "Note deleted"}