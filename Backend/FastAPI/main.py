from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return "¡Hola FastAPI"

@app.get("/url")
async def root():
    return {"url":"https://mouredev.com/python"}
