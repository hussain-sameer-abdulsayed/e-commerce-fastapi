from sqlmodel import SQLModel, Field, Relationship
from typing import Optional
from uuid import UUID
from models import Category


class Category_Discount(SQLModel, DiscountBase):
   category_id: Optional[UUID] = Field(default=None, foreign_key="category.id")
   category : Optional["Category"] = Relationship(back_populates="category_discounts")



   