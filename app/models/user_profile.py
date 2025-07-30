from __future__ import annotations
from sqlmodel import SQLModel, Field, Relationship
from typing import List, Optional
from datetime import datetime
from uuid import uuid4, UUID

from .enums import Gender




class User_Profile(SQLModel, table=True):
   id: UUID = Field(default_factory=uuid4, primary_key=True, index=True)
   user_id: Optional[UUID] = Field(default=None, foreign_key="user.id")
   user: Optional["User"] = Relationship(back_populates="user_profile")
   main_image_url: str
   bio: str
   gender: Gender = Field(default=Gender.male)
   birth_date: datetime
   created_at: datetime = Field(default_factory=datetime.utcnow)
   updated_at: Optional[datetime]
   product_reviews: Optional[List["Product_Review"]] = Relationship(back_populates="user_profile")




from .user import User
from .product_review import Product_Review
User_Profile.model_rebuild()