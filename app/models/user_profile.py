from sqlmodel import SQLModel, Field, Relationship
from typing import Optional
from datetime import date, datetime
from uuid import uuid4, UUID
from models import User, Gender




class User_Profile(SQLModel, table=True):
   id: UUID = Field(default_factory=uuid4, primary_key=True, index=True)
   user_id: Optional[str] = Field(default=None, foreign_key="user.id")
   user: Optional["User"] = Relationship(back_populates="user_profile")
   main_image_url: str
   bio: str
   gender: Gender = Field(default=Gender.male)
   birth_date: datetime
   created_at: datetime = Field(default_factory=datetime.utcnow)
   updated_at: Optional[datetime]



   