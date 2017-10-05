import sched, time
import tweepy
from tweepy import OAuthHandler
import csv

starttime=time.time()
cycle = 1 #In seconds

consumer_key = "wUbmryhVmsqFalSszOn4h388N"
consumer_secret = "ZpNt8zNKdC6S5M2NgzIwKUQHG6I7PdWL1NQ8MQUzfHFeLNmtXe"
access_key = "1708970276-p2cXSOvSjRwNgUBtAqjOFx0sLB1dobykn7hTFZg"
access_secret = "yulCHpOFoiBKTu4tsKFYfJPHugcfM3zerFl6uhVhvXQkk"

# userID = "http://twitter.com/nytimes"
userID = "nytimes"

def TweetProcessor(username):

  auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
  auth.set_access_token(access_key, access_secret)
  api = tweepy.API(auth)

  number_of_tweets = 5

  tweets = api.user_timeline(screen_name=username, count=number_of_tweets)

  tweets_for_csv = [[username, tweet.id_str, tweet.created_at, tweet.text.encode("utf-8")] for tweet in tweets]
  # print(tweets_for_csv[0][2]-tweets_for_csv[1][2])

  print ("writing to {0}_tweets.csv".format(username))
  with open("{0}_tweets.csv".format(username), 'w+') as file:
    writer = csv.writer(file, delimiter='|')
    writer.writerows(tweets_for_csv)

TweetProcessor(userID)
#For repeating
# while True:
#   print ("tick")
#
#
#
#
#   time.sleep(cycle - ((time.time() - starttime) % cycle))