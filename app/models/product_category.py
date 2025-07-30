from sqlmodel import Field, Relationship, SQLModel
from uuid import UUID

class Product_Category(SQLModel, table=True):
   product_id: UUID  = Field(foreign_key="product.id", primary_key=True)
   category_id: UUID = Field(foreign_key="category.id", primary_key=True)