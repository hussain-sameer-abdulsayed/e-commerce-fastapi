from __future__ import annotations
from decimal import Decimal
from sqlmodel import SQLModel, Field, Relationship
from typing import List, Optional
from datetime import datetime
from uuid import uuid4, UUID
from app.enums.enums import Order_Status



def generate_order_number() -> str:
    today = datetime.today()
    # Generate a 6-digit number from UUID (more unique than random)
    unique_number = str(uuid4())[-6:].zfill(6)
    return f"{today.year}-{today.month}-{today.day}-{unique_number}"



class OrderBase(SQLModel, table=False):
   order_number: str = Field(default_factory=generate_order_number, index=True, unique=True)

   ship_to_province: str
   ship_to_city: str
   ship_to_street: str
   ship_to_contact: str
   
   coupon_amount: Optional[Decimal] = None

   sub_total: Decimal
   shipping_cost: Decimal
   total: Decimal
   
   status: Order_Status = Field(default=Order_Status.pending)
   created_at: datetime = Field(default_factory=datetime.utcnow)
   updated_at: Optional[datetime] = None



   coupon_id: Optional[UUID] = Field(default=None, foreign_key="coupons.id")
   coupon: Optional["Coupon"] = Relationship(back_populates="orders")


   shipment_id: UUID = Field(foreign_key="shipments.id")
   shipment: "Shipment" = Relationship(back_populates="orders")      


   user_profile_id: UUID = Field(foreign_key="user_profiles.id", index=True)
   user_profile: "UserProfile" = Relationship(back_populates="orders")


   address_id: UUID = Field(foreign_key="addresses.id")
   address: "Address" = Relationship(back_populates="orders")


   
   order_items: List["OrderItem"] = Relationship(back_populates="order", cascade_delete=True)


   @property
   def set_total(self) -> Decimal:
       if self.coupon_amount:
           return self.sub_total + self.shipping_cost - self.coupon_amount
       return self.sub_total + self.shipping_cost








class Order(OrderBase, table=True):
   __tablename__ = "orders"
   id: UUID = Field(default_factory=uuid4, primary_key=True, index=True)


from app.models.coupon import Coupon
from app.models.shipment import Shipment
from app.models.user_profile import UserProfile
from app.models.address import Address
from app.models.order_item import OrderItem
Order.model_rebuild()