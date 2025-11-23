"# Basic-Product-API" 
Installation

Clone the repository:

git clone <your-repo-link>
cd <project-folder>

Install dependencies:

pip install flask flask-restful flask-cors

Run the server:

python app.py

Server will start at:

http://127.0.0.1:5000
📌 API Endpoints
1. Get All Products
GET /products

Optional Query Params:

search – Search by product name

category – Filter by category

Example:

GET /products?search=shoe&category=Fashion
2. Get Single Product
GET /products/<id>

Example:

GET /products/2
3. Add New Product
POST /products

Body (JSON):

{
  "name": "Smart Watch",
  "brand": "Apple",
  "category": "Electronics",
  "price": 25999,
  "rating": 4.9,
  "in_stock": true
}
4. Update Product
PUT /products/<id>

Body (JSON) Example:

{
  "price": 2999,
  "in_stock": false
}
5. Delete Product
DELETE /products/<id>

Example:
