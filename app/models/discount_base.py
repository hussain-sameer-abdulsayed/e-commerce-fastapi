from sqlmodel import SQLModel
from sqlmodel import Field
from typing import Optional
from datetime import date, datetime
from uuid import uuid4, UUID


class Discount_Base(SQLModel, table=False):
   id: UUID = Field(default_factory=uuid4, primary_key=True, index=True)
   discount_amount: int
   is_active: bool = Field(default=True)
   start_at: date
   end_at: date
   created_at: datetime = Field(default_factory=datetime.utcnow)
   updated_at: Optional[datetime]

   @property
   def is_currently_active(self) -> bool:
      now = datetime.utcnow()
      return self.is_active and self.start_at <= now <= self.end_at
   


   