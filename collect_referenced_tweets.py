import requests
from ruamel import yaml
import gc
import csv
import os
import time
import pandas as pd
import time
import tweepy 
from twython import Twython

def load_experiment(path_to_experiment):
    """load experiment"""
    data = yaml.safe_load(open(path_to_experiment))
    return data



class CollectReference:
    """collect parent posts """

    def __init__(self, datapath, outputPath, handlesFile, outputFile):
        '''define the main path'''
        self.inputP = datapath# input path
        self.outputP = outputPath# output path
        self.handlesFile = handlesFile
        self.outputFile = outputFile
      
    def read_handles(self, handlesFile):
        """Read handle files"""

        handles = pd.read_csv(outputP + self.handlesFile)
       
        return handles

    def activate_api(self, env):
        """read API info"""

        CONSUMER_KEY = env['twitter_api2']['consumer_key']
        CONSUMER_SECRET = env['twitter_api2']['consumer_secret']
        OAUTH_TOKEN = env['twitter_api2']['access_token']
        OAUTH_TOKEN_SECRET = env['twitter_api2']['access_token_secret']
   
        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
        api = tweepy.API(auth)

        return api


    def big_loop(self, env):

        api = self.activate_api(env)
        handles = self.read_handles(self.handlesFile)

        file_exists = os.path.isfile(self.outputP + '{}.csv'.format(self.outputFile))

        if not file_exists:
            f = open(self.outputP + '{}.csv'.format(self.outputFile), 'a', encoding='utf-8-sig')
            writer_top = csv.writer(f, delimiter=',', quoting=csv.QUOTE_MINIMAL)
            writer_top.writerow(["reference_text"] + ["tweet_id"] + ["created_at"] + ["retweet_count"] + ['like_count'] + ['reply_tweet_id'] + ['reference_author'] + ['handle'])
            f.close()

        # query user profile for each handle
        if file_exists:

            count = 0
            for tweet_id, company in zip(handles['tweet_id'], handles['account_name']):
                print(tweet_id)

                f = open(self.outputP + '{}.csv'.format(self.outputFile), 'a', encoding='utf-8-sig')
                writer_top = csv.writer(f, delimiter=',', quoting=csv.QUOTE_MINIMAL)

                try:
                    #get the reference_id from tweet
                    tweet = api.get_status(tweet_id) 
                    referenced_id = tweet.in_reply_to_status_id 
                    # get status according to reference id
                    reference_tweet = api.get_status(referenced_id)

                    content = [[reference_tweet.text, reference_tweet.id, reference_tweet.created_at, reference_tweet.retweet_count, reference_tweet.favorite_count, tweet_id, reference_tweet.author.name, reference_tweet.author.screen_name]]

                    writer_top.writerows(content)
                    count = count + 1

                except tweepy.TweepError:
                    pass

                f.close()

                if count == 100:
                
                    time.sleep(10)
                    count = 0

                


evn_path = '/disk/data/share/s1690903/collect_tweets_Ewelina/environment/'
env = load_experiment(evn_path + 'env.yaml')


inputP = '/disk/data/share/s1690903/collect_tweets_Ewelina/data/'
outputP = '/disk/data/share/s1690903/collect_tweets_Ewelina/data/tweets/'
handles = 'all_tweets_finance_health.csv'

handlesFile = 'all_tweets_finance_health.csv'
outputFile = 'all_reference_tweets'

lf = CollectReference(datapath=inputP, outputPath=outputP, handlesFile=handlesFile, outputFile=outputFile)

lf.big_loop(env)





# CONSUMER_KEY = env['twitter_api2']['consumer_key']
# CONSUMER_SECRET = env['twitter_api2']['consumer_secret']
# OAUTH_TOKEN = env['twitter_api2']['access_token']
# OAUTH_TOKEN_SECRET = env['twitter_api2']['access_token_secret']
# twitter = Twython(
#     CONSUMER_KEY, CONSUMER_SECRET,
#     OAUTH_TOKEN, OAUTH_TOKEN_SECRET)


# auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
# auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
# api = tweepy.API(auth)

# #referenced_id = file['reference_tweet_id'][8172].astype('int64') 
# tweet = api.get_status(1340361765926948866)

# t = api.get_status(tweet.in_reply_to_status_id)
# print(t.text)





