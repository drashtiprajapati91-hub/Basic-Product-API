from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS

app = Flask(__name__)
api = Api(app)
CORS(app)

# Sample product data
products = [
    {
        "id": 1,
        "name": "Wireless Headphones",
        "brand": "Sony",
        "category": "Electronics",
        "price": 3499,
        "rating": 4.5,
        "in_stock": True
    },
    {
        "id": 2,
        "name": "Gaming Keyboard",
        "brand": "Logitech",
        "category": "Electronics",
        "price": 2899,
        "rating": 4.7,
        "in_stock": True
    },
    {
        "id": 3,
        "name": "Running Shoes",
        "brand": "Nike",
        "category": "Fashion",
        "price": 4999,
        "rating": 4.3,
        "in_stock": False
    }
]

# PRODUCT LIST (GET, POST)

class ProductList(Resource):
    def get(self):
        # Search + Filter
        search = request.args.get("search")
        category = request.args.get("category")

        filtered = products

        if search:
            filtered = [p for p in filtered if search.lower() in p["name"].lower()]

        if category:
            filtered = [p for p in filtered if p["category"].lower() == category.lower()]

        return {"total": len(filtered), "products": filtered}

    def post(self):
        new_product = request.json

        if not new_product:
            return {"error": "No data provided"}, 400

        # Generate new ID automatically
        new_product["id"] = products[-1]["id"] + 1 if products else 1
        products.append(new_product)

        return {"message": "Product added successfully", "product": new_product}, 201



# SINGLE PRODUCT (GET, PUT, DELETE)

class SingleProduct(Resource):
    def get(self, product_id):
        product = next((p for p in products if p["id"] == product_id), None)
        if product:
            return product
        return {"error": "Product not found"}, 404

    def put(self, product_id):
        product = next((p for p in products if p["id"] == product_id), None)
        if not product:
            return {"error": "Product not found"}, 404

        updated_data = request.json
        for key, value in updated_data.items():
            product[key] = value

        return {"message": "Product updated successfully", "product": product}

    def delete(self, product_id):
        global products
        products = [p for p in products if p["id"] != product_id]

        return {"message": "Product deleted successfully"}



# Register API Routes
api.add_resource(ProductList, "/products")
api.add_resource(SingleProduct, "/products/<int:product_id>")

if __name__ == "__main__":
    app.run(debug=True)
