import tweepy
import csv
import pandas as pd

####input your credentials here
consumer_key = 'r1PWmElzBiEMA2CGVSToqeau3'
consumer_secret = 'vfidRAc3xn4hxnMMeUC0nNoDOhzmc5pvEmu93vTTWT88aam2aS'
access_token = '1053031421319794688-LrvfrNzNwRBxDOH2Qka16dBlg2mupu'
access_token_secret = '99Agon5uWaFzpH96wd6OXzjqihZ3ugKWYCavkCBoJoFSY'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)
#####United Airlines
# Open/Create a file to append data
csvFile = open('microsoft.csv', 'a')
#Use csv Writer
csvWriter = csv.writer(csvFile)

for tweet in tweepy.Cursor(api.search,q="#AAPL",count=100,
                           lang="en",
                           since="2018-11-07").items():
    # print (tweet.created_at, tweet.text.encode('utf-8'))
    print(type(tweet))
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])
