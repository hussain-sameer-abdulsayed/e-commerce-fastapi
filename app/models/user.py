from datetime import datetime
from sqlmodel import SQLModel, Field, Relationship
from typing import List, Optional
from uuid import uuid4, UUID
from models import Category, Address, Coupon_Usage


class User(SQLModel, table=True):
   id: UUID = Field(default_factory=uuid4, primary_key=True, index=True)
   user_name: str = Field(default_factory=lambda: str(uuid4()),index=True, unique=True)
   full_name: str
   phone_number: str
   email: str = Field(index=True)
   password_hash: str
   categories: Optional[List["Category"]] = Relationship(back_populates="user")
   created_at: datetime = Field(default_factory=datetime.utcnow)
   updated_at: Optional[datetime]
   addresses: Optional[List["Address"]] = Relationship(back_populates="user")
   coupon_usages: Optional[List["Coupon_Usage"]] = Relationship(back_populates="user")

   

   
   