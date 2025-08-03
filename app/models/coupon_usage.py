from __future__ import annotations
from datetime import datetime
from sqlmodel import SQLModel, Field, Relationship
from uuid import uuid4, UUID



class CouponUsageBase(SQLModel, table=False):
   __tablename__ = "coupon_usages"
   id: UUID = Field(default_factory=uuid4, primary_key=True, index=True)
   used_at: datetime = Field(default_factory=datetime.utcnow)


   user_id: UUID = Field(foreign_key="users.id", index=True)
   user: "User" = Relationship(back_populates="coupon_usages")


   coupon_id: UUID = Field(foreign_key="coupons.id", index=True)
   coupon: "Coupon" = Relationship(back_populates="coupon_usages")



class CouponUsage(CouponUsageBase, table=True):
   __tablename__ = "coupon_usages"
   id: UUID = Field(default_factory=uuid4, primary_key=True, index=True)



from app.models.user import User
from app.models.coupon import Coupon
CouponUsage.model_rebuild()