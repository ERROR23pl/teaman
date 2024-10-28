import asyncio

from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.ext.asyncio import AsyncSession
import models, schemas
from database import AsyncSessionLocal, engine, get_db
import uvicorn
from datetime import timedelta
from src.server import auth
from src.server.datasource.crud import user_crud
from src.server.datasource.init_db import init_db

app = FastAPI(title="TEAMAN")
HOST = "localhost"
PORT = 8000
AUX_PORT = 4200

origins = [
    f"http://${HOST}:${AUX_PORT}",
    "http://localhost:4200"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=['*']
)

@app.post("/signup/", response_model=schemas.User)
async def create_user(user: schemas.UserCreate, db: AsyncSession = Depends(get_db)):
    db_user = await user_crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail=f"Email ${db_user.email} already registered")
    return await user_crud.create_user(db=db, user=user)

@app.post("/token", response_model=schemas.Token)
async def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: AsyncSession = Depends(get_db)
):
    user = await user_crud.authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=auth.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = auth.create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@app.get("/users/me/", response_model=schemas.User)
async def read_users_me(
    current_user: schemas.User = Depends(user_crud.get_current_user)
):
    return current_user

async def main():
    # await init_db() # TODO uncomment
    uvicorn.run("tmp:app", host=HOST, port=PORT, reload=True)


if __name__ == "__main__":
    asyncio.run(main())