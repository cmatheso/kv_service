"""Tests targetting the kv_service app."""

from fastapi.testclient import TestClient
import pytest

from app.main import app
from app.models import KeyValueModel

client = TestClient(app)

def __get_key_value(key:str) -> str:
    """Helper function to retrieve the key value from the endpoint."""

    response = client.get(f"/kv/{key}")
    assert response.status_code == 200

    return KeyValueModel(**response.json())

def test_read_key_empty(request: pytest.FixtureRequest):
    response = client.get(f"/kv/{request.node.name}")
    assert response.status_code == 404

def test_update_key(request: pytest.FixtureRequest):
    testData = KeyValueModel()
    testData.value = 'some data 1234324'

    response = client.post(f"/kv/{request.node.name}", data=testData.json())
    assert response.status_code == 200

def test_set_and_retrieve_key(request: pytest.FixtureRequest):
    testData = KeyValueModel()
    testData.value = 'some data 1234324'

    response = client.post(f"/kv/{request.node.name}", data=testData.json())
    assert response.status_code == 200

    # Read value back to ensure it was successful
    keyVal = __get_key_value(request.node.name)
    assert keyVal.value == testData.value

def test_key_overwrite(request: pytest.FixtureRequest):
    testData = KeyValueModel()
    testData.value = 'some data 1234324'

    response = client.post(f"/kv/{request.node.name}", data=testData.json())
    assert response.status_code == 200

    # Read value back to ensure it was successful
    keyVal = __get_key_value(request.node.name)
    assert keyVal.value == testData.value

    # Run the overwrite now
    testData2 = KeyValueModel()
    testData2.value = 'overwritten!!!'

    response = client.post(f"/kv/{request.node.name}", data=testData2.json())
    assert response.status_code == 200

    # Read overwritten value back to ensure it was successful
    keyVal = __get_key_value(request.node.name)
    assert keyVal.value == testData2.value

def test_delete_key_empty(request: pytest.FixtureRequest):
    response = client.delete(f"/kv/{request.node.name}")
    assert response.status_code == 200

def test_set_and_delete_key(request: pytest.FixtureRequest):
    testData = KeyValueModel()
    testData.value = 'some data 1234324'
    response = client.post(f"/kv/{request.node.name}", data=testData.json())
    assert response.status_code == 200

    # Read value back to ensure it was successful
    keyVal = __get_key_value(request.node.name)
    assert keyVal.value == testData.value

    # Trigger deletion now
    response = client.delete(f"/kv/{request.node.name}")
    assert response.status_code == 200

    # Confirm its gone
    response = client.get(f"/kv/{request.node.name}")
    assert response.status_code == 404
