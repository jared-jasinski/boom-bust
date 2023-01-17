import random


class Holder:
    days_hodling = 0
    transactions = []

    holdings = 0
    buying_power = 0
    xs = 0

    numerator = 0

    def __init__(self):
        self.transactions = []
        self.luck = 130 / (random.uniform(0, 100) + 1)
        self.buying_power = self.luck / 50000

    def update(self, amount, value):
        self.transactions.append((amount, value))
        self.holdings += amount
        self.numerator = self.numerator + amount * value
        self.xs = (abs(value) / (self.numerator / abs(self.holdings)))

    def add_day(self):
        self.days_hodling += 1

    def roll(self):
        if random.random() < 0.05:
            # do something 75% of the time
            return 'buy'
        else:
            # do something else 25% of the time
            return 'sell'    # generate selling chance
    # generate buying chance
    # generate do nothing chance

    # use moving average of price
    # use x factor
    # multiply by sinusoid + linear amount?
    # sin(ωt) + 2t
