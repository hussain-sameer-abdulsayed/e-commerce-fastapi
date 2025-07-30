from decimal import Decimal
from sqlmodel import SQLModel, Field, Relationship
from datetime import datetime
from typing import Optional
from uuid import uuid4, UUID
from models import User, Coupon, Cart_Item



class Cart(SQLModel, table=True):
   id: UUID = Field(default_factory=uuid4, primary_key=True, index=True)
   user_id: Optional[UUID] = Field(default=None, foreign_key="user.id")
   user: Optional["User"] = Relationship(back_populates="cart")
   items: Optional[List["Cart_Item"]] = Relationship(back_populates="cart")
   total: Decimal | None = None
   coupon_id: UUID = Field(default=None, foreign_key="coupon.id")
   coupon: Optional["Coupon"] = Relationship(back_populates="cart")
   coupon_amount: Decimal | None = None
   created_at: datetime = Field(default_factory=datetime.utcnow)


