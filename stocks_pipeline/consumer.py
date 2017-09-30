from kafka import KafkaConsumer
import json

import datetime
import hashlib
import redis
import os
import sys
import json

import ast

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))

import mongodb_client
import yahoo_api_client
# from cloudAMQP_client import CloudAMQPClient

SLEEP_TIME_IN_SECONDS = 10
NEWS_TIME_OUT_IN_SECONDS = 3600 * 24 * 3

REDIS_HOST = 'localhost'
REDIS_PORT = 6379

redis_client = redis.StrictRedis(REDIS_HOST, REDIS_PORT)
# cloudAMQP_client = CloudAMQPClient(SCRAPE_NEWS_TASK_QUEUE_URL, SCRAPE_NEWS_TASK_QUEUE_NAME)

TWEETS_TABLE_NAME = "stocks-tweets"
db = mongodb_client.get_db()

# while True:                                            # we have to update stocks hourly

consumer = KafkaConsumer('AAPL')

while(True):
    for msg in consumer:
        # print(type(msg))
        # print(json.load(msg))
        # print(type(msg.value))
        # tweet = msg.value
        # tweet = ast.literal_eval("{'x':1, 'y':2}")
        tweet = ast.literal_eval(msg.value)
        # print(tweet)
        print(type(tweet))
        # print(tweet)
        tweet_digest = tweet['digist']
        tweet['digest'] = tweet_digest
        # ''' redis can dedupe here '''
        # # print(len(stock['history']))
        # # cloudAMQP_client.sendMessage(news)
        # # stock_json = json.dumps(stock)
        if len(list(db[TWEETS_TABLE_NAME].find().sort([('digest', -1)]))) > 200:
            db[TWEETS_TABLE_NAME].drop()
        db[TWEETS_TABLE_NAME].replace_one({'digest': tweet_digest}, tweet, upsert=True)

