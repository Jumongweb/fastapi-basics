from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
products = []

class User(BaseModel):
    id: int
    name: str
    email: str
    is_active: bool = True

class Product(BaseModel):
    id: int
    name: str
    price: float
    in_stock: bool = True

@app.get("/")
def home():
    return {"message": "Hello Codefather, FastAPI is ready!"}

@app.get("/service")
def service():
    return {"message": "Which of our services do you want to use!"}

@app.get("/items/{item_id}")
def get_item(item_id: int):
    return {"item_id": item_id, "owner": "Codefather"}

@app.get("/search")
def search(q: str | None = None, limit: int = 10):
    return {"query": q, "limit": limit}

@app.post("/users")
def create_user(user: User):
    return {"status": "success", "user": user}

@app.post("/products")
def create_product(product: Product):
    products.append(product)
    return {"message": "Product saved", "product": product}

@app.get("/products")
def get_products():
    return products

@app.get("/products/{product_id}")
def get_product(product_id: int):
    for product in products:
        if product.id == product_id:
            return product
    return {"error": "Product not found"}

@app.put("/products/{product_id}")
def update_product(product_id: int, updated: Product):
    for index, product in enumerate(products):
        if product.id == product_id:
            products[index] = updated
            return {"message": "Product updated", "product": updated}
    return {"error": "Product not found"}

@app.delete("/products/{product_id}")
def delete_product(product_id: int):
    for index, product in enumerate(products):
        if product.id == product_id:
            deleted = products.pop(index)
            return {"message": "Deleted", "product": deleted}
    return {"error": "Product not found"}


