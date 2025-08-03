from __future__ import annotations
from datetime import datetime
from decimal import Decimal
from typing import Optional
from uuid import UUID
from .base_schema import BaseSchema



class CouponBase(BaseSchema):
   discount_amount: int
   min_order_amount: Decimal
   max_uses: int
   used_count: int
   start_at: datetime
   end_at: datetime
   is_active: bool


class CouponCreate(CouponBase):
   pass


class CouponUpdate(CouponBase):
   discount_amount: Optional[int] = None
   min_order_amount: Optional[Decimal] = None
   max_uses: Optional[int] = None
   used_count: Optional[int] = None
   start_at: Optional[datetime] = None
   end_at: Optional[datetime] = None
   is_active: Optional[bool] = None


class CouponRead(CouponBase):
   id: UUID
   code: str
   is_currently_active: bool
   created_at: datetime
   updated_at: Optional[datetime]




      