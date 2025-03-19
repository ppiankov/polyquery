from fastapi import FastAPI, HTTPException
import httpx

app = FastAPI()
POLYGON_RPC_URL = "https://polygon-rpc.com/"

@app.get("/block/number")
async def get_block_number():
    """
    Endpoint to get the latest block number.
    """
    payload = {
        "jsonrpc": "2.0",
        "method": "eth_blockNumber",
        "id": 2
    }
    async with httpx.AsyncClient() as client:
        response = await client.post(POLYGON_RPC_URL, json=payload)
    if response.status_code != 200:
        raise HTTPException(status_code=500, detail="Error contacting blockchain RPC")
    data = response.json()
    return {"blockNumber": data.get("result")}


@app.get("/block/{block_number}")
async def get_block_by_number(block_number: str):
    """
    Endpoint to get block details by number.
    The block number should be provided as a hexadecimal string (e.g., '0x134e82a').
    """
    payload = {
        "jsonrpc": "2.0",
        "method": "eth_getBlockByNumber",
        "params": [block_number, True],
        "id": 2
    }
    async with httpx.AsyncClient() as client:
        response = await client.post(POLYGON_RPC_URL, json=payload)
    if response.status_code != 200:
        raise HTTPException(status_code=500, detail="Error contacting blockchain RPC")
    data = response.json()
    return {"block": data.get("result")}