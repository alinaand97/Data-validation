#Валидация данных

from fastapi import FastAPI, Path, Query

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Главная страница"}

@app.get("/user/admin")
async def read_admin():
    return {"message": "Вы вошли как администратор"}

@app.get("/user/{user_id}")
async def read_user(
    user_id: int = Path(..., gt=0, le=100, description="Enter User ID")
):
    return {"message": f"Вы вошли как пользователь № {user_id}"}

@app.get("/user/{username}/{age}")
async def read_user_info(
    username: str = Path(..., min_length=5, max_length=20, description="Enter username"),
    age: int = Path(..., gt=17, le=120, description="Enter age")
):
    return {"message": f"Информация о пользователе. Имя: {username}, Возраст: {age}"}