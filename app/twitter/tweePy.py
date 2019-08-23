import pytz
import tweepy
from tweepy.auth import OAuthHandler

from env.Lib.warnings import catch_warnings
from ..models import *
import datetime
from django.db.models import Max

GET_TOTAL_TWEET_COUNT = 1000
API_RATE_LIMIT_TIME_MINUTES = 15


CONSUMER_KEY = 'tyF1ycXulIkEG44EEaNre8H9M'
CONSUMER_SECRET = 'NOHXnBFB2FLwdKEIinHvZzkihAcJgPL0ibGUpYaKGz9B5qNUL3'

ACCESS_TOKEN = '1073823523540324352-x6RimeEQ73i0YFkUqssrp2Q5g2P7Dl'
ACCESS_TOKEN_SECRET = 'AqjyPJxFq099h8h1qnURFKA7nTQ17VrI4XmaqryPoj3Dc'


def user_tweets():
    api = get_twitter_api()
    tweets = api.home_timeline(count=GET_TOTAL_TWEET_COUNT)
    return tweets


def get_twitter_api():
    auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    return tweepy.API(auth)


def save_to_db():
    original_tweets = user_tweets()
    insert_date = datetime.datetime.now()
    new_tweets = []
    for original_tweet in original_tweets:
        if not original_tweet.retweeted:
            if not Tweet.objects.filter(uuid=original_tweet.id):
                new_tweet = Tweet(uuid=original_tweet.id,
                                  text=original_tweet.text,
                                  date=original_tweet.created_at,
                                  insert_date=insert_date
                                  )
                new_tweets.append(new_tweet)

    print("NEW Tweets: " + str(len(new_tweets)))
    Tweet.objects.bulk_create(new_tweets)


def get_tweets():
    if is_safe_to_call_twitter_api():
        save_to_db()

    return Tweet.objects.order_by('-insert_date')[:10]


def get_last_inserted_date_time():
    return Tweet.objects.aggregate(recent=Max('insert_date')).get('recent')


def is_safe_to_call_twitter_api():
    # I can only fire 15 request in 15 minutes. so I need to be
    # defensive. When I can call I will collect massive amount of data.
    # then for 15 minutes I will accept the request but will not call
    # twitter api, instead I will render data from cache.
    last_inserted_time = get_last_inserted_date_time().replace(tzinfo=pytz.UTC)
    now = datetime.datetime.now().replace(tzinfo=pytz.UTC)
    time_delta = datetime.timedelta(minutes=API_RATE_LIMIT_TIME_MINUTES)

    safe = now - time_delta > last_inserted_time
    if safe:
        print("CALLING API")
    else:
        print("USING CACHE")

    return safe
