from __future__ import annotations
from datetime import datetime
from decimal import Decimal
from sqlmodel import SQLModel, Field, Relationship
from typing import Optional
from uuid import uuid4, UUID


class CartItemBase(SQLModel, table=False):
   quantity: int = Field(gt=0)
   unit_price: Decimal = Field(gt=0)
   created_at: datetime = Field(default_factory=datetime.utcnow)
   updated_at: Optional[datetime] = None


   cart_id: UUID = Field(foreign_key="carts.id", index=True)
   cart: "Cart" =  Relationship(back_populates="cart_items")


   product_id: UUID = Field(foreign_key="products.id", index=True)
   product: "Product" = Relationship(back_populates="cart_items")

   @property
   def total(self) -> Decimal:
      return self.unit_price * self.quantity



class CartItem(CartItemBase, table=True):
   __tablename__ = "cart_items"
   id: UUID = Field(default_factory=uuid4, primary_key=True, index=True)
   


from app.models.cart import Cart
from app.models.product import Product
CartItem.model_rebuild()
