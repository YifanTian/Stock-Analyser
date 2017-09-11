
import requests
from pprint import pprint


# streams/symbol
# Returns the most recent 30 messages for the specified symbol. 
# Includes symbol object in response.
url = 'https://api.stocktwits.com/api/2/streams/symbol/AAPL.json'
r = requests.get(url).json()
pprint(r)


# Returns the most recent 30 messages with trending symbols in the last 5 minutes.
url = 'https://api.stocktwits.com/api/2/streams/trending.json'
r = requests.get(url).json()
pprint(r)
