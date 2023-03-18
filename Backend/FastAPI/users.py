from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

#iniciar el servidor con uvicorn users:app --reload

# Entidad user

class User(BaseModel):
    id: int
    name: str
    surname: str
    url: str
    age: int

users_list = [User(id=1, name="Brais", surname="Moure", url="https://moure.dev", age=35),
              User(id=2, name="Moure", surname="Dev", url="https://moure.com", age=35),
              User(id=3, name="Haakon", surname="Dahlberg", url="https://haakon.dev", age=33)]

@app.get("/usersjson")
async def usersjson():
    return [{"name": "Brais", "surname": "Moure", "url": "https://moure.dev", "age":35},
            {"name": "Moure", "surname": "Dev", "url": "https://moure.com", "age":35},
            {"name": "Haakon", "surname": "Dahlberg", "url": "https://haakon.com", "age":33}]

@app.get("/users")
async def users():
    return users_list

# Path
@app.get("/user/{id}")
async def user(id: int):
    return search_user(id)


# Query

@app.get("/user/")   
async def user(id: int):
    return search_user(id)


@app.post("/user/")
async def user(user: User):
    if type(search_user(user.id)) == User:
        return {"Error":"El usuario ya existe"}
    else:
        users_list.append(user)

@app.put("/user/")
async def user(user: User):

    found = False


    for index, saved_user in enumerate(users_list):
        if saved_user.id == user.id:
            users_list[index] = user
            found =True

    if not found:
        return {"error": "No se ha actualizado el usuario"}
            


def search_user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {"error": "No se ha encontrado el usuario"}

