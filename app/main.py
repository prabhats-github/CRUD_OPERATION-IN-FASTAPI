from fastapi import FastAPI
app = FastAPI()

products = [
    {"id": 1, "name": "Product 1", "price": 10.0},
    {"id": 2, "name": "Product 2", "price": 20.0},
    {"id": 3, "name": "Product 3", "price": 30.0},      
]


#read or fetch all data using get method

@app.get("/products")
async def get_products():
    return products