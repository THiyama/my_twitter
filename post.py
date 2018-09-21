# coding: utf-8
from requests_oauthlib import OAuth1Session
import json
import key
from datetime import datetime

twitter = OAuth1Session(key.CONSUMER_KEY, key.CONSUMER_SECRET_KEY, key.ACCESS_TOKEN, key.ACCESS_TOKEN_SECRET)

time = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
params = {"status": "@mintomato__ hey ! Toru ! Training ended ! " + time}
req = twitter.post("https://api.twitter.com/1.1/statuses/update.json",params = params)

