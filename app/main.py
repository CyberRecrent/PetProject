from fastapi import FastAPI
from pydantic import BaseModel
import psycopg2
import os
import time

app = FastAPI()

DB_HOST = os.getenv("DB_HOST", "db")
DB_NAME = os.getenv("DB_NAME", "pet_project")
DB_USER = os.getenv("DB_USER", "myuser")
DB_PASSWORD = os.getenv("DB_PASSWORD", "mypassword")

# подключение к базе с retry
while True:
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        )
        break
    except psycopg2.OperationalError:
        print("Waiting for DB...")
        time.sleep(2)

cursor = conn.cursor()

# создаём таблицу
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50),
    second_name VARCHAR(50),
    age INT,
    email VARCHAR(100),
    subscribe VARCHAR(20)
)
""")
conn.commit()


# модель пользователя
class User(BaseModel):
    name: str
    second_name: str
    age: int
    email: str
    subscribe: str


# 🔥 POST — создать пользователя
@app.post("/users")
def create_user(user: User):
    cursor.execute(
        "INSERT INTO users (name, second_name, age, email, subscribe) VALUES (%s, %s, %s, %s, %s)",
        (user.name, user.second_name, user.age, user.email, user.subscribe)
    )
    conn.commit()

    return {"message": "User created successfully"}


# 🔥 GET — получить всех пользователей
@app.get("/users")
def get_users():
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()

    return {"users": rows}