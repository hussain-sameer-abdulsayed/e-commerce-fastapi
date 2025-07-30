from decimal import Decimal
from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime
from uuid import uuid4, UUID
from models import Province



class Shipment(SQLModel, table=True):
   id: UUID = Field(default_factory=uuid4, primary_key=True, index=True)
   province: Province = Field(default=Province.baghdad)
   cost: Decimal 
   created_at: datetime = Field(default_factory=datetime.utcnow)
   updated_at: Optional[datetime]


