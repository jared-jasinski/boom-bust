import random


class Holder:
    transaction = []

    hodl = False

    holdings = 0
    luck = 0
    buying_power = 0
    hands = 0
    buy_chance = 0.1

    def __init__(self):
        self.luck = 130 / random.uniform(0, 10)
        self.hands = 100

    def update(self, tx):
        self.transaction.append(tx)

    def unrealized_gains(self, curr_value):
        unrealized_gains = 0
        total_cost = 0
        for i in range(len(self.transaction_quantity)):
            unrealized_gains += self.transaction_quantity[i] * (curr_value - self.transaction_at_value[i])
            total_cost += self.transaction_quantity[i] * self.transaction_at_value[i]
        return unrealized_gains / total_cost * 100
