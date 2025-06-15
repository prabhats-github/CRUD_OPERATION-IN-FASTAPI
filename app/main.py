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

#read or fetch a single product by id using get method
@app.get("/products/{product_id}")
async def get_product(product_id: int):
    for i in products:
        if i["id"] == product_id:
            return i
    return {"error": "Product not found"}

# Create or insert a new product using post method
@app.post("/products")
async def create_product(new_product: dict):
    products.append(new_product)
    return {"status": "Product created successfully", "new product": new_product}

#put request
#update complete data
    