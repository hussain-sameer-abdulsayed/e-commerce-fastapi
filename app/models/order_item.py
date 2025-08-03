from __future__ import annotations
from decimal import Decimal
from sqlmodel import SQLModel, Field, Relationship
from datetime import datetime
from typing import Optional
from uuid import uuid4, UUID


class OrderItemBase(SQLModel, table=False):
   
   quantity: int
   unit_price: Decimal
   created_at: datetime = Field(default_factory=datetime.utcnow)
   updated_at: Optional[datetime] = None

  
   @property
   def sub_total(self) -> Decimal:
      return self.unit_price * self.quantity
   

   product_id: UUID = Field(foreign_key="products.id")
   product: "Product" = Relationship(back_populates="order_items")

   
   order_id: Optional[UUID] = Field(default=None, foreign_key="orders.id", index=True)
   order: Optional["Order"] = Relationship(back_populates="order_items")





class OrderItem(OrderItemBase, table=True):
   __tablename__ = "order_items"
   id: UUID = Field(default_factory=uuid4, primary_key=True, index=True)




from app.models.product import Product
from app.models.order import Order
OrderItem.model_rebuild()