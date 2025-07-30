from sqlmodel import SQLModel, Field, Relationship
from typing import Optional
from datetime import datetime
from uuid import uuid4, UUID
from models import User, Province, Seller_Profile





class Address(SQLModel, table=True):
   id: UUID = Field(default_factory=uuid4, primary_key=True, index=True)
   user_id : Optional[UUID] = Field(default=None, foreign_key="user.id")
   user: Optional["User"] = Relationship(back_populates="addresses")
   seller_profile_id: Optional[UUID] = Field(default=None, foreign_key="seller_profile.id")
   seller_profile: Optional["Seller_Profile"] = Relationship(back_populates="addresses")
   province: Province
   city: str
   street: str
   nearest_point: str | None = None
   is_default: bool = Field(default=False)
   is_store_address: bool = Field(default=False)
   is_shipment_address: bool = Field(default=True)
   created_at: datetime = Field(default_factory=datetime.utcnow)
   updated_at: Optional[datetime]




