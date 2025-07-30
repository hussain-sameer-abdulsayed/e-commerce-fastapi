from __future__ import annotations
from uuid import uuid4, UUID
from sqlmodel import Field, Relationship
from typing import Optional
from .discount_base import Discount_Base



class Shipment_Discount(Discount_Base, table=True):
   shipment_id: Optional[UUID] = Field(default=None, foreign_key="shipment.id")
   shipment : Optional["Shipment"] = Relationship(back_populates="shipment_discounts")



from .shipment import Shipment
Shipment_Discount.model_rebuild()