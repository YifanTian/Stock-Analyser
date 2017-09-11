from yahoo_finance import Share
import yqd
import json

# yahoo = Share('AAPL')

# print(yahoo.get_open())

# print(yahoo.get_price())

# print(yahoo.get_trade_datetime())

# print(yahoo.get_historical('2014-04-25', '2014-04-29'))

# from pprint import pprint

# print(yahoo.get_historical('2017-04-25', '2017-04-29'))

import pandas as pd
data = pd.read_csv("/home/yifantian/Desktop/bittigercs503-1703/capstone1/common/nasdaq.csv", index_col=None, header=None)         # this might need update daily,weekly
data.columns=["Ticker"]
SORT_BY_TOP = 1                                                     # according to user or recommendation

# print(data.describe())
# data.columns=["Ticker"]
# print(type(data))

# for stock in data["Ticker"][:100]:
#     print(stock)
#     share = Share(stock)
#     print(share.get_open())
#     print(share.get_price())
#     print(share.get_trade_datetime())
#     print(share.get_volume())
#     print(share.get_avg_daily_volume())
#     print(share.get_days_high())
#     print(share.get_days_low())
#     print()

def getStocksFromSource(indexes=data, sortBy=SORT_BY_TOP):
    stocks = []

    for stock in data["Ticker"][:50]:
        try:
            print(stock)
            print(type(stock))
            yf_data = yqd.load_yahoo_quote(stock, '20170801', '20170830')
            # yf_data = yqd.load_yahoo_quote('ABEO', '20170712', '20170725')
            # print(yf_data)
            share = Share(stock)

            history = []
            for i,day in enumerate(yf_data[1:-1]):
                daily_data = day.split(',')
                history.append([i,str(daily_data[0]),float(daily_data[1])])

            # stock = {'index':stock}

            stock = {'index':stock,
                    'open':share.get_price(),
                    'price':share.get_price(),
                    'volume':share.get_volume(),
                    'trade_datetime':share.get_trade_datetime(),
                    'avg_daily_volume':share.get_avg_daily_volume(),
                    'history':history}
            # stock_json = json.dumps(stock)
            # print(type(stock_json))
            stocks.append(stock)
        except Exception as e:
            pass
    print(len(stocks))
    return stocks



# get_price()
# get_change()
# get_percent_change()
# get_volume()
# get_prev_close()
# get_open()
# get_avg_daily_volume()
# get_stock_exchange()
# get_market_cap()
# get_book_value()
# get_ebitda()
# get_dividend_share()
# get_dividend_yield()
# get_earnings_share()
# get_days_high()
# get_days_low()
# get_year_high()
# get_year_low()
# get_50day_moving_avg()
# get_200day_moving_avg()
# get_price_earnings_ratio()
# get_price_earnings_growth_ratio()
# get_price_sales()
# get_price_book()
# get_short_ratio()
# get_trade_datetime()
# get_historical(start_date, end_date)
# get_name()
# refresh()
# get_percent_change_from_year_high()
# get_percent_change_from_year_low()
# get_change_from_year_low()
# get_change_from_year_high()
# get_percent_change_from_200_day_moving_average()
# get_change_from_200_day_moving_average()
# get_percent_change_from_50_day_moving_average()
# get_change_from_50_day_moving_average()
# get_EPS_estimate_next_quarter()
# get_EPS_estimate_next_year()
# get_ex_dividend_date()
# get_EPS_estimate_current_year()
# get_price_EPS_estimate_next_year()
# get_price_EPS_estimate_current_year()
# get_one_yr_target_price()
# get_change_percent_change()
# get_dividend_pay_date()
# get_currency()
# get_last_trade_with_time()
# get_days_range()
# get_year_range()