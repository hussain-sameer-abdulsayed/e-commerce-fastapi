from __future__ import annotations
from datetime import datetime
from decimal import Decimal
from typing import List, Optional
from uuid import UUID
from models import Order_Status
from .base_schema import BaseSchema
from .order_item import OrderItemRead



class OrderBase(BaseSchema):
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





