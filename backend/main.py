from fastapi import FastAPI, Request
from .calculate import calculate
from datetime import datetime

app = FastAPI()


@app.post("/delivery_fee/")
async def delivery_fee(request: Request):
    data = await request.json()

    cart_value = data['cart_value']
    delivery_distance = data['delivery_distance']
    number_of_items = data['number_of_items']
    time = data['time']
    datetimenow = datetime.strptime(time, "%Y-%m-%dT%H:%M:%SZ")

    total_fee = calculate(cart_value, delivery_distance, number_of_items, datetimenow)
    return {"delivery_fee": total_fee}