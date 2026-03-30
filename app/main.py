import os
import time
import psycopg2

DB_HOST = os.getenv("DB_HOST", "db")
DB_NAME = os.getenv("DB_NAME", "pet_project")
DB_USER = os.getenv("DB_USER", "myuser")
DB_PASSWORD = os.getenv("DB_PASSWORD", "mypassword")

# Retry подключения к базе, пока сервер не готов
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
        print("Database not ready, waiting 2 seconds...")
        time.sleep(2)

cursor = conn.cursor()

# Создаём таблицу, если не существует
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

print("Hello, this is my pet-project")

Name = input("Your name: ")
Second_name = input("Your second name: ")
Age = int(input("Your age: "))
Mail = input("Email: ")
Subscribe = input("Your plan: ")

cursor.execute(
    "INSERT INTO users (name, second_name, age, email, subscribe) VALUES (%s, %s, %s, %s, %s)",
    (Name, Second_name, Age, Mail, Subscribe)
)
conn.commit()

if Subscribe == "Pro":
    print(f"Dear {Name} {Second_name}, you have Pro subscription: you can go boxing and gym")
elif Subscribe == "Standart":
    print(f"Dear {Name} {Second_name}, you can go to the gym. Upgrade to Pro for boxing")
else:
    print("Please buy a subscription. Contact support for info")

print("Thanks for using the app")