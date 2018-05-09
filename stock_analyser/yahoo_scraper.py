# import requests
# from pprint import pprint

# url = 'https://query1.finance.yahoo.com/v10/finance/quoteSummary/ADP?formatted=true&crumb=ILlIC9tOoXt&lang=en-US&region=US&modules=upgradeDowngradeHistory%2CrecommendationTrend%2CfinancialData%2CearningsHistory%2CearningsTrend%2CindustryTrend%2CindexTrend%2CsectorTrend&corsDomain=finance.yahoo.com'
# r = requests.get(url).json()
# pprint(r)

# =====================

# import json
# from pprint import pprint
# from urllib.request import urlopen
# from urllib.parse import urlencode

import matplotlib.pyplot as plt

# def parse():
#     host   = 'https://query1.finance.yahoo.com'
#     #host   = 'https://query2.finance.yahoo.com'  # try if above doesn't work
#     path   = '/v10/finance/quoteSummary/%s' % 'ADP'
#     params = {
#         'formatted' : 'true',
#         #'crumb'     : 'ILlIC9tOoXt',
#         'lang'      : 'en-US',
#         'region'    : 'US',
#         'modules'   : 'earningsTrend',
#         'domain'    : 'finance.yahoo.com'
#     }

#     response = urlopen('{}{}?{}'.format(host, path, urlencode(params)))
#     data = json.loads(response.read().decode())

#     pprint(data)

# if __name__ == '__main__':
#     parse()

# ==========================================

import yqd
# yf_data = yqd.load_yahoo_quote('LABU', '201704013', '20180414')
# yf_data = yqd.load_yahoo_quote('JOBS', '201704013', '20180414')
# yf_data = yqd.load_yahoo_quote('AVGO', '201704013', '20180414')
# yf_data = yqd.load_yahoo_quote('JPM', '201704013', '20180414')
# yf_data = yqd.load_yahoo_quote('MGC', '201704013', '20180414')
# yf_data = yqd.load_yahoo_quote('BRK.B', '201704013', '20180414')
# yf_data = yqd.load_yahoo_quote('MILN', '201704013', '20180414')

# yf_data = yqd.load_yahoo_quote('V', '201704013', '20180414')
# yf_data = yqd.load_yahoo_quote('QQQC', '201704013', '20180414')
# yf_data = yqd.load_yahoo_quote('BAC', '201704013', '20180414')
# yf_data = yqd.load_yahoo_quote('GOOG', '201704013', '20180414')
# yf_data = yqd.load_yahoo_quote('SPLV', '201704013', '20180414')
# yf_data = yqd.load_yahoo_quote('BABA', '201704013', '20180414')
yf_data = yqd.load_yahoo_quote('ISRG', '201704013', '20180418')

# yf_data = yqd.load_yahoo_quote('FB', '201704013', '20180414')
# yf_data = yqd.load_yahoo_quote('AMZN', '201704013', '20180414')
# yf_data = yqd.load_yahoo_quote('AAPL', '201704013', '20180414')
# yf_data = yqd.load_yahoo_quote('INTC', '201704013', '20180414')
# yf_data = yqd.load_yahoo_quote('NVDA', '201704013', '20180414')
# yf_data = yqd.load_yahoo_quote('MSFT', '201704013', '20180414')


print(yf_data)
history = []
history1 = []
days = []
for i,day in enumerate(yf_data[1:-1]):
    data = day.split(',')
    print(data)
    print(str(data[0]),float(data[1]),float(data[2]),float(data[3]),float(data[4]),float(data[6]))
    history.append([i,str(data[0]),float(data[1]),float(data[2]),float(data[3]),float(data[4]),float(data[6])])
    days.append(i)
    history1.append(float(data[1]))

# print(history)
plt.plot(days, history1)
plt.show()
