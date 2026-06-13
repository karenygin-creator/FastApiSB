
from fastapi import FastAPI, HTTPException
from fastapi.params import Path, Query, Body
from starlette import status
from starlette.responses import HTMLResponse, FileResponse, JSONResponse, Response, RedirectResponse
from starlette.staticfiles import StaticFiles

from database import engine, Base
from routers import users


Base.metadata.create_all(bind=engine)
app=FastAPI(title="To-Do List Api", description="Для заметок")
@app.get("/")
def home():
    return {"message": "To-Do List Api"}

app.include_router(users.router)