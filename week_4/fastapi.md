# FastAPI Notes

## Table of Contents
1. [FastAPI](#fastapi)
2. [Installation and Creating FastAPI App](#installation-and-creating-fastapi-app)
3. [Endpoints and HTTP Methods](#endpoints-and-http-methods)
4. [Endpoint Parameters](#endpoint-parameters)
   - [Path Parameters](#path-parameters)
   - [Query Parameters](#query-parameters)
5. [Request Body and POST Method](#request-body-and-post-method)
6. [PUT Method](#put-method)
7. [DELETE Method](#delete-method)

---

# FastAPI

- Modern, fast and high performance Web Framework for building API’s with python
- Automatically generates UI documentation → navigate to **/docs**
- Can check our API directly from the documentation UI, no external service like Postman to test the API

# Installation and creating

- FastAPI → python web framework
- Can be installed by using pip install
    
    ```python
    pip install fastapi
    pip install uvicorn
    ```
    
- **uvicorn →** used to run web server
- Django doesn’t needs a external web server
- FastAPI instance is created by
    
    ```python
    from fastapi import FastAPI
    
    app = FastAPI()
    ```
    
- Endpoint → url; one end of a communication channel;
    - GET → get an information
    - POST → Create/Add something new
    - PUT → update a object
    - DELETE → delete something
- Creating endpoint
    
    ```python
    **@app.get("/")**
    def index():
    	return {"response":200}
    ```
    
- FastAPI uses JSON in response
- To run, syntax
    
    ```python
    uvicorn file_name:fastapi_obj --reload
    ```
    

# **Endpoint parameter**

- Used to return a data relating to an input in the path or in the endpoint
- Two endpoint parameters
    1. Path parameter
    2. Query parameter

### **1. Path Parameter**

- URL example: /get/{id} → value is passed in the path
- Parameter is defined in the endpoint
    
    ```python
    @app.get(”/get-pokemon/{pokemon_id}”)
    def get_pokemon(pokemon_id: int):
    	...
    ```
    
- Use *Path* from *FastAPI* to declare and validate
- Features of Path:
    - Default value (optional, but path params are usually required)
    - Description → shown in the OpenAPI docs / Swagger UI
    - Validation:
        - gt, lt, ge, le → int, float
        - min_length, max_length, regex → str
    - Can provide *example* value in Swagger UI

```python
# path parameter
# example -> http://127.0.0.1:8000/get-pokemon/1
@app.get("/get-pokemon/{pokemon_id}")
def get_pokemon(
    pokemon_id: int = Path(
        description="Pokemon's Id that needs to be fetched", gt=0, le=len(pokemons)
    )
):
    return pokemons[pokemon_id]
```

### 2. Query Parameter

- Used to pass values in the URL after **?** as key-value pairs
- Parameter is no needed to be defined in the endpoint
- Optional query parameters are allowed by giving a default value (None)
- Python restriction: Optional parameters cannot come before required ones in the function signature
    - can be solved by Adding ***** at the start to make all parameters keyword-only.

```python
# query parameter
# example -> http://127.0.0.1:8000/get-pokemon-by-name?name=pikachu
@app.get("/get-pokemon-by-name")
def get_pokemon(name: str):
    for pokemon_id in pokemons:
        if pokemons[pokemon_id]["name"] == name:
            return pokemons[pokemon_id]
    return {"data": "Not found"}

#    @app.get("/get-pokemon-by-type")
#    def get_pokemon(type: Optional[str] = None, level: int): -> throws an error
#    optional parameter cannot be before the required one

@app.get("/get-pokemon-by-type")
def get_pokemon(*, type: Optional[str] = None, level: int):  # adding *, will work
    results = {}
    for pokemon_id in pokemons:
        pokemon = pokemons[pokemon_id]
        if (type is None or pokemon["type"] == type) and pokemon["level"] == level:
            results.update(pokemon)

    return results
```

> Both path parameter and query parameter can be combined
> 

# Request Body and Post method

- **Post** → used to send data to server
- **Request Body**
    - Used to send structured data(JSON, form, etc) in the request
    - Defined using *Pydantic’s BaseModel*
    - FastAPI automatically validates the data, converts to correct types, provides Swagger UI

```python
# here pokemon is passed in request body
@app.post("/add-pokemon/{pokemon_id}")
def add_pokemon(pokemon_id: int, pokemon: Pokemon):
    if pokemon_id in pokemons.keys():
        return {"Error": f"Pokemon with {pokemon_id} already exists"}
    pokemons[pokemon_id] = pokemon
    return pokemons[pokemon_id]
```

- Without pydantic’s BaseModel, using Body
    
    ```python
    from fastapi import Body
    @app.post("/add-pokemon")
    async def add_pokemon(
        name: str = Body(...), type: str = Body(...), level: float = Body(...)
    ):
        return {"name": name, "type": type, "level": level}
    ```
    
- Using Request → raw body; Docs won’t show request body
- Using dict or list as body type → no field level validation can be implemented like pydantic

# Put

- put method → update something that already exists
- **PUT**: Replace entire resource → usually all fields required.
- **PATCH**: Partial update → only some fields optional.
- Typically takes a request body

# Delete

- Used to delete a data
