from holder import Holder
from blockchain import block_reward
from liq_pool import Pool
import math


if __name__ == '__main__':
    block = 0
    circ_supply = 0
    day = 1
    years_full_population = 1000
    starting_cost_per_token = 0.30

    holders = []

    starting_supply = block_reward(block)
    lp = Pool(starting_cost_per_token, starting_supply)

    buy_queue = []
    sell_queue = []

    while 1:

        while buy_queue or sell_queue:
            if buy_queue:
                lp.buy_from_pool(buy_queue.pop(0))
            if sell_queue:
                lp.sell_to_pool(sell_queue.pop(0))

        holder_equation = 8_000_000_000 * math.sin(
            2 * math.pi * day / (2 * years_full_population * 365) - math.pi / 2) + 8_000_000_000

        num_new_holders = int(holder_equation - len(holders))
        for x in range(num_new_holders):
            new_holder = Holder()
            buy_queue.append(new_holder)
            holders.append(new_holder)
        day += 1
