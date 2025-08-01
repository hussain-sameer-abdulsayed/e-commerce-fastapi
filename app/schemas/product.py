from __future__ import annotations
from datetime import datetime
from decimal import Decimal
from typing import List, Optional
from schemas import BaseSchema
from uuid import UUID



class ProductBase(BaseSchema):
   name: str
   price: Decimal
   stock_quantity: int
   description: str
   main_image_url: str
   seller_profile_id: UUID
   category_ids: List[UUID]


class ProductCreate(ProductBase):
   pass


class ProductUpdate(ProductBase):
   name: Optional[str] = None
   price: Optional[Decimal] = None
   stock_quantity: Optional[int] = None
   description: Optional[str] = None
   main_image_url: Optional[str] = None
   category_ids: Optional[List[UUID]] = None



class ProductRead(ProductBase):
   created_at: datetime
   updated_at: datetime
   is_available: bool




      