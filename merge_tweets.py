import pandas as pd
import csv


"""Merging files """
class MergeReferenceTweet:
    """Merge reference tweet with reply tweets"""

    def __init__(self, inputP, tweetFile, reference_tweet, outputFileReference):
        '''define the main path'''
        self.inputP = inputP# inp
        self.tweets = pd.read_csv(inputP + tweetFile)
        self.reference_tweet = pd.read_csv(inputP + reference_tweet)
        self.outputFileReference = outputFileReference


    def merge_reference_tweet(self):
        
        # select useful columns
        tweets = self.tweets[['text', 'author_id', 'created_at',
       'conversation_id', 'tweet_id', 'retweet_count', 'reply_count',
       'like_count', 'quote_count', 'referenced_tweets_type', 'account_name']]
       # convert tweet id to int
        tweets.tweet_id = tweets.tweet_id.fillna(0).astype(int) 

        reference_tweet = self.reference_tweet.drop_duplicates(subset=['tweet_id'])
        reference_tweet = reference_tweet.rename(columns={'tweet_id': "reference_tweet_id", "created_at": "reference_create_at", "like_count": "reference_like_count", "handle": "reference_screen_name"}, errors="raise")

        all_df = tweets.merge(reference_tweet, left_on='tweet_id', right_on='reply_tweet_id', how = 'inner')

        all_df.to_csv(self.inputP + self.outputFileReference, encoding='utf-8-sig')

        return all_df

class MergeScores:
    """Merge scores with tweet file """

    def __init__(self, inputP, tweetFile, scoresFile, outputFile):
        '''define the main path'''
        self.inputP = inputP# inp
        self.tweets = pd.read_csv(inputP + tweetFile)
        self.scores = pd.read_csv(inputP + scoresFile)
        self.outputFile = outputFile


    def merge_score(self):
        """Merge scores with tweet file """
        tweets = self.tweets[['text', 'author_id', 'created_at',
       'conversation_id', 'tweet_id', 'retweet_count', 'reply_count',
       'like_count', 'quote_count', 'referenced_tweets_type', 'account_name', 'neg',
       'neu', 'pos', 'compound']]
       # convert tweet id to int
        tweets.tweet_id = tweets.tweet_id.fillna(0).astype(int)

        scores = self.scores
        scores.tweet_id = self.scores.tweet_id.fillna(0).astype(int) 

        all_df = tweets.merge(scores, left_on='tweet_id', right_on='tweet_id', how = 'inner')

        all_df.to_csv(self.inputP + self.outputFile, encoding='utf-8-sig')

        return all_df



inputP = '/disk/data/share/s1690903/collect_tweets_Ewelina/data/tweets/'
tweetFile = 'all_tweets_finance_health_scores.csv' #all tweets from the collected accounts
reference_tweet = 'all_reference_tweets.csv' # reference tweets from all_tweets_finance_health_final.csv
outputFileReference = 'merged_reference_tweets.csv'

m = MergeReferenceTweet(inputP=inputP, tweetFile=tweetFile, reference_tweet= reference_tweet, outputFileReference = outputFileReference)

mer_t = m.merge_reference_tweet()


##merging scores*******

# outputFile = 'all_tweets_finance_health_scores.csv'
# scoresFile = 'readability_score.csv'

# m2 = MergeScores(inputP=inputP, tweetFile=tweetFile, scoresFile=scoresFile, outputFile = outputFile)
# all_df = m2.merge_score()















