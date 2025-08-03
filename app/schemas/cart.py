from __future__ import annotations
from datetime import datetime
from decimal import Decimal
from typing import List, Optional
from uuid import UUID
from .base_schema import BaseSchema
from .cartitem import CartItemRead



class CartBase(BaseSchema):
   user_id: UUID


class CartCreate(CartBase):
   pass


class CartRead(CartBase):
   id: UUID
   items: Optional[List["CartItemRead"]] = None
   total: Decimal
   coupon_id: Optional[UUID] = None
   coupon_amount: Optional[Decimal]  = None
   created_at: datetime
   updated_at: Optional[datetime] = None