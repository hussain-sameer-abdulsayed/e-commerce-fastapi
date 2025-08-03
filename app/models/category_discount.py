from __future__ import annotations
from sqlmodel import SQLModel, Field, Relationship
from typing import Optional
from uuid import UUID
from app.models.discount_base import DiscountBase



class CategoryDiscount(DiscountBase):
   __tablename__ = "category_discounts"
   category_id: UUID = Field(foreign_key="categories.id", index=True)
   category : "Category" = Relationship(back_populates="category_discounts")




from app.models.category import Category
CategoryDiscount.model_rebuild()
