from fastapi import FastAPI
from sqlmodel import SQLModel
from database import engine
from app.routers import category_router  # Adjust based on your router imports
from app.models import address, cart_item, cart, category_discount, category, coupon_usage, coupon, order_item, order, product_category, product_discount, product_review, product, seller_profile, shipment_discount, shipment, user_profile, user

app = FastAPI(title="E-Commerce FastAPI", version="1.0.0")






app.include_router(category_router.router)



@app.on_event("startup")
async def on_startup():
   async with engine.begin() as conn:
      await conn.run_sync(SQLModel.metadata.create_all) 

