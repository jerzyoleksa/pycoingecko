from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()
result = cg.get_price(ids='bitcoin', vs_currencies='usd')
print(result)

h = cg.get_coin_history_by_id('cap', date='10-11-2022')
hprice = h['market_data']['current_price']['usd']
print(hprice)
