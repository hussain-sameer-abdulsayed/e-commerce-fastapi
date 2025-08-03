from __future__ import annotations
from datetime import datetime
from decimal import Decimal
from typing import Optional
from .base_schema import BaseSchema
from uuid import UUID


class ShipmentDiscountBase(BaseSchema):
   shipment_id: UUID
   discount_amount: Decimal
   is_active: bool
   start_at: datetime
   end_at: datetime


class ShipmentDiscountCreate(ShipmentDiscountBase):
   pass


class ShipmentDiscountUpdate(ShipmentDiscountBase):
   shipment_id: Optional[UUID] = None
   discount_amount: Optional[int] = None
   is_active: Optional[bool] = None
   start_at: Optional[datetime] = None
   end_at: Optional[datetime] = None


class ShipmentDiscountRead(ShipmentDiscountBase):
   id: UUID
   created_at: datetime
   updated_at: Optional[datetime] = None
   is_currently_active: bool