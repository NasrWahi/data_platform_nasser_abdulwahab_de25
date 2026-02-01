# Deletion of `__name__` - why?

Traditional Python script:
```python
def main():
    print("App started")

if __name__ == "__main__":
    main()
```
FastAPI (no __name__ needed):
```python
from fastapi import FastAPI

app = FastAPI()
```


## Servlet Container
* Hosting of application (locally)
* FastAPI introduces a different way of running applications
* Removes the traditional "play/start" button
* Requires a FastAPI start command to run the app

## FastAPI
* Install:
  * `$ pip install "fastapi[standard]"`
* Verify installation (via `.venv`)
  * List project dependencies:
    * `$ pip list`
* Best practice
  * Keep `main.py` in the root folder
* Start application
  * `$ fastapi dev FILENAME.py`
  * IMPORTANT: stand in the same folder as `main.py`
* Bonus
  * `uv` as an alternative for better performance
  * `CMD + F` (filter for "success", use `CTRL` on Windows)
* Warning
  * "Consider adding this to PATH"

Fast Api (minimal app)
```python
from fastapi import FastAPI

app = FastAPI()
```

## Endpoint
* API & URL related
* Consists of a path: "/example" 
* Accompanied by an HTTP-Method (GET, POST, PUT, DELETE)

```python
@app.get("/example")
def example():
    return {"message": "Hello"}
```


## Decorator
- A decorator uses the `@` symbol
- It adds behavior to a function without changing the function itself
- In FastAPI:
  - The decorator registers the function as an endpoint
  - It connects a URL and an HTTP method to the function
- The function is called automatically when a request matches
- The return value is automatically converted to JSON

Example:
```python
@app.get("/test")
def test_function():
    return {"status": "ok"}
```

## URL
Example URL: # https://www.google.com/search?q=bananas
* In this example we see a dynamic parameter
  * q == query (just a variable name)
  * ? == start of query
  * What comes after = is Dynamic_Value (client input)

```python
@app.get("/search")
def search(q: str):
    return {"query": q}
```

## Pydantic
- Uses schemas (defines the logical data structure)
- Class-based
- Used for data validation
- Facilitates conversion of JSON → Python objects
- Best practice: keep schemas in a separate package or file
- Uses `BaseModel` as the base class for schema definitions

```python
from pydantic import BaseModel

class Product(BaseModel):
    name: str
    price: float
```