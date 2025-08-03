from __future__ import annotations
from sqlmodel import SQLModel, Field, Relationship
from typing import List, Optional
from datetime import datetime
from uuid import uuid4, UUID
from app.enums.enums import Gender



class UserProfileBase(SQLModel, table=False):
   main_image_url: str
   bio: str
   gender: Gender = Field(default=Gender.male)
   birth_date: datetime
   created_at: datetime = Field(default_factory=datetime.utcnow)
   updated_at: Optional[datetime] = None
   
   
   
   product_reviews: List["ProductReview"] = Relationship(back_populates="user_profile", cascade_delete=True)


   user_id: UUID = Field(foreign_key="users.id", index=True)
   user: "User" = Relationship(back_populates="user_profile")

   orders: List["Order"] = Relationship(back_populates="user_profile")



class UserProfile(UserProfileBase, table=True):
   __tablename__ = "user_profiles"
   id: UUID = Field(default_factory=uuid4, primary_key=True, index=True)





from app.models.product_review import ProductReview
from app.models.user import User
from app.models.order import Order
UserProfile.model_rebuild()