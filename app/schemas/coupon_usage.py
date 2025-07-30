from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel
from uuid import UUID


class CouponUsageBase(BaseModel):
   user_id: UUID
   coupon_id: UUID


class CouponUsageCreate(CouponUsageBase):
   pass


class CouponUsageRead(CouponUsageBase):
   id: UUID
   used_at: datetime


   class Config:
      orm_mode = True