from fastapi import FastAPI, HTTPException, Depends, File, UploadFile, Form
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, EmailStr, Field
from typing import List, Annotated
import models
from database import engine, SessionLocal
from sqlalchemy.orm import Session
from datetime import date
from sqlalchemy import update,text, func, desc
import shutil



app = FastAPI()
models.Base.metadata.create_all(bind=engine)


origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:5173",
    "http://127.0.0.1:5500"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ProductBase(BaseModel):
    name: str = Form(...)
    description: str = Form(...)
    price: float = Form(...)
    # uploaded_file: UploadFile = File(...)

class UserBase(BaseModel):
    name: str
    email: EmailStr
    address: str
    password: str
    date_of_birth: date

class RatingBase(BaseModel):
    product_id: int
    user_id: int
    rate: float

class LoginBase(BaseModel):
    email: EmailStr
    password: str


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

@app.get("/product/{product_id}")
async def get_product(product_id:str, db: db_dependency):
    if product_id == "all":
        result = db.query(models.Products).all() #.order_by(desc(models.Products.rating))
    else:
        result = db.query(models.Products).filter(models.Products.id==product_id).first()
    if not result:
        raise HTTPException(status_code=404,detail="No product Found !")
    return result

@app.post("/product/")
async def create_product(product: ProductBase, db: db_dependency):
    # filename = create_upload_file(product.uploaded_file)

    db_product = models.Products(name=product.name,description=product.description,price=product.price, picture="/src/assets/images/product-item1.jpg")
    db.add(db_product)
    db.commit()
    new_procuct_id = db_product.id
    db.refresh(db_product)
    if not db_product:
        raise HTTPException(status_code=404,detail="Error insert!")
    return new_procuct_id

@app.delete("/product/{product_id}")
async def delete_product(product_id: int, db: db_dependency):
    db_product = db.query(models.Products).filter(models.Products.id==product_id).delete()
    db.commit()
    if not db_product:
        raise HTTPException(status_code=404,detail="No User Found !")
        
    
@app.post("/login/")
async def simple_login(user: LoginBase, db: db_dependency):
    result = db.query(models.Users).filter(models.Users.email==user.email).filter(models.Users.password==user.password).first()
    if not result:
        raise HTTPException(status_code=404,detail="No User Found !")
    return result

@app.post("/user/")
async def create_user(user: UserBase, db: db_dependency):
    db_user = models.Users(name=user.name,email=user.email,address=user.address,password=user.password,date_of_birth=user.date_of_birth)
    db.add(db_user)
    db.commit()
    new_user_id = db_user.id
    db.refresh(db_user) 
    if not db_user:
        raise HTTPException(status_code=404,detail="Error Add!")
    return new_user_id

@app.delete("/user/{user_id}")
async def delete_user(user_id: str, db: db_dependency):
    db_user = db.query(models.Users).filter(models.Users.id==user_id).delete()
    db.commit()
    if not db_user:
        raise HTTPException(status_code=404,detail="No User Found !")
    

@app.post("/rating/")
async def add_rating(rating: RatingBase, db: db_dependency):
    rating_exist = db.query(models.Ratings).filter(models.Ratings.user_id==rating.user_id).filter(models.Ratings.product_id==rating.product_id).first()
    if rating_exist:
        update_rating = db.query(models.Ratings).filter(models.Ratings.user_id==rating.user_id).filter(models.Ratings.product_id==rating.product_id).update({"rate":rating.rate})
        db.commit()
    else:
        db_rating = models.Ratings(product_id=rating.product_id,user_id=rating.user_id,rate=rating.rate)
        db.add(db_rating)
        db.commit()
        db.refresh(db_rating)

    product_count = db.query(models.Ratings).filter(models.Ratings.product_id==rating.product_id).count()
    product_rating = db.query(func.sum(models.Ratings.rate).label('sum')).filter(models.Ratings.product_id==rating.product_id).first()

    update_product_rating = db.query(models.Products).filter(models.Products.id==rating.product_id).update({"rating":product_rating[0]/product_count})
    db.commit()

    return update_product_rating

@app.delete("/rating/{product_id}")
async def delete_rating(product_id: int, db: db_dependency):
    db_rating = db.query(models.Ratings).filter(models.Ratings.product_id==product_id).delete()
    db.commit()
    if not db_rating:
        raise HTTPException(status_code=404,detail="No Ratings Found !")
    
    

async def create_upload_file(uploaded_file: UploadFile = File(...)):    
    file_location = f"upload_dir/picture/{uploaded_file.filename}"
    with open(file_location, "wb+") as file_object:
        shutil.copyfileobj(uploaded_file.file, file_object)    
    return file_location
    




