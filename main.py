from fastapi import FastAPI
from models import Movietop

app = FastAPI()
movietop_data = [
    {"name": "Аватар", "id": 1, "cost": 23700000000, "director": "Джеймс Кэмерон"},
    {"name": "Мстители: Финал", "id": 2, "cost": 35600000000, "director": "Энтони и Джо Руссо"},
    {"name": "Мстители: Война бесконечности", "id": 3, "cost": 231600000000, "director": "Энтони и Джо Руссо"},
    {"name": "Пираты Карибского моря: На странных берегах", "id": 4, "cost": 37850000000, "director": "Роб Маршалл"},
    {"name": "Стражи Галактики. Часть 3", "id": 5, "cost": 25000000000, "director": "Джеймс Ганн"},
    {"name": "Терминатор 3: Восстание машин", "id": 6, "cost": 20000000000, "director": "Джонатан Мостоу"},
    {"name": "Титаник", "id": 7, "cost": 20000000000, "director": "Джеймс Кэмерон"},
    {"name": "Король Лев (2019)", "id": 8, "cost": 26000000000, "director": "Джон Фавро"},
    {"name": "Джон Картер", "id": 9, "cost": 26370000000, "director": "Эндрю Стэнтон"},
    {"name": "Звёздные войны: Пробуждение силы", "id": 10, "cost": 24500000000, "director": "Дж. Дж. Абрамс"}]

@app.get("/movietop/{name}")
async def movietop(name: str):
    for movie in movietop_data:
        if movie["name"] == name:
            return movie