import requests
import json
from ruamel import yaml
import gc
import csv
import os
import time
import pandas as pd
import time


def load_experiment(path_to_experiment):
    """load experiment"""
    data = yaml.safe_load(open(path_to_experiment))
    return data

class GetConversation:
    """Collect replies via twitter api v2."""

    def __init__(self, inputP, outputP, bearer_token, tweet_fields, outputFile):
        '''define the main path'''
        self.inputP = inputP# input path
        self.outputP = outputP# output path
        #self.handlesFile = handlesFile
        self.bearer_token = bearer_token
        self.tweet_fields = tweet_fields
        self.outputFile = outputFile

    def search_conversation(self, query):
        """Define search twitter function."""
        #curl "https://api.twitter.com/2/tweets/search/all?query=from%3Atwitterdev&max_results=500&start_time=2020-01-01T00%3A00%3A00Z&end_time=2020-03-31T11%3A59%3A59Z"

        headers = {"Authorization": "Bearer {}".format(self.bearer_token)}

        url = "https://api.twitter.com/2/tweets/search/recent?query=conversation_id:{}&{}&start_time=2021-06-10T00%3A00%3A00Z".format(
            query, self.tweet_fields)

        response = requests.request("GET", url, headers=headers)

        #print(response.status_code)

        if response.status_code != 200:
            #raise Exception(response.status_code, response.text)
            time.sleep(60)
        return response.json()


evn_path = '/disk/data/share/s1690903/collect_tweets_Ewelina/environment/'
env = load_experiment(evn_path + 'env.yaml')


inputP = '/disk/data/share/s1690903/collect_tweets_Ewelina/data/'
outputP = '/disk/data/share/s1690903/collect_tweets_Ewelina/data/tweets/'
bearer_token = env['twitter_api']['bearer_token']
tweet_fields = "tweet.fields=text,author_id,created_at,conversation_id"
#in_reply_to_user_id
#conversation_id_file = 
outputFile = 'conversation'


c = GetConversation(inputP=inputP, outputP=outputP, bearer_token=bearer_token, tweet_fields=tweet_fields,outputFile=outputFile)

tweet = pd.read_csv(outputP + 'all_tweets_finance_health3.csv')

for cid in tweet.tweet_id.fillna(0).astype(int):
    print(cid)
    res = c.search_conversation(cid)
    print(res)


#1340360116806291712
# 1340352757962842112
#1279940000004973111

#headers = {"Authorization": "Bearer {}".format(bearer_token)}

# # url= 'https://api.twitter.com/2/tweets?ids=1225917697675886593&tweet.fields=author_id,conversation_id,created_at,in_reply_to_user_id,referenced_tweets&expansions=author_id,in_reply_to_user_id,referenced_tweets.id&user.fields=name,username'

#url =  'https://api.twitter.com/2/tweets/search/recent?query=conversation_id:1279940000004973111&tweet.fields=in_reply_to_user_id,author_id,created_at,conversation_id' 

# url = 'https://api.twitter.com/2/tweets/search/all?query=conversation_id:1340352757962842112&tweet.fields=created_at,source,entities,public_metrics&start_time=2010-01-01T00%3A00%3A00Z'

# response = requests.request("GET", url, headers=headers)

# res = response.json()








