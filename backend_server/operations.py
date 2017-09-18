import json
import os
import pickle
import random
import redis
import sys

from bson.json_util import dumps
from datetime import datetime

# import common package in parent directory
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))

import mongodb_client
# import news_recommendation_service_client

from cloudAMQP_client import CloudAMQPClient

REDIS_HOST = "localhost"
REDIS_PORT = 6379

STOCKS_TABLE_NAME = "stocks-test1"
CLICK_LOGS_TABLE_NAME = 'click_logs'

STOCKS_LIMIT = 100
STOCKS_LIST_BATCH_SIZE = 20
USER_STOCKS_TIME_OUT_IN_SECONDS = 60

# LOG_CLICKS_TASK_QUEUE_URL = "amqp://erygdeea:mJdprUO-I6KpJNoyO18sx23FFQm1ouIX@donkey.rmq.cloudamqp.com/erygdeea"
# LOG_CLICKS_TASK_QUEUE_NAME = "tap-news-log-clicks-task-queue"

redis_client = redis.StrictRedis(REDIS_HOST, REDIS_PORT, db=0)
# cloudAMQP_client = CloudAMQPClient(LOG_CLICKS_TASK_QUEUE_URL, LOG_CLICKS_TASK_QUEUE_NAME)

def getStocksSummariesForUser(user_id, page_num):
    page_num = int(page_num)
    begin_index = (page_num - 1) * STOCKS_LIST_BATCH_SIZE
    end_index = page_num * STOCKS_LIST_BATCH_SIZE

    # The final list of news to be returned.
    sliced_stocks = []

    # if redis_client.get(user_id) is not None:
    #     stocks_digests = pickle.loads(redis_client.get(user_id))

    #     # If begin_index is out of range, this will return empty list;
    #     # If end_index is out of range (begin_index is within the range), this
    #     # will return all remaining news ids.
    #     sliced_stocks_digests = stocks_digests[begin_index:end_index]
    #     print sliced_stocks_digests
    #     db = mongodb_client.get_db()
    #     sliced_stocks = list(db[STOCKS_TABLE_NAME].find({'digest':{'$in':sliced_stocks_digests}}))
    # else:
    db = mongodb_client.get_db()
    total_stocks = list(db[STOCKS_TABLE_NAME].find().sort([('digest', -1)]).limit(STOCKS_LIMIT))
    total_stocks_digests = map(lambda x:x['digest'], total_stocks)

    redis_client.set(user_id, pickle.dumps(total_stocks_digests))
    redis_client.expire(user_id, USER_STOCKS_TIME_OUT_IN_SECONDS)

    sliced_stocks = total_stocks[begin_index:end_index]

    # print(sliced_stocks)
    result_stocks = []
    for stock in sliced_stocks:
        if 'history' in stock:
            if len(stock['history']) > 100:
                result_stocks.append(stock)

    # begin_index = (page_num - 1) * 3
    # end_index = page_num * 3
    # result_stocks = result_stocks[begin_index:end_index]

    # Get preference for the user
    # preference = news_recommendation_service_client.getPreferenceForUser(user_id)
    # topPreference = None

    # if preference is not None and len(preference) > 0:
    #     topPreference = preference[0]

    # for news in sliced_news:
    #     # Remove text field to save bandwidth.
    #     del news['text']
    #     if news['class'] == topPreference:
    #         news['reason'] = 'Recommend'
    #     if news['publishedAt'].date() == datetime.today().date():
    #         news['time'] = 'today'

    return json.loads(dumps(result_stocks))


# def logNewsClickForUser(user_id, news_id):
#     message = {'userId': user_id, 'newsId': news_id, 'timestamp': datetime.utcnow()}

#     db = mongodb_client.get_db()
#     db[CLICK_LOGS_TABLE_NAME].insert(message)

#     # Send log task to machine learning service for prediction
#     message = {'userId': user_id, 'newsId': news_id, 'timestamp': str(datetime.utcnow())}
#     cloudAMQP_client.sendMessage(message)
