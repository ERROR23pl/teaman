from typing import Optional

from pydantic import BaseModel, EmailStr, constr


# testing schemas

class UserBase(BaseModel):
    email: EmailStr
    username: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool

    class Config:
        from_attributes = True


class UserInDB(User):
    hashed_password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class UserUpdate(BaseModel):
    email: Optional[EmailStr] = None
    username: Optional[constr(min_length=3, max_length=50)] = None
    password: Optional[constr(min_length=8)] = None
    is_active: Optional[bool] = None

    def model_dump(self, exclude_unset: bool = True, exclude_none: bool = True):
        """
        Creates a dictionary of non-None values for updating user.

        Args:
            exclude_unset: If True, excludes fields that weren't explicitly set
            exclude_none: If True, excludes fields that are None

        Returns:
            dict: Dictionary with only the fields that should be updated
        """
        # Get all values that were explicitly set
        data = super().model_dump(
            exclude_unset=exclude_unset,
            exclude_none=exclude_none
        )

        return data
