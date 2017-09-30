from yahoo_finance import Share
import yqd
import json
import os
import requests
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'sentiment'))

import nltk_service
import azure_sentiment_service

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

# ================================================ custom index sheet ==================

# data = [
# ]

data = [
    'AAPL',
    'AXP',
    'BA',
    'CAT',
    'CSCO',
    'CVX',
    'DIS',
    'DWDP',
    'GE',
    'GS',
    'HD',
    'IBM',
    'INTC',
    'JNJ',
    'JPM',
    'KO',
    'MCD',
    'MMM',
    'MRK',
    'MSFT',
    'NKE',
    'PFE',
    'PG',
    'TRV',
    'UNH',
    'UTX',
    'V',
    'VZ',
    'WMT',
    'XOM'
]

# f = open('/home/yifantian/Desktop/bittigercs503-1703/capstone1/common/stocks_success_index.txt','w')

def getStocksFromSource(indexes=data, sortBy=SORT_BY_TOP):
    ''' '''
    stocks = []
    index = ['AGTC']
    # for stock in data["Ticker"][:100]:
    # for stock in index:
    for stock in data:
        try:
            print(stock)
            # print(type(stock))
            yf_data = yqd.load_yahoo_quote(stock, '20170301', '20170830')
            # yf_data = yqd.load_yahoo_quote('ABEO', '20170712', '20170725')
            # print(yf_data)
            share = Share(stock)

            # history part
            history = []
            for i,day in enumerate(yf_data[1:-1]):
                daily_data = day.split(',')
                history.append([i,str(daily_data[0]),float(daily_data[1]),float(daily_data[2]),float(daily_data[3]),float(daily_data[4]),float(daily_data[6])])
            
            # print(history)
            # comments part
            comments = []
            new_StockTwits_comments = []
            url = 'https://api.stocktwits.com/api/2/streams/symbol/{0}.json'.format(stock)
            print(url)
            try:
                r = requests.get(url).json()
                print(len(r['messages']))
                for message in r['messages']:
                    try:
                        new_tweet = {
                            'id': message['id'], 
                            'body': message['body'], 
                            'created_at': message['created_at'],
                            'core_body': nltk_service.clean_tweet(message['body']),
                            'nltk_sentiment': nltk_service.get_tweet_sentiment(message['body']),
                            # 'azure_sentiment': azure_sentiment_service.GetSentiment(message['body'])
                        }
                        try:
                            new_tweet['azure_sentiment'] = azure_sentiment_service.GetSentiment(message['body'])
                        except Exception as e:
                            new_tweet['azure_sentiment'] = 0.5
                            print(e)
                        # print(new_tweet['azure_sentiment'])
                        new_StockTwits_comments.append(new_tweet)
                    except Exception as e:
                        print(e)
                        # pass
            except Exception as e:
                print('stock tweets part problem')
                print(e)
            # new_StockTwits_comments = [{'id': message['id'], 'body': message['body'], 'created_at': message['created_at']} for message in r['messages']]

            print(len(new_StockTwits_comments))
            stock = {
                        'index':stock,
                        'open':share.get_open(),
                        'change':share.get_change(),
                        'percent_change':share.get_percent_change(),
                        'prev_close':share.get_prev_close(),
                        'price':share.get_price(),
                        'volume':share.get_volume(),
                        'history':history,
                        'new_StockTwits_comments':new_StockTwits_comments
                    }
            # stock_json = json.dumps(stock)
            # print(type(stock_json))
            print(len(history))
            if len(history) != 0:
                # f.write(stock['index']+'/n')
                stocks.append(stock)
        except Exception as e:
            print(e)
            pass
    print(len(stocks))
    return stocks

# f.close()

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