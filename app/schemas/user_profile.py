from __future__ import annotations
from datetime import datetime
from typing import Optional
from schemas import BaseSchema
from uuid import UUID
from models import Gender



class UserProfileBase(BaseSchema):
   main_image_url: str
   bio: str
   gender: Gender 
   birth_date: datetime

   

class UserProfileCreate(UserProfileBase):
   user_id: UUID


class UserProfileUpdate(UserProfileBase):
   main_image_url: Optional[str] = None
   bio: Optional[str] = None
   gender: Optional[Gender] = None 
   birth_date: Optional[datetime] = None



class UserProfileRead(UserProfileCreate):
   id: UUID
   created_at: datetime
   updated_at: Optional[datetime]



