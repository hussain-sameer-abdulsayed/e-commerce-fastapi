from datetime import datetime
from sqlmodel import SQLModel, Field, Relationship
from typing import Optional
from uuid import uuid4, UUID
from models import Category, Address


class User(SQLModel, table=True):
   id: UUID = Field(default_factory=uuid4, primary_key=True, index=True)
   user_name: str = Field(index=True, unique=True)
   full_name: str
   phone_number: str
   email: str = Field(index=True)
   password_hash: str
   role: str = "client"
   categories: List["Category"] = Relationship(back_populates="user")
   ccreated_at: datetime = Field(default_factory=datetime.utcnow)
   updated_at: Optional[datetime]
   addresses: List["Address"] = Relationship(back_populates="user")
   

   