from decimal import Decimal
from sqlmodel import SQLModel, Field, Relationship
from typing import List, Optional
from datetime import datetime
from uuid import uuid4, UUID
from models import Order_Item, Coupon, Address, Shipment, User, Order_Status
from __future__ import annotations

def generate_order_number() -> str:
    today = datetime.today()
    # Generate a 6-digit number from UUID (more unique than random)
    unique_number = str(uuid4())[-6:].zfill(6)
    return f"{today.year}-{today.month}-{today.day}-{unique_number}"



class Order(SQLModel, table=True):
   id: UUID = Field(default_factory=uuid4, primary_key=True, index=True)
   order_number: str = Field(default_factory=generate_order_number, index=True, unique=True)
   user_id : Optional[UUID] = Field(default=None, foreign_key="user.id")
   user: Optional["User"] = Relationship(back_populates="orders")
   address_id: Optional[UUID] = Field(default=None, foreign_key="address.id")
   address: Optional["Address"] = Relationship(back_populates="orders")
   ship_to_province: str
   ship_to_city: str
   ship_to_street: str
   ship_to_contact: str
   coupon_id: Optional[UUID] = Field(default=None, foreign_key="coupon.id")
   coupon: Optional["Coupon"] = Relationship(back_populates="orders")
   coupon_amount: Optional[Decimal] = None
   sub_total: Decimal
   shipping_cost: Decimal
   total: Decimal
   shipment_id: Optional[UUID] = Field(default=None, foreign_key="shipment.id")
   shipment: Optional["Shipment"] = Relationship(back_populates="order")
   order_items: Optional[List["Order_Item"]] = Relationship(back_populates="order")
   status: Order_Status = Field(default=Order_Status.pending)
   created_at: datetime = Field(default_factory=datetime.utcnow)
   updated_at: Optional[datetime]



   