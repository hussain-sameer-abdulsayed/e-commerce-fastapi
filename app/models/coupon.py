from decimal import Decimal
from sqlmodel import SQLModel, Field, Relationship
from datetime import datetime
from typing import List, Optional
from uuid import uuid4, UUID
from models import Coupon_Usage


class Coupon(SQLModel, table=True):
   id: UUID = Field(default_factory=uuid4, primary_key=True, index=True)
   code: str = Field(default_factory=lambda: str(uuid4()), index=True, unique=True)
   discount_type: Discount_Type
   discount_amount: Decimal
   min_order_amount: Decimal
   max_uses: int
   used_count: int
   start_at: datetime
   end_at: datetime
   is_active: bool = Field(default=True)
   coupon_usages: Optional[List[Coupon_Usage]] = Relationship(back_populates="coupon")
   created_at: datetime = Field(default_factory=datetime.utcnow)
   updated_at: Optional[datetime]



   @property
   def is_currently_active(self):
      now = datetime.utcnow()
      return self.is_active and self.start_at <= now <= self.end_at
   


   