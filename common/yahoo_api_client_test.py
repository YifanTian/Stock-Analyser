import yahoo_api_client as client

def test_basic():
    stocks = client.getStocksFromSource()
    # print(stocks)
    print(len(stocks))
    assert len(stocks) > 0
    print('test_basic passed')

if __name__ == '__main__':
    test_basic()