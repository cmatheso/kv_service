from http import HTTPStatus
from fastapi import Body, FastAPI, HTTPException
from .models import KeyValueModel

app = FastAPI()

# Using an extremely simple dict for a cache. Generally, this service would probably be replaced with a redis cache directly.
app.state.localCache = {}

@app.get("/kv/{key}", response_model=KeyValueModel)
def read_key(key:str) -> KeyValueModel:
    if key not in app.state.localCache:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail='Key not found')

    data = KeyValueModel()
    data.value = app.state.localCache[key]

    return data

@app.post("/kv/{key}")
def update_key(key:str, model:KeyValueModel = Body(None, embed=False)):
    if key is None or len(key) == 0:
        raise HTTPException(status_code=HTTPStatus.BAD_REQUEST, detail='Key is invalid')

    if model is None:
        raise HTTPException(status_code=HTTPStatus.BAD_REQUEST, detail='Invalid value payload.')

    app.state.localCache[key] = model.value

@app.delete("/kv/{key}", response_model=None)
def delete_key(key:str):
    app.state.localCache.pop(key, None) # Likely don't care if we delete a key that doesn't exist

@app.get('/')
def get_root():
    return 'KV_Service is running!'
