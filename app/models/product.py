from datetime import datetime
from sqlmodel import SQLModel, Field, Relationship
from typing import List, Optional
from uuid import uuid4, UUID
from decimal import Decimal


from models import Seller_Profile, Product_Review, Category, Product_Category, Order_Item


class Product(SQLModel, table=True):
   id: UUID = Field(default_factory=uuid4, primary_key=True, index=True)
   name: str = Field(index=True)
   price: Decimal
   stock_quantity: int
   description: str
   main_image_url: str ## check it if string or not
   seller_profile_id: Optional[UUID] = Field(default=None, foreign_key="seller_profile.id")
   seller_profile: Optional["Seller_Profile"] = Relationship(back_populates="products")
   created_at: datetime = Field(default_factory=datetime.utcnow)
   updated_at: Optional[datetime]
   reviews: List[Product_Review] = Relationship(back_populates="product")
   categories: List["Category"] = Relationship(back_populates="products", link_model=Product_Category)
   order_items: Optional[List["Order_Item"]] = Relationship(back_populates="product")



   @property
   def is_available(self) -> bool:
      return self.stock_quantity > 0


