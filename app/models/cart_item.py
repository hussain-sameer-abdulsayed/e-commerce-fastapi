from datetime import date, datetime
from decimal import Decimal
from sqlmodel import SQLModel, Field, Relationship
from typing import Optional
from uuid import uuid4, UUID
from models import Cart, Product


class Cart_Item(SQLModel, table=True):
   id: UUID = Field(default_factory=uuid4, primary_key=True, index=True)
   cart_id: Optional[UUID] = Field(default=None, foreign_key="cart.id")
   cart: Optional["Cart"] =  Relationship(back_populates="cart_items")
   product_id: Optional[UUID] = Field(default=None, foreign_key="product.id")
   product: Optional["Product"] = Relationship(back_populates="cart_item")
   quantity: int
   unit_price: Decimal
   total: Decimal
   created_at: datetime = Field(default_factory=datetime.utcnow)
   updated_at: Optional[datetime]


