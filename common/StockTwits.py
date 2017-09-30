
import requests
from pprint import pprint


# <type 'dict'>
# cursor
# symbol
# messages
# response

# streams/symbol
# Returns the most recent 30 messages for the specified symbol. 
# Includes symbol object in response.
url = 'https://api.stocktwits.com/api/2/streams/symbol/AAPL.json'
r = requests.get(url).json()
# print(type(r))
# print(r['response'])


# print(type(r['messages']))                      # list of tweets

# print(type('abc'.decode('utf-8')))

# print(r['messages'][0].keys()[0])

# print(r['messages'][1]['body'])


'''
# body_key = r['messages'].values()[0]

for item in r['messages']:
    # print(type(item))
    # print(item.keys())                          # u'body', u'mentioned_users', u'entities', u'links', u'conversation', u'created_at', u'reshares', u'symbols', u'source', u'user', u'id', u'likes'
    pprint(item['body'])
    pprint(item['created_at'])
    # pprint(item['user'])
    # pprint(item['id'])
    # try:
    #     pprint(item['likes'.decode('utf-8')])
    # except:
    #     pass
    print()
    # item[body_key]
    # print(item.values()[0])
'''

# for item in r:
#     print(r[item])
# pprint(r)












# Returns the most recent 30 messages with trending symbols in the last 5 minutes.
# url = 'https://api.stocktwits.com/api/2/streams/trending.json'
# r = requests.get(url).json()
# pprint(r)
