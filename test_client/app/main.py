# from http import HTTPStatus
from http import HTTPStatus
from fastapi import FastAPI, HTTPException

from .kv_service_client import kv_service_client

app = FastAPI()

client = kv_service_client()

@app.get('/')
def get_root():
    return 'test_client is running!'

@app.get("/test/deletion")
def test_deletion():
    testKey = 'test_deletion'
    testVal = 'some text'

    if not client.update_key(testKey, testVal):
        raise HTTPException(status_code=HTTPStatus.INTERNAL_SERVER_ERROR, detail='Test storing response indicated a failure')

    respVal = client.read_key(testKey)
    if respVal != testVal:
        raise HTTPException(status_code=HTTPStatus.INTERNAL_SERVER_ERROR, detail='Test reading failed')

    if not client.delete_key(testKey):
        raise HTTPException(status_code=HTTPStatus.INTERNAL_SERVER_ERROR, detail='Test deletion response indicated a failure')

    respVal = client.read_key(testKey)
    if respVal is not None:
        raise HTTPException(status_code=HTTPStatus.INTERNAL_SERVER_ERROR, detail='Test deletion failed')

    return 'Passed'

@app.get("/test/overwrite")
def test_overwrite():
    testKey = 'test_overwrite'
    testVal = 'some text'
    testVal2 = 'updated text'

    if not client.update_key(testKey, testVal):
        raise HTTPException(status_code=HTTPStatus.INTERNAL_SERVER_ERROR, detail='Test storing 1st key response indicated a failure')
    
    respVal = client.read_key(testKey)
    if respVal != testVal:
        raise HTTPException(status_code=HTTPStatus.INTERNAL_SERVER_ERROR, detail='Test reading 1st key failed')

    if not client.update_key(testKey, testVal2):
        raise HTTPException(status_code=HTTPStatus.INTERNAL_SERVER_ERROR, detail='Test storing 2nd key response indicated a failure')

    respVal = client.read_key(testKey)
    if respVal != testVal2:
        raise HTTPException(status_code=HTTPStatus.INTERNAL_SERVER_ERROR, detail='Test reading 2nd key failed')

    return 'Passed'
