# Description

A Django Project to Get/Add/Update/Delete Products for a Shopping Site.

## Features :

1. RESTFul APIs for CRUD Operation.
2. JWT Authentication

## Endpoints :

1. GET All Products
```python
   endpoint : http://127.0.0.1:8000/product/
   response : [{
        "id": 1,
        "name": "A320",
        "description": "Passenger Aircraft",
        "units": 3,
        "category": "Commercial"
    },
    {
        "id": 2,
        "name": "H135",
        "description": "Light Twin",
        "units": 1,
        "category": "Helicopter"
    }]
```

2. GET All Products of a given Category
```python
   endpoint :http://127.0.0.1:8000/product/?category=Helicopter
   response : [ {
        "id": 2,
        "name": "H135",
        "description": "Light Twin",
        "units": 1,
        "category": "Helicopter"
    },...]
    
```
3. Create/POST a new Product
```python
   endpoint :http://127.0.0.1:8000/product/
   payload :
    {
        "name": "H135",
        "description": "Light Twin",
        "units": 1,
        "category": "Helicopter"
    }
    
```

4. Update/PUT an existing Product
```python
   endpoint :http://127.0.0.1:8000/product/<product_id>
   payload :
    {
        "units": 5,

    }
    
```

5. Delete an existing Product
```python
   endpoint :http://127.0.0.1:8000/product/<product_id>
    
```

