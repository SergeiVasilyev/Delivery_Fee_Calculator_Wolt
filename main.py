from backend.model import Cart
import pytz
from pytz import timezone
from datetime import datetime


def calculate(total, delivery_distance, number_of_items, time):
    cart = Cart(total, delivery_distance, number_of_items, time)
    print('ten_euro_fee', cart.ten_euro_fee())
    print('delivery_fee', cart.delivery_fee())
    print('extra_surcharge', cart.extra_surcharge())
    print('time', time)
    return cart.total_fee()


if __name__ == "__main__":
    # now = datetime.now()
    # datetimenow = pytz.utc.localize(now)
    time = '2024-02-02T20:00:00Z'
    datetimenow = datetime.strptime(time, "%Y-%m-%dT%H:%M:%SZ")
    print('Delivery Fee', calculate(5000, 1200, 12, datetimenow) / 100)

    
    # for i in range(5):
    #     print('Delivery Fee', calculate(1000, i*500, 4, i) / 100)