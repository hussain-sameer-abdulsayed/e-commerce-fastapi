from datetime import datetime
from decimal import Decimal
from typing import List, Optional
from pydantic import BaseModel
from uuid import UUID
from models.enums import Order_Status
from schemas.order_item import OrderItemCreate, OrderItemRead
from __future__ import annotations


class OrderBase(BaseModel):
   address_id: UUID
   ship_to_province: str
   ship_to_city: str
   ship_to_street: str
   ship_to_contact: str
   shipment_id: UUID


class OrderCreate(OrderBase):
   user_id : UUID
   coupon_id: Optional[UUID] = None



class OrderUpdate(OrderBase):
   pass


class OrderRead(OrderCreate):
   id: UUID
   order_number: str
   coupon_amount: Optional[Decimal] = None
   sub_total: Decimal
   shipping_cost: Decimal
   total: Decimal
   order_items: List["OrderItemRead"]
   status: Order_Status
   created_at: datetime
   updated_at: Optional[datetime]




   class Config:
      orm_mode: True