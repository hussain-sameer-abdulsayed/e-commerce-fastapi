from __future__ import annotations
from datetime import datetime
from typing import Optional
from schemas import BaseSchema
from uuid import UUID




class SellerProfileBase(BaseSchema):
   store_name: str
   store_description: str
   main_image_url: str
   store_phone_number: str


class SellerProfileCreate(SellerProfileBase):
   user_id: UUID



class SellerProfileUpdate(SellerProfileBase):
   store_name: Optional[str] = None
   store_description: Optional[str] = None
   main_image_url: Optional[str] = None
   store_phone_number: Optional[str] = None


class SellerProfileRead(SellerProfileCreate):
   id: UUID
   is_verified: bool
   is_active: bool
   created_at: datetime
   updated_at: Optional[datetime]



