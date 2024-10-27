from typing import Optional, List
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import or_
import models
import schemas
from .database import get_db
from .. import auth
from ..auth import get_hash, verify_password
from fastapi import HTTPException, status

# crud.py
from fastapi import Depends, HTTPException, status

# def get_user(db: Session, user_id: int):
#     return db.query(models.User).filter(models.User.id == user_id).first()
#
# def get_user_by_email(db: Session, email: str):
#     return db.query(models.User).filter(models.User.email == email).first()
#
# def get_users(db: Session, skip: int = 0, limit: int = 100):
#     return db.query(models.User).offset(skip).limit(limit).all()
#
# def create_user(db: Session, user: schemas.UserCreate):
#     hashed_password = auth.get_password_hash(user.password)
#     db_user = models.User(
#         email=user.email,
#         username=user.username,
#         hashed_password=hashed_password
#     )
#     db.add(db_user)
#     db.commit()
#     db.refresh(db_user)
#     return db_user
#
# def authenticate_user(db: Session, username: str, password: str):
#     user = db.query(models.User).filter(models.User.username == username).first()
#     if not user:
#         return False
#     if not auth.verify_password(password, user.hashed_password):
#         return False
#     return user
#


class UserCRUD:
    async def get_user(self, db: AsyncSession, user_id: int) -> Optional[models.User]:
        """Get user by ID."""
        query = select(models.User).where(models.User.id == user_id)
        result = await db.execute(query)
        return result.scalar_one_or_none()

    async def get_user_by_email(self, db: AsyncSession, email: str) -> Optional[models.User]:
        """Get user by email."""
        query = select(models.User).where(models.User.email == email)
        result = await db.execute(query)
        return result.scalar_one_or_none()

    async def get_user_by_username(self, db: AsyncSession, username: str) -> Optional[models.User]:
        """Get user by username."""
        query = select(models.User).where(models.User.username == username)
        result = await db.execute(query)
        return result.scalar_one_or_none()

    async def get_current_user(self,
        token: str = Depends(auth.oauth2_scheme),
        db: AsyncSession = Depends(get_db)
    ):
        credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
        try:
            payload = auth.jwt.decode(token, auth.SECRET_KEY, algorithms=[auth.ALGORITHM])
            email: str = payload.get("sub")
            if email is None:
                raise credentials_exception
        except auth.JWTError:
            raise credentials_exception
        user = await self.get_user_by_email(db=db, email=email)
        if user is None:
            raise credentials_exception
        return user

    async def get_users(
            self,
            db: AsyncSession,
            skip: int = 0,
            limit: int = 100
    ) -> List[models.User]:
        """Get list of users with pagination."""
        query = select(models.User).offset(skip).limit(limit)
        result = await db.execute(query)
        return [ user.index for user in result.all() ]

    async def create_user(
            self,
            db: AsyncSession,
            user: schemas.UserCreate
    ) -> models.User:
        """Create new user with input validation."""
        # Check if user already exists
        existing_user = await db.execute(
            select(models.User).where(
                or_(
                    models.User.email == user.email,
                    models.User.username == user.username
                )
            )
        )
        if existing_user.scalar_one_or_none():
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Username or email already registered"
            )

        # Create new user
        hashed_password = get_hash(user.password)
        db_user = models.User(
            email=user.email,
            username=user.username,
            hashed_password=hashed_password
        )
        db.add(db_user)
        await db.commit()
        await db.refresh(db_user)
        return db_user

    async def authenticate_user(
            self,
            db: AsyncSession,
            username: str,
            password: str
    ) -> Optional[models.User]:
        """Authenticate user with username and password."""
        user = await self.get_user_by_username(db, username)
        if not user:
            return None
        if not verify_password(password, user.hashed_password):
            return None
        return user

    async def update_user(
            self,
            db: AsyncSession,
            user_id: int,
            user_update: schemas.UserUpdate
    ) -> Optional[models.User]:
        """Update user information."""
        user = await self.get_user(db, user_id)
        if not user:
            return None

        update_data = user_update.model_dump(exclude_unset=True)

        # Hash password if it's being updated
        if "password" in update_data:
            update_data["hashed_password"] = get_hash(update_data.pop("password"))

        # Update user attributes
        for field, value in update_data.items():
            setattr(user, field, value)

        await db.commit()
        await db.refresh(user)
        return user

    async def delete_user(
            self,
            db: AsyncSession,
            user_id: int
    ) -> bool:
        """Delete user by ID."""
        user = await self.get_user(db, user_id)
        if not user:
            return False

        await db.delete(user)
        await db.commit()
        return True

    async def deactivate_user(
            self,
            db: AsyncSession,
            user_id: int
    ) -> Optional[models.User]:
        """Deactivate user account."""
        user = await self.get_user(db, user_id)
        if not user:
            return None

        user.is_active = False
        await db.commit()
        await db.refresh(user)
        return user


# Create a global instance
user_crud = UserCRUD()



# from sqlalchemy.ext.asyncio import AsyncSession
# from sqlalchemy.future import select
# from sqlalchemy.orm import selectinload
# import models
#
# class CRUDBase:
#     def __init__(self, model):
#         self.model = model
#
#     async def get(self, db: AsyncSession, item_id: int):
#         query = select(self.model).where(self.model.id == item_id)
#         result = await db.execute(query)
#         return result.scalar_one_or_none()
#
#     async def get_multi(self, db: AsyncSession, skip: int = 0, limit: int = 100):
#         query = select(self.model).offset(skip).limit(limit)
#         result = await db.execute(query)
#         return result.scalars().all()
#
#     async def create(self, db: AsyncSession, obj_in):
#         db_obj = self.model(**obj_in.dict())
#         db.add(db_obj)
#         await db.commit()
#         await db.refresh(db_obj)
#         return db_obj
#
# # Initialize CRUD operations for models
# user_crud = CRUDBase(models.User)
# team_crud = CRUDBase(models.Team)
# channel_crud = CRUDBase(models.Channel)
# message_crud = CRUDBase(models.Message)


# FOR LATER:

# from typing import TypeVar, Generic, Type, Optional, List
# from pydantic import BaseModel
# from sqlalchemy.ext.asyncio import AsyncSession
# from sqlalchemy.future import select
# from sqlalchemy.exc import SQLAlchemyError
# from sqlalchemy.orm import selectinload
# from sqlalchemy.orm.decl_api import DeclarativeMeta
#
# ModelType = TypeVar("ModelType")
# class CRUDBase(Generic[ModelType, CreateSchemaType]):
#     def __init__(self, model: Type[DeclarativeMeta]):
#         self.model = model
#
#     async def get(
#         self,
#         db: AsyncSession,
#         item_id: int,
#         load_relationships: list[str] = None
#     ) -> Optional[ModelType]:
#         try:
#             query = select(self.model).where(self.model.id == item_id)
#             if load_relationships:
#                 for rel in load_relationships:
#                     query = query.options(selectinload(getattr(self.model, rel)))
#             result = await db.execute(query)
#             return result.scalar_one_or_none()
#         except SQLAlchemyError as e:
#             await db.rollback()
#             raise ValueError(f"Database error: {str(e)}")
#
#     async def get_multi(
#         self,
#         db: AsyncSession,
#         skip: int = 0,
#         limit: int = 100,
#         load_relationships: list[str] = None
#     ) -> List[ModelType]:
#         try:
#             query = select(self.model).offset(skip).limit(limit)
#             if load_relationships:
#                 for rel in load_relationships:
#                     query = query.options(selectinload(getattr(self.model, rel)))
#             result = await db.execute(query)
#             return result.scalars().all()
#         except SQLAlchemyError as e:
#             await db.rollback()
#             raise ValueError(f"Database error: {str(e)}")
#
#     async def create(
#         self,
#         db: AsyncSession,
#         obj_in: CreateSchemaType
#     ) -> ModelType:
#         try:
#             # Convert Pydantic model to dict and filter out unknown fields
#             obj_data = obj_in.model_dump(exclude_unset=True)
#             db_obj = self.model(**{
#                 k: v for k, v in obj_data.items()
#                 if hasattr(self.model, k)
#             })
#             db.add(db_obj)
#             await db.commit()
#             await db.refresh(db_obj)
#             return db_obj
#         except SQLAlchemyError as e:
#             await db.rollback()
#             raise ValueError(f"Database error: {str(e)}")
#
# # Initialize CRUD operations for models with proper typing
# from typing import TypeVar
# from schemas import UserCreate, TeamCreate, ChannelCreate, MessageCreate
#
# UserModel = TypeVar("UserModel", bound=models.User)
# TeamModel = TypeVar("TeamModel", bound=models.Team)
# ChannelModel = TypeVar("ChannelModel", bound=models.Channel)
# MessageModel = TypeVar("MessageModel", bound=models.Message)
#
# user_crud = CRUDBase[UserModel, UserCreate](models.User)
# team_crud = CRUDBase[TeamModel, TeamCreate](models.Team)
# channel_crud = CRUDBase[ChannelModel, ChannelCreate](models.Channel)
# message_crud = CRUDBase[MessageModel, MessageCreate](models.Message)
#
# CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)