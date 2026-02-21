from fastapi import FastAPI, status
from psycopg_pool import ConnectionPool
from psycopg.types.json import Json # Convert Pydantic -> JSON
from psycopg import Connection      # Open Temporary Connection

from schema.product import ProductSchema

DATABASE_URL = "postgresql://USERNAME:PASSWORD@ADDRESS:PORT/DB_NAME"
pool = ConnectionPool(DATABASE_URL)
app = FastAPI(title="lektion_5_postgresql_fastapi")

@app.get("/")
def root() -> dict:
    return {"Hello": "World"}

@app.post(
        "/products", 
    status_code=status.HTTP_201_CREATED, # Swagger Documentation clarity
    response_model=ProductSchema,        # Swagger Documentation update
)
def post_product(product: ProductSchema) -> ProductSchema:
   
    # Query-Insert
    with pool.connection() as conn:
        insert_product(conn, product.model())
        conn.commit()    # Execute Logic (close connection when done)
   
    return product


# Helper Method for DB-quaries
def insert_product(conn: Connection, product: ProductSchema):
    conn.execute(
        "INSERT_INTO products_raw (product) VALUES (%s)",
        (Json(product),)    # TODO - Explore the Syntax
    )