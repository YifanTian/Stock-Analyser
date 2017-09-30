import re
import tweepy
from tweepy import OAuthHandler
from textblob import TextBlob
from pprint import pprint

def clean_tweet(tweet):
    '''
    Utility function to clean tweet text by removing links, special characters
    using simple regex statements.
    '''
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())


def get_tweet_sentiment(tweet):
    '''
    Utility function to classify sentiment of passed tweet
    using textblob's sentiment method
    '''
    # create TextBlob object of passed tweet text
    # print(clean_tweet(tweet))
    analysis = TextBlob(clean_tweet(tweet))
    # set sentiment
    if analysis.sentiment.polarity > 0:
        return 'positive'
    elif analysis.sentiment.polarity == 0:
        return 'neutral'
    else:
        return 'negative'


if __name__ == "__main__":
	# calling main function
    sentiment = get_tweet_sentiment('$NDAQ Says $AAPC is OK to Stay Listed Post-Merger!!! https://www.dailymarijuanaobserver.com/single-post')
    
    pprint(clean_tweet("$AAPC https://www.dailymarijuanaobserver.com/atlantic-alliance-partnership-aapc"))
    
    # print(sentiment)