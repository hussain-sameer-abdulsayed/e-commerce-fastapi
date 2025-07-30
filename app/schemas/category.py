from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel
from uuid import UUID

from schemas.product import ProductRead


class CategoryBase(BaseModel):
   name: str 
   description: str
   main_image_url: Optional[str] = None
   


class CategoryCreate(CategoryBase):
   created_by_id : UUID


class CategoryUpdate(CategoryBase):
   name: Optional[str] = None
   description: Optional[str] = None
   main_image_url: Optional[str] = None


class CategoryRead(CategoryCreate):
   id: UUID
   created_at: datetime 
   updated_at : datetime
   products: Optional[List[ProductRead]] = None


   class Config:
      orm_mode = True