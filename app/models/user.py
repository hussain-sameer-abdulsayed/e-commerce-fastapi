from __future__ import annotations
from datetime import datetime
from sqlmodel import Relationship, SQLModel, Field
from typing import List, Optional
from uuid import uuid4, UUID





class UserBase(SQLModel, table=False):
   user_name: str = Field(default_factory=lambda: str(uuid4()),index=True, unique=True)
   full_name: str
   phone_number: str
   email: str = Field(index=True)
   password_hash: str
   
   created_at: datetime = Field(default_factory=datetime.utcnow)
   updated_at: Optional[datetime] = None
   
   
   
   
   addresses: List["Address"] = Relationship(back_populates="user", cascade_delete=True)
   
   
   coupon_usages: List["CouponUsage"] = Relationship(back_populates="user", cascade_delete=True)
   
   
   # cart_id: Optional[UUID] = Field(default=None, foreign_key="carts.id", index=True)
   cart: Optional["Cart"] = Relationship(back_populates="user", cascade_delete=True)
  
   
   # seller_profile_id: Optional[UUID] = Field(default=None, foreign_key="seller_profiles.id", index=True)
   seller_profile: Optional["SellerProfile"] = Relationship(back_populates="user",cascade_delete=True)
   
   
   # user_profile_id: Optional[UUID] = Field(default=None, foreign_key="user_profiles.id", index=True)
   user_profile: Optional["UserProfile"] = Relationship(back_populates="user", cascade_delete=True)


   categories: List["Category"] = Relationship(back_populates="user")






class User(UserBase, table=True):
   __tablename__ = "users"
   id: UUID = Field(default_factory=uuid4, primary_key=True, index=True)




from app.models.address import Address
from app.models.coupon_usage import CouponUsage
from app.models.cart import Cart
from app.models.user_profile import UserProfile
from app.models.category import Category
User.model_rebuild()
