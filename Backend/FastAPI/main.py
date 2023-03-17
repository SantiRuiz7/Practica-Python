from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return "¡Hola FastAPI"

@app.get("/url")
async def root():
    return {"url":"https://mouredev.com/python"}

#iniciar el servidor con uvicorn main:app --reload
#cerrar el servidor con CTRL+C

