
# import os
 
# os.system("curl --ftp-ssl anonymous:jupi@jupi.com "
#           "ftp://ftp.nasdaqtrader.com/SymbolDirectory/nasdaqlisted.txt "
#           "> nasdaq.lst")

# os.system("head -20 nasdaq.lst")
# print()

# os.system("tail -5 nasdaq.lst")
# print()

# os.system("tail -n +9 nasdaq.lst | cat | sed '$d' | sed 's/|/ /g' > "
#           "nasdaq.lst2")

# os.system("awk '{print $1}' nasdaq.lst2 > nasdaq.csv")
# os.system("echo; head nasdaq.csv; echo '...'; tail nasdaq.csv")

# import pandas as pd
# data = pd.read_csv("nasdaq.csv", index_col=None, header=None)
# # data.to_csv('./example.csv', index=False)

# data.columns=["Ticker"]
# # pd.DataFrame.to_csv('./nasdaq.csv')
# print(data)



# =====================================================

# from bs4 import BeautifulSoup
# import requests

# myurl = "http://finance.yahoo.com/q/cp?s=^DJI"
# # I use requests to get the html content
# html = requests.get(myurl).content
# soup = BeautifulSoup(html)

# # you don't need to iterate the children, just use find
# # and you need to use attrs { key: value }, not just 'time_rtq_ticker'
# list = soup.find('span', attrs={'class':'time_rtq_ticker'})

# ===========================================

#
# Simple Scraper for Dow Jones Industrial Average
# With Python 3
#
# INSTALLATION (with pyenv)
#   pyenv local 3.4.1
#   pip install requests
#   pip install beautifulsoup4
#   pip install https://github.com/syabro/soupselect/archive/master.zip
#
# USAGE
#   python ./djia.py
#


# =========================================================================

# data = [
#     'AAPL',
#     'AXP',
#     'BA',
#     'CAT',
#     'CSCO',
#     'CVX',
#     'DIS',
#     'DWDP',
#     'GE',
#     'GS',
#     'HD',
#     'IBM',
#     'INTC',
#     'JNJ',
#     'JPM',
#     'KO',
#     'MCD',
#     'MMM',
#     'MRK',
#     'MSFT',
#     'NKE',
#     'PFE',
#     'PG',
#     'TRV',
#     'UNH',
#     'UTX',
#     'V',
#     'VZ',
#     'WMT',
#     'XOM'
# ]