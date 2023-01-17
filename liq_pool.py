class Pool:
    circ_supply = 0
    market_cap = 0
    value = 0
    USD = 0

    # the starting price will be $0.30 USD per token. the luck parameter of the Holder will be used to determine the
    # proportion of the pool able to be bought and the price impact of the purchase

    # the liquidity pool equation is  x * y = k, where x = USD quantity, y = item y quantity, and k = constant
    #
    # 10 ETH * 1,000 DAI = 10,000
    # What happens when someone buys 1 ETH from this pool?
    # (10 - 1) ETH * y DAI = 10,000
    # new
    def __init__(self, value, circ_supply):
        self.value = value
        self.circ_supply = circ_supply
        self.market_cap = value * self.circ_supply
        self.USD = value * circ_supply

    def buy_from_pool(self, holder):
        amount_to_buy = self.circ_supply * holder.buying_power
        holder.update(amount_to_buy, self.value)

        self.value = self.market_cap * 0.2 / (self.circ_supply * 0.2 - amount_to_buy)
        # print(amount_to_buy)

    def sell_to_pool(self, param):
        pass

    def add(self, reward):
        self.circ_supply += reward

    def update(self):
        self.market_cap = self.circ_supply * self.value
