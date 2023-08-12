from fastapi import FastAPI
from fastapi.params import Body

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/post")
async def root(payLoad: dict = Body(...)):
    print(payLoad)
    return {"message": "Received Payload"}