from pydantic import BaseModel


class UserCreate(BaseModel):
    name: str
    password: str
    password_repeat:str
class UserLogin(BaseModel):
    username: str
    password: str
class UserResponce(BaseModel):
    id: int
    name: str
    class Config:
        from_attributes = True
class Token(BaseModel):
    access_token: str
    token_type: str
class NoteCreate(BaseModel):
    name: str
    note: str
class NoteUpdate(BaseModel):
    name: str
    note: str
class NoteResponce(BaseModel):
    id: int
    user_id: int
    name: str
    note: str
    class Config:
        from_attributes = True