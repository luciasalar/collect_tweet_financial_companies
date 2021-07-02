import requests
import json
from ruamel import yaml
import gc
import csv
import os
import time
import pandas as pd
from twarc.client2 import Twarc2
from twarc.expansions import ensure_flattened
import datetime 

##collect reference tweets
def load_experiment(path_to_experiment):
    """load experiment"""
    data = yaml.safe_load(open(path_to_experiment))
    return data

class GetConversation:
    """Collect replies via twitter api v2."""

    def __init__(self, inputP, outputP, bearer_token, outputFile, tweetFile):
        '''define the main path'''
        self.inputP = inputP# input path
        self.outputP = outputP# output path
        self.bearer_token = bearer_token
        self.outputFile = outputFile
        self.tweetFile = tweetFile


    def read_handles(self):
        """Read handle files"""

        handles = pd.read_csv(self.outputP + self.tweetFile)
        handles = handles.iloc[1101068::]
        cleaned = handles.drop_duplicates(subset=['tweet_id'])

        # drop rows that do not have referenced tweets
        cleaned = cleaned.dropna(subset=['reference_tweet_id'])


        return cleaned


    def search_tweet(self, id_list, t):
        """search conversation """
       
        start_time = datetime.datetime(2006, 3, 21, 0, 0, 0, 0, datetime.timezone.utc)
        end_time = datetime.datetime(2021, 6, 22, 0, 0, 0, 0, datetime.timezone.utc)
        #search_results = t.search_all(query="conversation_id:{}".format(conversation_id), start_time=start_time, end_time=end_time, max_results=500)
        search_results = t.tweet_lookup(id_list)

        return search_results

    def split(self, a, n):
        k, m = divmod(len(a), n)
        return (a[i*k+min(i, m):(i+1)*k+min(i+1, m)] for i in range(n))

    def loop_file(self):

        t = Twarc2(bearer_token=self.bearer_token)
        handles = self.read_handles()

        f = open(self.outputP + '{}.csv'.format(self.outputFile), 'a', encoding='utf-8-sig')
        writer_top = csv.writer(f, delimiter=',', quoting=csv.QUOTE_MINIMAL)

        #count = 0
        #for conversation_id, company in zip(handles['conversation_id'], handles['account_name']):

            #print(conversation_id)
        id_list = handles['reference_tweet_id']

        trunks = list(self.split(id_list, 20000))

        for trunk in trunks:
            print(trunk)

            search_results = self.search_tweet(trunk, t)


            for page in search_results:
                try:

                    for tweet in ensure_flattened(page):

                        
                            content = [[tweet['author_id'], tweet['conversation_id'], tweet['created_at'], tweet['text'], tweet['id']]]
                            print(content)

                            writer_top.writerows(content)
                            print(content)

                except ValueError:
                    continue

            time.sleep(10)

        # count = count + 1
        # if count == 10:
        #     print(count)

        #     time.sleep(5)
        #     count = 0

        f.close()


    def save_file(self):

        file_exists = os.path.isfile(self.outputP + '{}.csv'.format(self.outputFile))

        if not file_exists:
            f = open(self.outputP + '{}.csv'.format(self.outputFile), 'a', encoding='utf-8-sig')
            writer_top = csv.writer(f, delimiter=',', quoting=csv.QUOTE_MINIMAL)
            writer_top.writerow(['author_id'] + ['conversation_id'] + ['created_at'] + ['text'] +['tweet_id'])

            f.close()
            self.loop_file()

        if file_exists:
            self.loop_file()



evn_path = '/disk/data/share/s1690903/collect_tweets_Ewelina/environment/'
env = load_experiment(evn_path + 'env.yaml')

inputP = '/disk/data/share/s1690903/collect_tweets_Ewelina/data/'
outputP = '/disk/data/share/s1690903/collect_tweets_Ewelina/data/tweets/'
bearer_token = env['twitter_api']['bearer_token']
#tweet_fields = "tweet.fields=text,author_id,created_at,conversation_id"
tweetFile = 'all_tweets_IT.csv'
outputFile = 'IT_reference_tweets.csv'

c = GetConversation(inputP=inputP, outputP=outputP, bearer_token=bearer_token, tweetFile=tweetFile, outputFile=outputFile)

c.save_file()



# testing
# t = Twarc2(bearer_token=bearer_token)
# start_time = datetime.datetime(2012, 3, 21, 0, 0, 0, 0, datetime.timezone.utc)
# end_time = datetime.datetime(2021, 6, 22, 0, 0, 0, 0, datetime.timezone.utc)
# search_results = t.tweet_lookup([1409421390441336833, 1409421390441336833])

# for page in search_results:
#     for tweet in ensure_flattened(page):
#         print(tweet['author_id'], tweet['conversation_id'], tweet['created_at'], tweet['text'], tweet['id'], tweet['in_reply_to_user_id'])


#file = pd.read_csv(outputP + 'reference_tweets/IT_reference_tweets.csv.csv')
#file2 = pd.read_csv(outputP + 'all_tweets_IT.csv')
#file2.loc[file2['reference_tweet_id'] == 16951538681]


# 1271168584878886913
# 1272518460690640898










