from pymongo import MongoClient
from MyApp import constants
import tweepy
import pytumblr
import pymongo


#mongodb client connection
client = MongoClient(constants.mongo.CONN_STRING)
db = client.get_database(constants.mongo.DB_NAME)
twitterCol = db[constants.mongo.TWITTER_COL]
tumblerrCol = db[constants.mongo.TUMBLER_COL]

#twitter api connections
twitterAuth = tweepy.OAuthHandler(constants.twitter.CONSUMER_KEY,constants.twitter.CONSUMER_SECRET)
twitterAuth.set_access_token(constants.twitter.ACCESS_TOKEN, constants.twitter.ACCESS_TOKEN_SECRET)
twitterAPI = tweepy.API(twitterAuth,wait_on_rate_limit=True)

#tumbler API Connections

tumblrClient = pytumblr.TumblrRestClient(
    constants.tumblr.CONSUMER_KEY,
    constants.tumblr.CONSUMER_SECRET,
    constants.tumblr.OAUTH_TOKEN,
    constants.tumblr.OAUTH_TOKEN_SECRET
)

