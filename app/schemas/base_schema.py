from pydantic import BaseModel
from decimal import Decimal

class BaseSchema(BaseModel):
    class Config:
        orm_mode = True
        arbitrary_types_allowed = True
        json_encoders = {
            Decimal: lambda x: float(round(x, 2)),
        }
