import pytz
import tweepy
from tweepy.auth import OAuthHandler

from ..models import *
import datetime
from django.db.models import Max

from ..configuration import *


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
    media_list = []
    for original_tweet in original_tweets:
        if not original_tweet.retweeted:
            if not Tweet.objects.filter(uuid=original_tweet.id):
                # print(original_tweet)
                new_tweet = Tweet(uuid=original_tweet.id,
                                  text=original_tweet.text,
                                  date=original_tweet.created_at,
                                  insert_date=insert_date,
                                  user=original_tweet.user.screen_name
                                  )
                json = original_tweet._json
                # print("@@@@@@@@@@@@@@@@@@@@@@@@@@@")
                # print(json)
                # print("@@@@@@@@@@@@@@@@@@@@@@@@@@@")
                if 'extended_entities' in json:
                    # print(original_tweet._json)

                    for media in json['extended_entities']['media']:
                        if media['type'] == 'video':

                            new_media = Media(media_url=media['video_info']['variants'][0]['url'],
                                              media_type=media['type'],
                                              tweet_id=original_tweet.id,
                                              medium_width=media['sizes']['medium']['w'],
                                              medium_height=media['sizes']['medium']['h'],
                                              )

                        else:

                            new_media = Media(media_url=media['media_url'],
                                              media_type=media['type'],
                                              tweet_id=original_tweet.id,
                                              medium_width=media['sizes']['medium']['w'],
                                              medium_height=media['sizes']['medium']['h']
                                              )
                        media_list.append(new_media)
                new_tweets.append(new_tweet)

    print("NEW Tweets: " + str(len(new_tweets)))
    print("NEW Media: " + str(len(media_list)))

    Tweet.objects.bulk_create(new_tweets)
    Media.objects.bulk_create(media_list)


def get_media(page):
    if is_safe_to_call_twitter_api():
        save_to_db()

    limit = TWEETS_PER_PAGE
    offset = page * TWEETS_PER_PAGE
    return Media.objects.order_by('-id')[offset:offset + limit]


def get_tweets(page):
    if is_safe_to_call_twitter_api():
        save_to_db()

    limit = TWEETS_PER_PAGE
    offset = page * TWEETS_PER_PAGE
    return Tweet.objects.order_by('-insert_date')[offset:offset + limit]


def get_last_inserted_date_time():
    return Tweet.objects.aggregate(recent=Max('insert_date')).get('recent')


def is_safe_to_call_twitter_api():
    # I can only fire 15 request in 15 minutes. so I need to be
    # defensive. When I can call I will collect massive amount of data.
    # then for 15 minutes I will accept the request but will not call
    # twitter api, instead I will render data from cache.
    safe = True
    if get_last_inserted_date_time() is not None:
        last_inserted_time = get_last_inserted_date_time().replace(tzinfo=pytz.UTC)
        now = datetime.datetime.now().replace(tzinfo=pytz.UTC)
        time_delta = datetime.timedelta(minutes=API_RATE_LIMIT_TIME_MINUTES)

        safe = now - time_delta > last_inserted_time
        safe = False  # comment out this line whenever twitter is ready to unblock

    if safe:
        print("CALLING API")
    else:
        print("USING CACHE")

    return safe
