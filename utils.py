# -*- coding: utf-8 -*-
from config import config
import tweepy
import pyfscache

auth = tweepy.OAuthHandler(config['consumer_key'], config['consumer_secret'])
auth.set_access_token(config['access_token'], config['access_token_secret'])
api = tweepy.API(auth)

cache_result = pyfscache.FSCache('cache/tweets', days=1)

@cache_result
def getByHashtags(str):
    items = tweepy.Cursor(api.search, q=str).items(10)
    for item in items:
        print item.text.encode('utf-8')

# convert data to array for google api
def arrayify(object):
    result = [['Hashtag', 'Number']]
    for key in object:
        row = []
        row.append(key)
        row.append(object[key])
        result.append(row)
    return result

# count hashtags and store in a dict
def countHashtags(hashtags):
    counts = {}
    for ht in hashtags:
        counts[ht] = counts[ht] + 1 if ht in counts else 1
    return counts

#get hashtags of a user
def getHashtags(username, count=100):
    try:
        timeline = api.user_timeline(username, count=count)
    except:
        return []

    tweets_hashtag_dict_array = []
    for tweet in timeline:
        if tweet.entities.get('hashtags') != []:
            tweets_hashtag_dict_array.append(tweet.entities.get('hashtags'))

    hashtags = []
    for tweet_hashtag_dict_array in tweets_hashtag_dict_array:
        for tweet_hashtag_dict in tweet_hashtag_dict_array:
            hashtags.append(tweet_hashtag_dict['text'].encode('utf-8'))

    counts = countHashtags(hashtags)
    data = arrayify(counts)
    return data

#get tweets of a user
def getTweets(username):
    try:
        timeline = api.user_timeline(username, count=1000)
    except:
        return []

    for tweet in timeline:
        print tweet.text.encode('utf-8')
