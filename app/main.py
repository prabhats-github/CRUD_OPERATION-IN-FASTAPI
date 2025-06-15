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
@app.put("/products/{product_id}")
async def update_product(product_id: int, updated_product: dict):
    for index, i in enumerate(products):
        if i["id"] == product_id:
            products[index] = updated_product
            return {"status": "Product updated successfully", "updated product": updated_product}
       
#patch request 
#update partial data
@app.patch("/products/{product_id}")
async def partial_update_product(product_id: int, updated_data: dict):
    for index, i in enumerate(products):
        if i["id"] == product_id:
            products[index].update(updated_data)
            return {"status": "Product partially updated successfully", "updated product": products[index]}
    return {"error": "Product not found"}


#delete request
#delete a product by id
@app.delete("/products/{product_id}")
async def delete_product(product_id: int):
   for index, i in enumerate(products):
        if i["id"] == product_id:
           products.pop(index)
        return {"status": "Product deleted successfully"}