from datetime import datetime
from decimal import Decimal
from typing import Optional
from pydantic import BaseModel
from uuid import UUID
from models import Province



class ShipmentBase(BaseModel):
   province: Province
   cost: Decimal 
   

class ShipmentCreate(ShipmentBase):
   pass


class ShipmentUpdate(ShipmentBase):
   province: Optional[Province] = None
   cost: Optional[Decimal] = None 


class ShipmentRead(ShipmentBase):
   id: UUID
   province: Province
   cost: Decimal 
   created_at: datetime
   updated_at: datetime



   
   class Config:
      orm_mode = True