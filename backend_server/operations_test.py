import operations
import os
import sys

from sets import Set

# import common package in parent directory
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))

import mongodb_client

# Start Redis and MongoDB before running following tests.

def test_getStocksSummariesForUser_basic():
    news = operations.getStocksSummariesForUser('test', 1)
    print news
    assert len(news) > 0
    print 'test_getStocksSummariesForUser_basic passed!'

def test_getStocksSummariesForUser_pagination():
    news_page_1 = operations.getStocksSummariesForUser('test', 1)
    news_page_2 = operations.getStocksSummariesForUser('test', 2)

    assert len(news_page_1) > 0
    assert len(news_page_2) > 0

    # Assert that there is no dupe news in two pages.
    digests_page_1_set = Set([news['index'] for news in news_page_1])
    digests_page_2_set = Set([news['index'] for news in news_page_2])
    assert len(digests_page_1_set.intersection(digests_page_2_set)) == 0

    print 'test_getNewsSummariesForUser_pagination passed!'

if __name__ == "__main__":
    test_getStocksSummariesForUser_basic()
    test_getStocksSummariesForUser_pagination()
