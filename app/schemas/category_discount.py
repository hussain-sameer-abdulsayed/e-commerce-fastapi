from __future__ import annotations
from datetime import datetime
from decimal import Decimal
from typing import Optional
from uuid import UUID
from .base_schema import BaseSchema


class CategoryDiscountBase(BaseSchema):
   category_id: UUID
   discount_amount: Decimal
   is_active: bool
   start_at: datetime
   end_at: datetime


class CategoryDiscountCreate(CategoryDiscountBase):
   pass


class CategoryDiscountUpdate(CategoryDiscountBase):
   category_id: Optional[UUID] = None
   discount_amount: Optional[int] = None
   is_active: Optional[bool] = None
   start_at: Optional[datetime] = None
   end_at: Optional[datetime] = None


class CategoryDiscountRead(CategoryDiscountBase):
   id: UUID
   created_at: datetime
   updated_at: Optional[datetime] = None
   is_currently_active: bool


      