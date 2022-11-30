import tweepy
from private_key import secret_key, api_key, api_secret, access_key, access_secret
 
# fill the develop key from twitter develop
consumer_key = api_key
consumer_secret = api_secret
access_token = access_key
access_token_secret = access_secret
 
# submit your key and secret key
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
 
# get contain text post
api = tweepy.API(auth)

for tweets in api.search_tweets(q="PixelArtFilterWeb", lang="en"):
    print(tweets.text)
