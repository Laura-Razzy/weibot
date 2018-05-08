#!usr/bin/env python
# -*- coding utf-8 -*-
import tweepy, time, sys
import random

argfile = str(sys.argv[1])

#twitter info
from secrets import *
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

filename=open(argfile, 'r')
f=filename.readlines()
filename.close()

for line in f:
    api.update_status(line)
    time.sleep(30) #tweets x seconds (4h = 14400s) [1h = 3600s]