from __future__ import annotations
from datetime import datetime
from typing import Optional
from pydantic import Field
from .base_schema import BaseSchema
from uuid import UUID





class UserBase(BaseSchema):
   full_name: str
   phone_number: str
   email: str


class UserCreate(UserBase):
   password: str = Field(min_length=6)


class UserUpdate(UserBase):
   full_name: Optional[str] = None
   phone_number: Optional[str] = None
   email: Optional[str] = None


class UserRead(UserBase):
   id: UUID
   user_name: str
   created_at: datetime
   updated_at: Optional[datetime]


