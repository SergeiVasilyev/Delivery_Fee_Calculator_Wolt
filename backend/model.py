class Cart:
    def __init__(self, total, delivery_distance, number_of_items, time):
        self.total = total
        self.delivery_distance = delivery_distance
        self.number_of_items = number_of_items
        self.time = time
        self.fee = 0
    
    def no_fee(func):
    # No fee if total price is equal or more than 20000 (€200.00)
        def wrapper(obj):
            if obj.total < 20000:
                return func(obj)
            return 0
        return wrapper

    @no_fee
    def ten_euro_fee(self):
        if self.total < 1000:
            self.fee = 1000 - self.total
            return self.fee
        return 0

    @no_fee
    def delivery_fee(self):
        base_fee = 200 # base fee
        if self.delivery_distance > 1000:
            additional_distance = self.delivery_distance - 1000
            self.fee = base_fee + (additional_distance // 500 + int(bool(additional_distance % 500))) * 100
            return self.fee
        return base_fee
    
    @no_fee
    def extra_surcharge(self):
        min_no_extra_fee, min_no_extra_bulk = 4, 12
        if self.number_of_items > min_no_extra_fee:
            self.fee = (self.number_of_items - 4) * 50
            if self.number_of_items > min_no_extra_bulk:
                self.fee += 120
            return self.fee
        return 0

    @no_fee
    def no_fee_on_friday(self):
        if self.time.weekday() == 4 and self.time.hour >= 15 and self.time.hour <= 19:
            return self.fee * 1.2
        return self.fee
    

    def total_fee(self):
        self.fee = 0
        self.fee = self.ten_euro_fee() + self.delivery_fee() + self.extra_surcharge()
        self.fee = self.no_fee_on_friday()
        self.fee = 1500 if self.fee > 1500 else self.fee
        return self.fee

