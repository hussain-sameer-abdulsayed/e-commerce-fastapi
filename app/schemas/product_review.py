from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from uuid import UUID



class ProductReviewBase(BaseModel):
   product_id: UUID
   rating: int
   comment: Optional[str] = None



class ProductReviewCreate(ProductReviewBase):
   user_profile_id: UUID



class ProductReviewUpdate(ProductReviewBase):
   rating : Optional[int] = None


class ProductReviewRead(ProductReviewCreate):
   id: UUID
   is_approved: bool
   created_at: datetime
   updated_at: Optional[datetime] = None


   class Config:
      orm_mode: True