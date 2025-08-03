
from __future__ import annotations
from datetime import datetime
from sqlmodel import SQLModel, Field, Relationship
from typing import List, Optional
from uuid import uuid4, UUID

from app.models.product_category import ProductCategoryLink


class CategoryBase(SQLModel, table=False):
    name: str = Field(index=True)
    description: str
    main_image_url: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: Optional[datetime] = None
    


    # Relationships
    created_by_id: UUID = Field(default=None, foreign_key="users.id")
    user: "User" = Relationship(back_populates="categories")
    

    products: List["Product"] = Relationship(back_populates="categories", link_model=ProductCategoryLink, cascade_delete=True)
    
    
    category_discounts: List["CategoryDiscount"] = Relationship(
        back_populates="category", cascade_delete=True)
    



class Category(CategoryBase, table=True):
    __tablename__ = "categories"
    id: UUID = Field(default_factory=uuid4, primary_key=True, index=True)



from app.models.category_discount import CategoryDiscount
from app.models.user import User
from app.models.product import Product
Category.model_rebuild()
