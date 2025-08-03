from __future__ import annotations
from datetime import datetime
from sqlmodel import SQLModel, Field, Relationship
from typing import List, Optional
from uuid import uuid4, UUID
from decimal import Decimal
from app.models.product_category import ProductCategoryLink


class ProductBase(SQLModel, table=False):
    name: str = Field(index=True)
    price: Decimal
    stock_quantity: int = Field(default=0)
    description: str
    main_image_url: str
    
    
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: Optional[datetime] = None


    @property
    def is_available(self) -> bool:
        return self.stock_quantity > 0
    

    
    product_reviews: List["ProductReview"] = Relationship(back_populates="product", cascade_delete=True)
    
    
    
    categories: List["Category"] = Relationship(back_populates="products", link_model=ProductCategoryLink)
    

    seller_profile_id: UUID = Field(foreign_key="seller_profiles.id", index=True)
    seller_profile: "SellerProfile" = Relationship(back_populates="products")
    


    order_items: List["OrderItem"] = Relationship(back_populates="product")


    cart_items: List["CartItem"] = Relationship(back_populates="product", cascade_delete=True)


    product_discounts: List["ProductDiscount"] = Relationship(back_populates="product")
    
    
    # @property
    # def current_price(self) -> Decimal:
    #     active_discount = [d for d in self.product_discounts if d.is_active]

    #     if active_discount:
    #         return self.price - active_discount.discount_amount
    #     return self.price



class Product(ProductBase, table=True):
    __tablename__ = "products"
    id: UUID = Field(default_factory=uuid4, primary_key=True, index=True)




from app.models.product_review import ProductReview
from app.models.category import Category
from app.models.seller_profile import SellerProfile
from app.models.order_item import OrderItem
from app.models.product_discount import ProductDiscount
Product.model_rebuild()