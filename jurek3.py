#https://ecency.com/hive-169321/@steevc/extracting-data-from-coingecko-with

from pycoingecko import CoinGeckoAPI
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import numpy as np

cg = CoinGeckoAPI()

data = cg.get_coin_market_chart_by_id(id='cap', vs_currency='usd', days=1, interval='minutely')
prices = data['prices'] 
print(prices)
for idx, price in enumerate(prices):
    print(idx, price)

#timestamps = [datetime.utcfromtimestamp(row[0]/1000).strftime('%Y-%m-%d %H:%M:%S') for row in prices]
timestamps = [row[0] for row in prices]

searchd = 1669395087796
formattedSearchd = datetime.utcfromtimestamp(searchd/1000).strftime('%Y-%m-%d %H:%M:%S')
#res = min(timestamps, key=lambda sub: abs(sub - searchd))

index = np.argmin(np.abs(np.array(timestamps)-searchd))
value = timestamps[index] # here is your result
formattedValue = datetime.utcfromtimestamp(value/1000).strftime('%Y-%m-%d %H:%M:%S')

print(formattedSearchd)
print(index, formattedValue)
# fig, ax = plt.subplots()
# fig.set_size_inches(8,6)
# ax.plot([datetime.utcfromtimestamp(x[0]/1000) for x in chartCap['prices']], 
#         [x[1] for x in chartCap['prices']], label='CAP')
# # ax.plot([datetime.utcfromtimestamp(x[0]/1000) for x in chartGmx['prices'] ], 
# #          [x[1] for x in chartGmx['prices']], label='GMX')
# ax.set_xlabel('Hours')
# ax.set_ylabel('Price *US$)')
# ax.legend()
# plt.show()
# plt.savefig('books_read.png')