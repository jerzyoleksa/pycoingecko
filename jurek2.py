#https://ecency.com/hive-169321/@steevc/extracting-data-from-coingecko-with

from pycoingecko import CoinGeckoAPI
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

cg = CoinGeckoAPI()

chartCap = cg.get_coin_market_chart_by_id(id='cap', vs_currency='usd', days=1, interval='minutely')

fig, ax = plt.subplots()
fig.set_size_inches(8,6)
ax.plot([datetime.utcfromtimestamp(x[0]/1000) for x in chartCap['prices']], 
        [x[1] for x in chartCap['prices']], label='CAP')
# ax.plot([datetime.utcfromtimestamp(x[0]/1000) for x in chartGmx['prices'] ], 
#          [x[1] for x in chartGmx['prices']], label='GMX')
ax.set_xlabel('Hours')
ax.set_ylabel('Price *US$)')
ax.legend()
plt.show()
plt.savefig('books_read.png')