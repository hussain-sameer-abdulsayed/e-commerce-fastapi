from pydantic import BaseModel
from decimal import Decimal

class BaseSchema(BaseModel):
    class Config:
        from_attributes = True  # Updated from orm_mode
        arbitrary_types_allowed = True
        json_encoders = {
            Decimal: lambda x: float(round(x, 2)),
        }