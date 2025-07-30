from datetime import datetime
from decimal import Decimal
from typing import List, Optional
from pydantic import BaseModel
from uuid import UUID

from schemas.cartitem import CartItemRead



class CartBase(BaseModel):
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


   class Config:
      orm_mode = True