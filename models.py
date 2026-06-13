from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, relationship
from sqlalchemy.testing.schema import mapped_column

from database import Base




class User(Base):
    __tablename__ = 'users'
    id:Mapped[int]=mapped_column(primary_key=True,index=True)
    name:Mapped[str]=mapped_column(String(100),unique=True,index=True)
    password:Mapped[str]=mapped_column(String(255))
    notes:Mapped[list["Note"]]=relationship(back_populates="user",cascade="all,delete")

class Note(Base):
    __tablename__ = 'notes'
    id:Mapped[int]=mapped_column(primary_key=True,index=True)
    user_id:Mapped[int]=mapped_column(ForeignKey('users.id'))
    name:Mapped[str]=mapped_column(String(100))
    note:Mapped[str]=mapped_column(String(500))
    user:Mapped["User"]=relationship(back_populates='notes')