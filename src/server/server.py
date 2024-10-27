from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime, timedelta, timezone
import jwt
from sqlalchemy.orm import Session
from datasource.database import AsyncSessionLocal, engine
from typing import Annotated
from passlib.context import CryptContext
from starlette.responses import HTMLResponse, RedirectResponse
from starlette.templating import Jinja2Templates
from fastapi import Request, status, Form
from fastapi.middleware.cors import CORSMiddleware
# Initialize FastAPI app
app = FastAPI(
    title="TEAMAN",
    description="Teaman is a safe and responsive web management app. Written by professionals from MTI univertisy",
    version="0.0.1"
)

origins = [
    'https://localhost:3000'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins
)

# dummy models
class User(BaseModel):
    username: str
    email: Optional[str] = None
    full_name: Optional[str] = None

class UserInDB(User):
    hashed_password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class Project(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    owner: str

class Task(BaseModel):
    id: int
    project_id: int
    title: str
    description: Optional[str] = None
    status: str = "TODO"

class Message(BaseModel):
    id: int
    sender: str
    content: str
    timestamp: datetime


# Security
SECRET_KEY: str = "your-secret-key"
ALGORITHM: str = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

pwd_context: CryptContext = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme: OAuth2PasswordBearer = OAuth2PasswordBearer(tokenUrl="token")

# Helper functions
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

def get_user(db, username: str):
    if username in db:
        user_dict = db[username]
        return UserInDB(**user_dict)

def authenticate_user(db, username: str, password: str):
    user = get_user(db, username)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user

def create_access_token(data: dict, expires_delta: timedelta = timedelta(minutes=15)):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + expires_delta
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except jwt.PyJWTError:
        raise credentials_exception
    user = get_user(users_db, username=username)
    if user is None:
        raise credentials_exception
    return user

# Routes
@app.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(users_db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@app.post("/users/", response_model=User)
async def create_user(user: User, password: str):
    if user.username in users_db:
        raise HTTPException(status_code=400, detail="Username already registered")
    hashed_password = get_password_hash(password)
    user_dict = user.model_dump()
    user_dict["hashed_password"] = hashed_password
    users_db[user.username] = user_dict
    return user

@app.get("/users/me", response_model=User)
async def read_users_me(current_user: User = get_current_user()):
    return current_user

@app.post("/projects/", response_model=Project)
async def create_project(project: Project, current_user: User = Depends(get_current_user)):
    project_id = len(projects_db) + 1
    project_dict = project.dict()
    project_dict["id"] = project_id
    project_dict["owner"] = current_user.username
    projects_db[project_id] = project_dict
    return project_dict

@app.get("/projects/", response_model=List[Project])
async def read_projects(current_user: User = Depends(get_current_user)):
    return [project for project in projects_db.values() if project["owner"] == current_user.username]

@app.post("/tasks/", response_model=Task)
async def create_task(task: Task, current_user: User = Depends(get_current_user)):
    if task.project_id not in projects_db or projects_db[task.project_id]["owner"] != current_user.username:
        raise HTTPException(status_code=403, detail="Not authorized to create task for this project")
    task_id = len(tasks_db) + 1
    task_dict = task.dict()
    task_dict["id"] = task_id
    tasks_db[task_id] = task_dict
    return task_dict

@app.get("/tasks/{project_id}", response_model=List[Task])
async def read_tasks(project_id: int, current_user: User = Depends(get_current_user)):
    if project_id not in projects_db or projects_db[project_id]["owner"] != current_user.username:
        raise HTTPException(status_code=403, detail="Not authorized to view tasks for this project")
    return [task for task in tasks_db.values() if task["project_id"] == project_id]

@app.post("/messages/", response_model=Message)
async def create_message(content: str, current_user: User = Depends(get_current_user)):
    message_id = len(messages_db) + 1
    message = Message(
        id=message_id,
        sender=current_user.username,
        content=content,
        timestamp=datetime.utcnow()
    )
    messages_db[message_id] = message.dict()
    return message

@app.get("/messages/", response_model=List[Message])
async def read_messages(current_user: User = Depends(get_current_user)):
    return list(messages_db.values())

#
# # Setting up Jinja2 for rendering HTML templates
templates = Jinja2Templates(directory="templates")




@app.get("/", response_class=HTMLResponse)
async def get_login_page(request: Request):
    # Render the login page using the template
    return templates.TemplateResponse("login.html", {"request": request})


@app.post("/login")
async def login(request: Request, username: str = Form(...), password: str = Form(...)):
    # Authenticate user
    user = authenticate_user(users_db, username, password)

    if user:
        # Redirect to a welcome page if login succeeds
        response = RedirectResponse(url="./logged_home", status_code=status.HTTP_302_FOUND)
        return response
    else:
        # If authentication fails, show an error message
        return templates.TemplateResponse("login.html", {"request": request, "error": "Invalid username or password"})


@app.get("/logged_home", response_class=HTMLResponse)
async def welcome_page(request: Request):
    # Render a welcome page for authenticated users
    return templates.TemplateResponse("user_home.html", {"request": request, "message": "Welcome to the app!"})


users_db = {
    "user1": {
        "username": "user1",
        "email" : "mockemail1",
        "full_name": "jane doe",
        "hashed_password": get_password_hash(password="admin")

    },
    "admin": {
        "username": "admin",
        "email" : "mockemail1",
        "full_name": "adminpass",
        "hashed_password": get_password_hash(password="admin")
    }
}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8888)