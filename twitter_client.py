import os
import sys
import config
from tweepy import API
from tweepy import OAuthHandler
def get_twitter_auth():
    '''
    Sets up Twitter Authentication.
    Returns tweety.OAuthHandler object
    '''
    try:
        consumer_key = os.environ['TWITTER_CONSUMER_KEY']
        consumer_secret = os.environ['TWITTER_CONSUMER_SECRET']
        access_token = os.environ['TWITTER_ACCESS_TOKEN']
        access_token_secret = os.environ['TWITTER_ACCESS_TOKEN_SECRET']
    except KeyError:
        sys.stderr.write("TWITTER_* environment variables not set\n")
        sys.exit(1)
    auth = OAuthHandler(config.consumer_key, config.consumer_secret)
    auth.set_access_token(config.access_token, config.access_token_secret)
    return auth

def get_twitter_client():
    '''
    Sets up Twitter API Client
    Returns tweepy.API object
    '''

    auth = get_twitter_auth()
    client = API(auth)
    return client

