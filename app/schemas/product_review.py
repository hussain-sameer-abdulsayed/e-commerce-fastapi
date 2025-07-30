from __future__ import annotations
from datetime import datetime
from typing import Optional
from schemas import BaseSchema
from uuid import UUID



class ProductReviewBase(BaseSchema):
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





      