from typing import Optional

from fastapi import FastAPI, HTTPException, Path
from pokemon_data import Pokemon, UpdatePokemon

app = FastAPI()

pokemons = {
    1: {"name": "greninja", "type": "water", "level": 9},
    2: {"name": "pikachu", "type": "electric", "level": 8.5},
}


# root or home page
@app.get("/")
def index():
    return {"name": "first data"}


@app.get("/get-pokemons")
def get_pokemons():
    return pokemons


# path parameter
# example -> http://127.0.0.1:8000/get-pokemon/1
@app.get("/get-pokemon/{pokemon_id}")
def get_pokemon(
    pokemon_id: int = Path(
        description="Pokemon Id that needs to be fetched", gt=0, le=len(pokemons)
    )
):
    return pokemons[pokemon_id]


# Here len(pokemons) will be calculated only once, when the server loads... no dynamic updation
# can raise an exception using HTTPException


@app.get("/get-pokemon-by-id/{pokemon_id}")
def get_pokemon_by_id(
    pokemon_id: int = Path(description="Pokemon Id that needs to be fetched", gt=0)
):
    if pokemon_id not in pokemons:
        raise HTTPException(status_code=404, detail="Pokemon not found")
    return pokemons[pokemon_id]


# query parameter
# example -> http://127.0.0.1:8000/get-pokemon-by-name?name=pikachu
@app.get("/get-pokemon-by-name")
def get_pokemon_by_name(name: str):
    for pokemon_id in pokemons:
        if pokemons[pokemon_id]["name"] == name:
            return pokemons[pokemon_id]
    return {"data": "Not found"}


#    @app.get("/get-pokemon-by-type")
#    def get_pokemon(type: Optional[str] = None, level: int): -> throws an error
#    optional parameter cannot be before the required one


@app.get("/get-pokemon-by-type")
def get_pokemon_by_type(
    *, type: Optional[str] = None, level: int
):  # adding *, will work

    results = {}
    for pokemon_id in pokemons:
        pokemon = pokemons[pokemon_id]
        if (type is None or pokemon["type"] == type) and pokemon["level"] == level:
            results.update(pokemon)

    return results


# here pokemon is passed in request body
@app.post("/add-pokemon/{pokemon_id}")
def add_pokemon(pokemon_id: int, pokemon: Pokemon):
    if pokemon_id in pokemons.keys():
        return {"Error": f"Pokemon with {pokemon_id} already exists"}
    pokemons[pokemon_id] = pokemon.dict()
    return pokemons[pokemon_id]


# without pydantic's BaseModel
# @app.post("/add-pokemon")
# async def add_pokemon(
#     name: str = Body(...), type: str = Body(...), level: float = Body(...)
# ):
#     return {"name": name, "type": type, "level": level}


@app.put("/update-pokemon/{pokemon_id}")
def update_pokemon(pokemon_id: int, pokemon: UpdatePokemon):
    if pokemon_id not in pokemons:
        return {"Error": f"No pokemon exists with given pokemon_id: {pokemon_id}"}
    pokemon_data = pokemons[pokemon_id]

    # Convert Pydantic model to dict and ignore missing fields
    update_data = pokemon.dict(exclude_unset=True)

    # Update only the provided fields
    pokemons[pokemon_id].update(update_data)

    return {"Success": pokemons[pokemon_id]}


@app.delete("/delete-pokemon/{pokemon_id}")
def delete_pokemon(pokemon_id: int):
    if pokemon_id not in pokemons:
        return {"Error": f"No pokemon exists with given pokemon_id: {pokemon_id}"}
    del pokemons[pokemon_id]

    return {"Success": "Deleted successfully"}
