import tweepy
import datetime
import math
from settings import *

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

tweet_ids_with_replies = []


# grab mentions to get latest tweets to see if things were replied to
# edge case: fails to work if there are 100 mentions on other tweets within 5 minutes
# if this happens to you why are you using this script, also, sorry
mentions = api.search(q=username)
for mention in mentions:
    parent_id = mention.in_reply_to_status_id
    if parent_id:
        tweet_ids_with_replies.append(parent_id)
        if DEBUG:
            print "adding %s to tweets with one or more replies" % mention.text


public_tweets = api.user_timeline()
for tweet in public_tweets:
    lifetime = datetime.datetime.utcnow()-tweet.created_at
    minutes = math.floor(lifetime.total_seconds() / 60)
    
    engagements = tweet.favorite_count + tweet.retweet_count

    # tweet was a reply to another tweet
    if tweet.in_reply_to_status_id:
        engagements = engagements + 1

    # tweet had one or more replies
    if tweet.id in tweet_ids_with_replies:
        engagements = engagements + 1


    if DEBUG:
        print "--------"
        print tweet.id
        print tweet.text
        print "%d engagements after %d minutes" % (engagements, minutes)
        if tweet.id in tweet_ids_with_replies:
            print "has one or more replies!"

    if minutes<60 and minutes>=MINUTES_TO_LIVE and engagements==0:
        if DEBUG:
            print "DELETING " + str(tweet.id)
            print tweet.text            

        with open(DELETED_TWEETS_FILE, "a") as f:
            f.write( tweet.text.encode('utf8') )
            f.write("\n\n")

        if not DEBUG:
            api.destroy_status(tweet.id)
