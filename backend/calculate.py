from .model import Cart
from datetime import datetime


def calculate(total, delivery_distance, number_of_items, time):
    cart = Cart(total, delivery_distance, number_of_items, time)
    return cart.total_fee()


if __name__ == "__main__":
    cart_value = 790
    delivery_distance = 2235
    number_of_items = 4
    time = '2024-01-15T13:00:00Z'
    date = datetime.strptime(time, "%Y-%m-%dT%H:%M:%SZ")

    print('Delivery Fee', calculate(cart_value, delivery_distance, number_of_items, date))