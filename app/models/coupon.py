from __future__ import annotations
from decimal import Decimal
from sqlmodel import SQLModel, Field, Relationship
from datetime import datetime
from typing import List, Optional
from uuid import uuid4, UUID




class CouponBase(SQLModel, table=False):
   code: str = Field(default_factory=lambda: str(uuid4()), index=True, unique=True)
   discount_amount: Decimal
   min_order_amount: Decimal
   max_uses: int
   used_count: int = Field(default=0)
   start_at: datetime = Field(index=True)
   end_at: datetime = Field(index=True)
   is_active: bool = Field(default=True, index=True)
   created_at: datetime = Field(default_factory=datetime.utcnow)
   updated_at: Optional[datetime] = None



   @property
   def is_currently_active(self):
      now = datetime.utcnow()
      return self.is_active and self.used_count < self.max_uses and self.start_at <= now <= self.end_at



   coupon_usages: List["CouponUsage"] = Relationship(back_populates="coupon", cascade_delete=True)
   
   orders: List["Order"] = Relationship(back_populates="coupon")

   carts: List["Cart"] = Relationship(back_populates="coupon")




class Coupon(CouponBase, table=True):
   __tablename__ = "coupons"
   id: UUID = Field(default_factory=uuid4, primary_key=True, index=True)



from app.models.cart import Cart
from app.models.coupon_usage import CouponUsage
from app.models.order import Order
Coupon.model_rebuild()