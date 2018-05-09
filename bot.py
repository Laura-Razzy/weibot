#!usr/bin/env python
# -*- coding utf-8 -*-
import tweepy
import time, sys, random
from random import uniform

argfile = str(sys.argv[1])

from secrets import * #secrets.py is the file with your credentials
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

filename=open(argfile, 'r')
f=filename.readlines()
filename.close()

for line in f:
    while True:
        try:
            api.update_status(random.choice(list(open(argfile))))
            time.sleep(uniform(7200, 21600)) #tweets every [7200, 21600]
        except tweepy.error.TweepError:
            pass