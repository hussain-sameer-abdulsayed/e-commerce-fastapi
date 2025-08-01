from __future__ import annotations
from datetime import datetime
from typing import Optional
from schemas import BaseSchema
from uuid import UUID
from models import Province



class AddressBase(BaseSchema):
   province: Province
   city: str
   street: str
   nearest_point: Optional[str] = None
   is_default: bool
   is_store_address: bool
   is_shipment_address: bool


class AddressCreate(AddressBase):
   pass


class AddressUpdate(AddressBase):
   province: Optional[Province] = None
   city: Optional[str] = None
   street: Optional[str] = None
   nearest_point: Optional[str] = None
   is_default: Optional[bool] = None
   is_store_address: Optional[bool] = None
   is_shipment_address: Optional[bool] = None


class AddressRead(AddressBase):
   id: UUID
   user_id : Optional[UUID] = None
   seller_profile_id: Optional[UUID] = None
   created_at: datetime
   updated_at: datetime



