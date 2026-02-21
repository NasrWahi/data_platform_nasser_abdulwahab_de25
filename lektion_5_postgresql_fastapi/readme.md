# postgresql & fastapi

## installation
(Use uv if that's your relevant tech)
* `$ pip install "fastapi[standard]"`
* `$ pip install "psycopg[binary]"`
* `$ pip install "psycopg[pool]"`

# Run App
* `$ fastpi dev main.py`

## Storing data - philosophy

* What's the purpose of our data?
  * Bulk uploading
  * JSON data storage
  * Unorganized data
  * PostgreSQL database
* What's the datatype of said data?
  * Unorganized 
  * unstructured
  * Json

## Database - PostgreSQL
A newly created database does NOT contain any TABLES by default.

Step #1 - Create new Table (products)
```postgresql
CREATE TABLE IF NOT EXISTS products_raw (
id BIGSERIAL PRIMARY KEY,
created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
product JSONB NOT NULL
);
```

Step #2 - Create a connection with the Database using URL
Assuming you're using PGadmin4 you can find the required data like so:
* Username: Right-click your own database -> properties -> username
* Password: You should know this one
* Port: Right-click PostgreSQL 17 -> properties -> connection -> port
* Address: same steps as with Port
```python
DATABASE_URL = "postgresql://USERNAME:PASSWORD@ADDRESS:PORT/DB_NAME"
```

Step #3 - Implement function for Insert (fastAPI)

```python
def insert_product(conn: Connection, product: ProductSchema):
    conn.execute(
        "INSERT INTO products_raw (product) VALUES (%s)",
        (Json(product),)    # TODO - Explore the Syntax
    )
```

Use helper-method:
```python
@app.post(
    "/products",
    status_code=status.HTTP_201_CREATED,    # Swagger Documentation clarity
    response_model=ProductSchema,           # Swagger Documentation update
)
def post_product(product: ProductSchema) -> ProductSchema:

    # Query-Insert
    with pool.connection() as conn:
        insert_product(conn, product)
        conn.commit()   # Execute Logic (close connection when done)

    return product
```


Postman Test against `localhost:8000/products`:
```json
{
    "product_id": "USP239",
    "name": "Wireless Mouse",
    "price": 249.0,
    "currency": "SEK",
    "category": "Electronics",
    "brand": null
}
```

## TODO : Difference between: uvicorn vs fastapi dev main.py 