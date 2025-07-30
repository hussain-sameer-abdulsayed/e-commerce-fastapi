from sqlmodel import Field, Relationship
from typing import Optional

from models import Discount_Base, Shipment


class Shipment_Discount(Discount_Base):
   shipment_id: Optional[str] = Field(default=None, foreign_key="shipment.id")
   shipment : Optional["Shipment"] = Relationship(back_populates="shipment_discounts")


   