from __future__ import annotations
from datetime import datetime
from uuid import UUID
from schemas import BaseSchema


class CouponUsageBase(BaseSchema):
   user_id: UUID
   coupon_id: UUID


class CouponUsageCreate(CouponUsageBase):
   pass


class CouponUsageRead(CouponUsageBase):
   id: UUID
   used_at: datetime

