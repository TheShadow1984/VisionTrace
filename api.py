from fastapi import FastAPI
import httpx

app = FastAPI()

async def fetch_api(url):
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        return response.json()

@app.get("/flights")
async def planes():
    return await fetch_api("https://opensky-network.org/api/states/all")

@app.get("/acled")
async def acleds():
    pass

@app.get("/nasa")
async def nasa():
    pass

@app.get("/gtd")
async def gtd():
    pass