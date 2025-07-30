from datetime import datetime
from decimal import Decimal
from typing import List, Optional
from pydantic import BaseModel
from uuid import UUID


class CartItemBase(BaseModel):
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


   class Config:
      orm_mode = True