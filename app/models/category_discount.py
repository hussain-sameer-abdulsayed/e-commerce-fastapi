from __future__ import annotations
from sqlmodel import SQLModel, Field, Relationship
from typing import Optional
from uuid import UUID
from .discount_base import Discount_Base



class Category_Discount(Discount_Base, table=True):
   category_id: Optional[UUID] = Field(default=None, foreign_key="category.id")
   category : Optional["Category"] = Relationship(back_populates="category_discounts")



from .category import Category
Category_Discount.model_rebuild()