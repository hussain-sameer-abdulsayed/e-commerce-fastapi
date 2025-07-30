from decimal import Decimal
from sqlmodel import SQLModel, Field, Relationship
from datetime import datetime
from typing import Optional
from uuid import uuid4, UUID
from models import Order, Product



class Order_Item(SQLModel, table=True):
   id: UUID = Field(default_factory=uuid4, primary_key=True, index=True)
   order_id: UUID = Field(foreign_key="order.id", index=True)
   order: Optional["Order"] = Relationship(back_populates="order_items")
   product_id: UUID = Field(foreign_key="product.id")
   product: Optional["Product"] = Relationship(back_populates="order_item")
   quantity: int
   unit_price: Decimal
   created_at: datetime = Field(default_factory=datetime.utcnow)
   updated_at: Optional[datetime] = None


   @property
   def sub_total(self) -> Decimal:
      return self.unit_price * self.quantity
   

   