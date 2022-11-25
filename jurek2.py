from pycoingecko import CoinGeckoAPI
import pandas as pd

cg = CoinGeckoAPI()
cs = 'bitcoin'

chart = cg.get_coin_market_chart_by_id(id='hive', vs_currency='usd', days=90)
print(chart)

