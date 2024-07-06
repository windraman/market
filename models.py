import os

from libcloud.storage.drivers.local import LocalStorageDriver
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float, Date
from database import Base
from sqlalchemy_file import File, FileField
from sqlalchemy_file.storage import StorageManager

class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, index=True)
    address = Column(String, index=True)
    password = Column(String, index=True)
    date_of_birth = Column(Date, index=True)

class Products(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True)
    price = Column(Float, index=True)
    picture = Column(String, index=True)
    rating = Column(Float, index=True, default=0)

class Ratings(Base):
    __tablename__ = 'ratings'

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("products.id"))
    user_id = Column(Integer, ForeignKey("users.id"))
    rate = Column(Float, index=True, default=0)


