"""Tests targetting the kv_service app."""

from fastapi.testclient import TestClient
import pytest

from app.main import app

client = TestClient(app)

def test_overwrite(request: pytest.FixtureRequest):
    response = client.get(f"/test/overwrite")
    assert response.status_code == 200

def test_deletion(request: pytest.FixtureRequest):
    response = client.get(f"/test/deletion")
    assert response.status_code == 200