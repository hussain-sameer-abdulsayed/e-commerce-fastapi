from __future__ import annotations
from datetime import datetime
from decimal import Decimal
from typing import Optional
from .base_schema import BaseSchema
from uuid import UUID


class OrderItemBase(BaseSchema):
   product_id: UUID
   quantity: int
   

class OrderItemCreate(OrderItemBase):
   order_id: UUID


class OrderItemUpdate(OrderItemBase): ##send orderid in req. header
   pass


class OrderItemRead(OrderItemCreate):
   id: UUID
   unit_price: Decimal
   created_at: datetime
   updated_at: Optional[datetime] = None
   sub_total: Decimal


