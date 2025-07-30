from __future__ import annotations
from datetime import datetime
from sqlmodel import SQLModel, Field, Relationship
from typing import List, Optional
from uuid import uuid4, UUID
from .product_category import Product_Category


class Category(SQLModel, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True, index=True)
    name: str = Field(index=True)
    description: str
    main_image_url: Optional[str]
    created_by_id: Optional[UUID] = Field(default=None, foreign_key="user.id")

    user: Optional["User"] = Relationship(back_populates="categories")
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: Optional[datetime]

    products: Optional[List["Product"]] = Relationship(
        back_populates="categories", link_model=Product_Category
    )
    category_discounts: Optional[List["Category_Discount"]] = Relationship(
        back_populates="category"
    )



from .product import Product
from .user import User
from .category_discount import Category_Discount

Category.model_rebuild()
