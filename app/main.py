from fastapi import FastAPI, HTTPException, Path, Query, Depends
from models import ProductsList, CategoryCreate, Category, Product
from typing import Annotated
from sqlmodel import Session, select
from database import init_db, get_session



app = FastAPI()



@app.get('/categories')
async def categories(
    name : str | None = None,
    q: Annotated[str | None, Query(max_length=10)] = None,
    session: Session = Depends(get_session)
) -> list[Category]:
   
   category_list = session.exec(select(Category)).all()

   if name:
    category_list = [p for p in category_list if p.name.lower() == name.lower()]


   if q:
       category_list =[
           p for p in category_list if q.lower() in p.name.value.lower()
       ] 
   return category_list


@app.get('/categories/{category_id}')
async def category(category_id : Annotated[int, 
Path(title="The category ID")],
                  session: Session = Depends(get_session)
) -> Category:
   category = session.get(Category, category_id)
   if not category:
        # status code 404
        raise HTTPException(status_code=404, detail='category not found')
   return category


@app.post('/categories')
async def create_category(
    category_data : CategoryCreate,
    session: Session = Depends(get_session)) -> Category:
     category = Category(
         name=category_data.name, 
         description=category_data.description,
         created_at= category_data.created_at
)
     session.add(category)
     session.flush()

     if category_data.products:
         for product in category_data.products:
             product_obj = Product(
                 name=product.name, 
                 price=product.price, 
                 category_id=category.id, 
                 category=category
             )
             session.add(product_obj)

     session.commit()
     session.refresh(category)
     return category