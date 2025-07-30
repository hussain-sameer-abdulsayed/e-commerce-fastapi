from sqlmodel import Field, Relationship
from typing import Optional
from uuid import UUID
from models import Discount_Base, Product


class Product_Discount(Discount_Base, table=True):
   product_id: UUID = Field(foreign_key="product.id")
   product : Optional["Product"] = Relationship(back_populates="product_discounts")



   