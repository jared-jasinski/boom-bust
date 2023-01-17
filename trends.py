import pandas as pd


class Trend:
    df = pd.DataFrame(columns=['days', 'value', 'circ_supply', 'supply', 'holders', 'buys', 'sells'])

    def add_daily_stat(self, day, value, circ_supply, supply, holders, buys, sells):
        self.df.loc[day] = day, value, circ_supply, supply, holders, buys, sells
