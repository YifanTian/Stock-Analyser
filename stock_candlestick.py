

from yahoo_finance import Share
import yqd
import json
import os
import requests
import sys
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats.stats import pearsonr  

stock = 'ISRG'
yf_data = yqd.load_yahoo_quote(stock, '20180301', '20180830')

# print(yf_data)

high_prices = []
low_prices = []

open_prices = []
close_prices = []
volumes = []

print(yf_data[0])
for i, day in enumerate(yf_data[1:]):
    # print(i, day)
    day = day.split(',')
    if len(day) > 1:
        # print(day)
        prices = [float(price) for price in day[1:-1]]
        # print(prices)
        high_prices.append(max(prices))
        low_prices.append(min(prices))
        open_prices.append(prices[0])
        close_prices.append(prices[3])
        volumes.append(int(day[-1]))
    

days = [i for i in range(len(open_prices))]

stock_data = {"high_prices":low_prices, "low_prices": low_prices, "open_prices":open_prices, "close_prices": close_prices}

def check_Three_Line_Strike(price_data, days):
    """ give days, provide confidence of a pattern """
    pattern = [-1.5,-1,-0.5,3]
    corr_list = [0,0,0]
    for day in days[3:]:
        price_change = []
        for i in range(4):
            price_change.append(price_data["close_prices"][day-i] - price_data["open_prices"][day-i])
        
        corr = pearsonr(pattern,price_change)
        print(corr)
        corr_list.append(corr[0])
    return corr_list


corr_list = check_Three_Line_Strike(stock_data,days)

price_max = max(high_prices)
price_low = min(low_prices)
price_range = price_max - price_low
plt.plot((np.array(open_prices)-price_low)/price_range,label = 'open')
plt.plot((np.array(close_prices)-price_low)/price_range, label = 'close')
plt.plot((np.array(high_prices)-price_low)/price_range, label = 'high')
plt.plot((np.array(low_prices)-price_low)/price_range, label = 'low')



plt.plot(corr_list, label='corr')
plt.title('Three_Line_Strike')
plt.savefig('ISRG_Three_Line_Strike.pdf')
plt.legend()
plt.show()
