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
yf_data = yqd.load_yahoo_quote('ABEO', '20170301', '20170830')
print(yf_data)
history = []
for i,day in enumerate(yf_data[1:-1]):
    data = day.split(',')
    print(data)
    print(str(data[0]),float(data[1]),float(data[2]),float(data[3]),float(data[4]),float(data[6]))
    history.append([i,str(data[0]),float(data[1]),float(data[2]),float(data[3]),float(data[4]),float(data[6])])

print(history)
