from datetime import datetime
from sqlmodel import SQLModel, Field, Relationship
from typing import Optional
from uuid import uuid4, UUID
from models import User_Profile, Product


class Product_Review(SQLModel, table=True):
   id: UUID = Field(default_factory=uuid4, primary_key=True, index=True)
   user_profile_id: Optional[UUID] = Field(default=None, foreign_key="user_profile.id")
   user_profile: Optional["User_Profile"] = Relationship(back_populates="product_reviews")
   product_id: Optional[UUID] = Field(default=None, foreign_key="product.id")
   product: Optional["Product"] = Relationship(back_populates="product_reviews")
   rating: int
   comment: Optional[str] = None
   is_approved: bool = Field(default=False)
   created_at: datetime = Field(default_factory=datetime.utcnow)
   updated_at: Optional[datetime] = None



