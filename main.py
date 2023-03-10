from holder import Holder
from blockchain import block_reward
from liq_pool import Pool
from trends import Trend
import math
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

if __name__ == '__main__':
    total_buys = 0
    total_sells = 0
    block = 0
    day = 0
    years_full_population = 750
    starting_cost_per_token = 0.01
    blocks_daily = 144

    holders = []
    x_axis = []
    y_axis = []

    starting_supply = block_reward(block)
    lp = Pool(starting_cost_per_token, starting_supply)
    trend = Trend()

    buy_queue = []
    sell_queue = []

    while day < 333:

        # add block rewards to the circulating supply
        for x in range(blocks_daily):
            lp.add(block_reward(block))
            block += 1
        lp.update()

        # roll the holder's action buy/sell/nothing and add to the corresponding queue
        for holder in holders:
            action = holder.roll()

            if action == 'buy':
                buy_queue.append(holder)

            if action == 'sell':
                sell_queue.append(holder)

            if action == 'nothing':
                continue

        # execute the buy or sell and change the liquidity pool accordingly
        while buy_queue or sell_queue:
            if buy_queue:
                lp.buy_from_pool(buy_queue.pop(0))
                total_buys += 1
            if sell_queue:
                lp.sell_to_pool(sell_queue.pop(0))
                total_sells += 1

        holder_equation = 800_000_000 * math.sin(
            2 * math.pi * day / (2 * years_full_population * 365) - math.pi / 2) + 800_000_000

        num_new_holders = int(holder_equation - len(holders))
        for x in range(num_new_holders):
            new = Holder()
            buy_queue.append(new)
            holders.append(new)
        x_axis.append(day)
        y_axis.append(lp.value)
        day += 1
        trend.add_daily_stat(day, lp.value, lp.circ_supply, lp.supply, len(holders), total_buys, total_sells)

    print(trend.df)

    fig = plt.figure(figsize=(6, 4))
    axes = fig.add_subplot(1, 1, 1)
    plt.title('$USD Vs. Day')
    plt.xlabel('Day')
    plt.ylabel('$USD')
    y1 = list(trend.df['value'])

    y = []
    max_y = 0


    def animate(i):
        y.append((y1[i]))
        plt.xlim(0.01, i + 5)
        plt.plot(y, scaley=True, scalex=True, color="blue")


    anim = FuncAnimation(fig, animate, interval=100)
    plt.show()
