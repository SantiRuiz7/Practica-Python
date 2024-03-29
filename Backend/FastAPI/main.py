from fastapi import FastAPI
from routers import products, users, basic_auth_users, jwt_auth_users, users_db
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# URL local = http://127.0.0.1:8000

# Routers

app.include_router(products.router)
app.include_router(users.router)

app.include_router(basic_auth_users.router)
app.include_router(jwt_auth_users.router)
app.include_router(users_db.router)


app.mount("/static", StaticFiles(directory="static"), name= "static")


@app.get("/")
async def root():
    return "¡Hola FastAPI"

# URL local = http://127.0.0.1:8000/url

@app.get("/url")
async def root():
    return {"url":"https://mouredev.com/python"}

#iniciar el servidor con uvicorn main:app --reload
#cerrar el servidor con CTRL+C

# Swagger URL local = http://127.0.0.1:8000/docs
# Redocly  URL local = http://127.0.0.1:8000/redocs

