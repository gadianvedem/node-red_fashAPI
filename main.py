from fastapi import FastAPI
import random

app = FastAPI()

# Hàm để sinh ngẫu nhiên giá trị nhiệt độ
def generate_random_temperature():

    return round(random.uniform(25, 30), 2)

# Hàm để sinh ngẫu nhiên giá trị độ ẩm
def generate_random_humidity():

    return round(random.uniform(80, 95), 2)

@app.get("/")
async def read_data():
    # Gán giá trị nhiệt độ và độ ẩm bằng hàm sinh ngẫu nhiên
    temperature = generate_random_temperature()
    humidity = generate_random_humidity()
    return {"temperature": temperature, "humidity": humidity}
