

import pandas as pd
import csv


"""Merging files """
# class MergeReferenceTweet:
#     """Merge reference tweet with reply tweets"""

#     def __init__(self, inputP, tweetFile, reference_tweet, outputFileReference):
#         '''define the main path'''
#         self.inputP = inputP# inp
#         self.tweets = pd.read_csv(inputP + tweetFile)
#         self.reference_tweet = pd.read_csv(inputP + reference_tweet)
#         self.outputFileReference = outputFileReference


#     def merge_reference_tweet(self):
        
#         # select useful columns
#         tweets = self.tweets[['text', 'author_id', 'created_at',
#        'conversation_id', 'tweet_id', 'retweet_count', 'reply_count',
#        'like_count', 'quote_count', 'referenced_tweets_type', 'account_name']]
#        # convert tweet id to int
#         tweets.tweet_id = tweets.tweet_id.fillna(0).astype(int) 

#         reference_tweet = self.reference_tweet.drop_duplicates(subset=['tweet_id'])
#         reference_tweet = reference_tweet.rename(columns={'tweet_id': "reference_tweet_id", "created_at": "reference_create_at", "like_count": "reference_like_count", "handle": "reference_screen_name"})

#         all_df = tweets.merge(reference_tweet, left_on='tweet_id', right_on='reply_tweet_id', how = 'inner')

#         all_df.to_csv(self.inputP + self.outputFileReference, encoding='utf-8-sig')

#         return all_df

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

        # change which column you want to merge from the tweet file
        tweets = self.tweets[['text', 'author_id', 'created_at',
       'conversation_id', 'tweet_id', 'retweet_count', 'reply_count',
       'like_count', 'quote_count', 'referenced_tweets_type', 'account_name']]

       #tweets = self.tweets[['text', 'author_id', 'created_at',
       # 'conversation_id', 'tweet_id', 'retweet_count', 'reply_count',
       # 'like_count', 'quote_count', 'referenced_tweets_type', 'account_name', 'neu','neg','pos','compound']]
       # convert tweet id to int
        tweets.tweet_id = tweets.tweet_id.fillna(0).astype(int)

        scores = self.scores
        scores.tweet_id = self.scores.tweet_id.fillna(0).astype(int) 

        all_df = tweets.merge(scores, left_on='tweet_id', right_on='tweet_id', how = 'inner')

        #all_df.to_csv(self.inputP + self.outputFile, encoding='utf-8-sig')

        return all_df


class MergeAccounts:
    """Check which account is not collected."""
    def __init__(self, inputP, tweetFile, account_list, outputFile):
        '''define the main path'''
        self.inputP = inputP# 
        self.tweets = pd.read_csv(inputP + tweetFile)
        self.account_list = pd.read_csv(inputP + account_list)
        self.outputFile = outputFile

    def merge_accounts(self):

        #get unique account
        account_list = self.account_list

        tweets = self.tweets.drop_duplicates(subset=['account_name'])

        all_df = tweets.merge(account_list, left_on='account_name', right_on='company', how = 'inner')

        all_df.to_csv(self.inputP + self.outputFile, encoding='utf-8-sig')

        return all_df

    def check_missing_accounts(self):
        """check accounts that are missing in the data """

        tweets = self.tweets.drop_duplicates(subset=['account_name'])
        count = 0
        for i in self.account_list['company']:
            for j in tweets['account_name']:
                if i != j:
                    count = count + 1
            count_num = count
            print(count)
            count = 0
            # if count_num > 85:
            #     print(i)

class MergeTopicCount:
    """merge the topic labels."""
    def __init__(self, inputP, outputFile, tweet_path, tweet_file):
        '''define the main path'''
        self.inputP = inputP# 
        self.outputFile = outputFile
        self.tweet_path = tweet_path
        self.tweet_file = tweet_file

    def read_files(self, fileName):
 
        file = pd.read_csv(self.inputP + fileName,lineterminator='\n')
        file = file.iloc[:, [2, 3]]
        file.tweet_id = file.tweet_id.fillna(0).astype(int) 

        return file


    def merge_topic_count(self):
        """Merge all the topic scores """

        promotion = self.read_files('count_promotion_IT.csv')

        product = self.read_files('count_product_IT.csv')

        price = self.read_files('count_price_IT.csv')

        place = self.read_files('count_place_IT.csv')

        all_df = promotion.merge(self.tweet_file, on='tweet_id', how = 'outer')

        all_df = all_df.merge(product, on='tweet_id')

        all_df = all_df.merge(price, on='tweet_id')

        all_df = all_df.merge(place, on='tweet_id')

        all_df.to_csv(self.tweet_path + self.outputFile)

        return all_df

class MergeReferenceTweet:
    """merge the topic labels."""
    def __init__(self, inputP, outputFile, tweet_file, reference_file):
        '''define the main path'''
        self.inputP = inputP# 
        self.outputFile = outputFile
        self.tweet_file = tweet_file
        self.reference_file = reference_file

    def merge_reference_tweets(self):
        """merge reference tweets with tweet file"""
        company = pd.read_csv(self.inputP + self.tweet_file)
        company = company.drop_duplicates(subset=['tweet_id'])
        cleaned = company.dropna(subset=['reference_tweet_id'])
        cleaned.reference_tweet_id = cleaned.reference_tweet_id.astype(int)  

        reference_tweet = pd.read_csv(self.inputP + self.reference_file)
        reference_tweet.tweet_id = reference_tweet.tweet_id.astype(int) 
        reference_tweet = reference_tweet.rename(columns={'tweet_id': 'tweet_id_reference', 'conversation_id': 'conversation_id_reference', 'created_at':'created_at_reference', 'author_id': 'author_id_reference', 'text': 'text_reference'})

        all_df = cleaned.merge(reference_tweet, left_on = 'reference_tweet_id', right_on = 'tweet_id_reference', how='inner')

        all_df.to_csv(inputP + self.outputFile)


        return all_df




# inputP = '/disk/data/share/s1690903/collect_tweets_Ewelina/data/tweets/finance/'
# tweetFile = 'tweets_all_scores_finance.csv' #all tweets from the collected accounts
# reference_tweet = 'finance_reference_tweets.csv' # reference tweets from all_tweets_finance_health_final.csv
# outputFileReference = 'merged_company.csv'

# m = MergeReferenceTweet(inputP=inputP, tweetFile=tweetFile, reference_tweet= reference_tweet, outputFileReference = outputFileReference)

# mer_t = m.merge_reference_tweet()


##merging scores*******
# inputP = '/disk/data/share/s1690903/collect_tweets_Ewelina/data/tweets/'
# tweetFile = 'all_tweets_IT.csv' #all tweets from the collected accounts

# outputFile = 'all_tweets_IT_scores.csv'
# scoresFile = 'vader_score_IT.csv'

# m2 = MergeScores(inputP=inputP, tweetFile=tweetFile, scoresFile=scoresFile, outputFile = outputFile)
# all_score = m2.merge_score()


###merge accounts

# inputP = '/disk/data/share/s1690903/collect_tweets_Ewelina/data/tweets/'
# tweetFile = 'all_tweets_c_suit_company.csv' #all tweets from the collected accounts
# account_list = 'handle_c_suite.csv'
# outputFile = 'handlesssss.csv'

# m3 = MergeAccounts(inputP=inputP, tweetFile=tweetFile, account_list=account_list, outputFile = outputFile)

# all_df = m3.check_missing_accounts()

## merge topic count
# inputP = '/disk/data/share/s1690903/collect_tweets_Ewelina/data/topic_dictionary/'
# outputFile = 'tweets_all_IT_scores_topic.csv'
# tweet_path = '/disk/data/share/s1690903/collect_tweets_Ewelina/data/tweets/'

# m4 = MergeTopicCount(inputP=inputP, outputFile=outputFile, tweet_path=tweet_path, tweet_file = all_score)
# df = m4.merge_topic_count()

# promotion = m4.read_files('count_promotion_IT.csv')

# rslt_df = promotion.loc[promotion['promotion'] > 0]


# check reference tweets

inputP = '/disk/data/share/s1690903/collect_tweets_Ewelina/data/tweets/'
tweet_file = 'all_tweets_IT.csv' #all tweets from the collected accounts
reference_file = 'IT_reference_tweets.csv.csv' # reference tweets from all_tweets_finance_health_final.csv
outputFile = 'All_IT_tweets_reference.csv'

m5 = MergeReferenceTweet(inputP = inputP, outputFile = outputFile, tweet_file =tweet_file, reference_file=reference_file)

all_df = m5.merge_reference_tweets()






















