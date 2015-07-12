import tweepy
import datetime
import math
from settings import *

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


public_tweets = api.user_timeline()
for tweet in public_tweets:
    lifetime = datetime.datetime.utcnow()-tweet.created_at
    minutes = math.floor(lifetime.total_seconds() / 60)
    

    engagements = 0
    engagements = engagements + tweet.favorite_count + tweet.retweet_count
    if tweet.in_reply_to_status_id:
        engagements = engagements + 1

    if DEBUG:
        print "--------"
        print "%d engagements after %d minutes" % (engagements, minutes)

    if minutes<60 and minutes>=MINUTES_TO_LIVE and engagements==0:
        if DEBUG:
            print "DELETING " + str(tweet.id)
            print tweet.text            

        with open(DELETED_TWEETS_FILE, "a") as f:
            f.write( tweet.text.encode('utf8') )
            f.write("\n\n")

        if not DEBUG:
            api.destroy_status(tweet.id)
