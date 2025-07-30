from __future__ import annotations
from datetime import datetime
from decimal import Decimal
from typing import Optional
from uuid import UUID
from schemas import BaseSchema


class CartItemBase(BaseSchema):
   quantity: int
   product_id: UUID

class CartItemCreate(CartItemBase):
   pass


class CartItemUpdate(CartItemBase):
   pass


class CartItemRead(CartItemBase):
   id: UUID
   order_id: UUID
   unit_price: Decimal
   sub_total: Decimal
   created_at: datetime
   updated_at: Optional[datetime] = None

