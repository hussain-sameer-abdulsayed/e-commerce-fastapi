from __future__ import annotations
from datetime import datetime
from typing import List, Optional
from sqlmodel import Field, SQLModel, Relationship
from uuid import uuid4, UUID



class Seller_Profile(SQLModel, table=True):
   id: UUID = Field(default_factory=uuid4, primary_key=True, index=True)
   user_id: Optional[UUID] = Field(default=None, foreign_key="user.id")
   user: Optional["User"] = Relationship(back_populates="seller_profile")
   store_name: str
   store_description: str
   main_image_url: str
   store_phone_number: str
   is_verified: bool = Field(default=False)
   is_active: bool = Field(default=True)
   created_at: datetime = Field(default_factory=datetime.utcnow)
   updated_at: Optional[datetime]
   addresses: List["Address"] = Relationship(back_populates="seller_profile")



from .user import User
from .address import Address
Seller_Profile.model_rebuild()