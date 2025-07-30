from __future__ import annotations
from sqlmodel import Field, Relationship
from typing import Optional
from uuid import UUID

from .discount_base import Discount_Base



class Product_Discount(Discount_Base, table=True):
   product_id: UUID = Field(foreign_key="product.id")
   product : Optional["Product"] = Relationship(back_populates="product_discounts")


from .product import Product
Product_Discount.model_rebuild()