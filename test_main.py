from fastapi.testclient import TestClient

from main import app
from database import engine,Base, SessionLocal
from httpx import AsyncClient
from starlette import status
from inline_snapshot import snapshot
from dirty_equals import IsStr, IsUUID, IsNumeric, IsList, IsJson, IsInt, IsDate, IsFloat
from pydantic import EmailStr

client = TestClient(app)

new_product_id = 0
new_user_id = 0

def test_create_produk():
    global new_product_id
    payload = {
        "name": "Produk",
        "description": "Test Produk",
        "price": 9999
    }
    response = client.post("product", json=payload)
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == snapshot(IsInt())
    new_product_id = response.json()


def test_product():
    response = client.get("product/all")
    assert response.status_code == status.HTTP_200_OK
    #compare list of json response
    # assert response.json() == IsList(snapshot(
    #             {
    #                 "name": IsStr(),
    #                 "id": IsInt(),
    #                 "price": IsFloat(),
    #                 "rating": IsFloat(),
    #                 "picture": IsStr(),
    #                 "description": IsStr()
    #             }
    #         )
    #     )

def test_create_user():
    global new_user_id
    payload = {
        "email": "joe@grillazz.com",
        "name": "Joe",
        "address": "Kampoeng Baroe",
        "password": "s1llyYou",
        "date_of_birth": "2024-07-07"
    }
    response = client.post("user", json=payload)
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == snapshot(IsInt())
    new_user_id = response.json()

def test_add_rating():
    #change product_id and user_id to existing 
    global new_user_id, new_product_id
    payload = {
        "product_id": new_product_id,
        "user_id": new_user_id,
        "rate": 3
        }
    response = client.post("rating", json=payload)
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == snapshot(IsInt())

def test_simple_login():
    #change email and password to existing 
    payload = {
        "email": "joe@grillazz.com",
        "password": "s1llyYou"
        }
    response = client.post("login", json=payload)
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == snapshot({
            "id": IsInt(),
            "email": IsStr(regex=r"^\S+@\S+\.\S+$"), #matching email format
            "name": IsStr(),
            "address": IsStr(),
            "password": IsStr(),
            "date_of_birth" : IsStr() #matching date format
        })

def test_delete_rating():
    global new_product_id
    response = client.delete("rating/"+str(new_product_id))
    assert response.status_code == status.HTTP_200_OK

#relatioanal data in rating table must be delete first
def test_delete_user():
    global new_user_id
    response = client.delete("user/"+str(new_user_id))
    assert response.status_code == status.HTTP_200_OK

def test_delete_product():
    global new_product_id
    response = client.delete("product/"+str(new_product_id))
    assert response.status_code == status.HTTP_200_OK
