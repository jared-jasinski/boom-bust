import random


class Holder:
    transaction = []

    holdings = 0
    buying_power = 0

    def __init__(self):
        self.transaction = []
        self.luck = 130 / (random.uniform(0, 20) + 1)
        self.buying_power = self.luck / 50000
        self.hands = 100

    def update(self, amount, value):
        self.transaction.append((amount, value))
        self.holdings += amount

    def unrealized_gains(self, curr_value):
        unrealized_gains = 0
        total_cost = 0
        for i in range(len(self.transaction_quantity)):
            unrealized_gains += self.transaction_quantity[i] * (curr_value - self.transaction_at_value[i])
            total_cost += self.transaction_quantity[i] * self.transaction_at_value[i]
        return unrealized_gains / total_cost * 100
