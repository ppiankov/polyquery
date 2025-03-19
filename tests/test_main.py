from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_block_number():
    response = client.get("/block/number")
    assert response.status_code == 200
    data = response.json()
    # We expect a hex string, e.g., "0x..." for the block number.
    assert "blockNumber" in data
    assert isinstance(data["blockNumber"], str)
    assert data["blockNumber"].startswith("0x")

def test_get_block_by_number():
    # Use a sample block number (for example, "0x1").
    response = client.get("/block/0x1")
    assert response.status_code == 200
    data = response.json()
    # The result may be None if the block does not exist.
    assert "block" in data
    # When a valid block is returned, it should be a dict.
    if data["block"]:
        assert isinstance(data["block"], dict)