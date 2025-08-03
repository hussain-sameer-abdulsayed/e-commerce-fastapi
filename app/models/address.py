from __future__ import annotations
from sqlmodel import SQLModel, Field, Relationship
from typing import List, Optional
from datetime import datetime
from uuid import uuid4, UUID

from app.enums.enums import Province


class AddressBase(SQLModel, table=False):
   province: Province
   city: str
   street: str
   nearest_point: str | None = None
   is_default: bool = Field(default=False)
   is_store_address: bool = Field(default=False)
   is_shipment_address: bool = Field(default=True)
   created_at: datetime = Field(default_factory=datetime.utcnow)
   updated_at: Optional[datetime] = None


   orders: List["Order"]= Relationship(back_populates="address")


   user_id : Optional[UUID] = Field(default=None, foreign_key="users.id", index=True)
   user: Optional["User"] = Relationship(back_populates="addresses")


   seller_profile_id: Optional[UUID] = Field(default=None, foreign_key="seller_profiles.id", index=True)
   seller_profile: Optional["SellerProfile"] = Relationship(back_populates="addresses")
   

   
class Address(AddressBase, table=True):
   __tablename__ = "addresses"
   id: UUID = Field(default_factory=uuid4, primary_key=True, index=True)



from app.models.order import Order
from app.models.user import User
from app.models.seller_profile import SellerProfile
Address.model_rebuild()
