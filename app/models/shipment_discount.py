from __future__ import annotations
from uuid import uuid4, UUID
from sqlmodel import Field, Relationship

from app.models.discount_base import DiscountBase




class ShipmentDiscount(DiscountBase, table=True):
   __tablename__ = "shipment_discounts"
   shipment_id: UUID = Field(foreign_key="shipments.id", index=True)
   shipment : "Shipment" = Relationship(back_populates="shipment_discounts")



from app.models.shipment import Shipment
ShipmentDiscount.model_rebuild()