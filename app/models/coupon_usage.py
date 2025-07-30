from datetime import datetime
from sqlmodel import SQLModel, Field, Relationship
from typing import Optional
from uuid import uuid4, UUID
from models import User, Coupon


class Coupon_Usage(SQLModel, table=True):
   id: UUID = Field(default_factory=uuid4, primary_key=True, index=True)
   user_id: Optional[UUID] = Field(default=None, foreign_key="user.id")
   user: Optional["User"] = Relationship(back_populates="user")
   coupon_id: UUID = Field(default=None, foreign_key="coupon.id")
   coupon: Optional["Coupon"] = Relationship(back_populates="coupon_usages")
   used_at: datetime = Field(default_factory=datetime.utcnow)


   