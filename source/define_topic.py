import pandas as pd
import csv
import collections
import re


class getTopic:
    '''define topics of tweets according to keywords'''

    def __init__(self, inputP_tweet, inputP_dict, inputFile, label):
        
        self.inputP_tweet = inputP_tweet# inp
        self.inputP_dict = inputP_dict
        self.inputFile = inputFile
        #self.diction_file = diction_file
        self.label = label

    def read_tweet_file(self):
        # read label files

        file = pd.read_csv(self.inputP_tweet + self.inputFile)
        #file = file.head(1000)

        file_dict = collections.defaultdict(dict)

        for tweetid, text in zip(file['tweet_id'], file['text']):
            file_dict[tweetid] = text

        return file_dict


    def read_dictionary(self):
        """Read manual define diction """

        file = pd.read_csv(self.inputP_dict + '{}.csv'.format(self.label))

        return file


    def label_topic(self):
        """count occurences of topic words in a tweet """
        diction = self.read_dictionary()
        tweet_dict = self.read_tweet_file()

        count = 0
        count_dict = collections.defaultdict(dict)
        for key, tweet in tweet_dict.items():
            for word in diction.iloc[:, 0]:
                if word.lower() in tweet.lower().split():
                #if word in tweet.split():
                    count = count + 1

            # there's a bigram in promotion category, we need to seperate the computation
            if ((self.label == 'promotion') and (len(re.findall("social media", tweet.lower())) > 0)):
                count = count + 1

            count_dict[key]['text'] = tweet
            count_dict[key][self.label] = count

            if count_dict[key][self.label]> 0:
                print(tweet)

            count = 0

        df = pd.DataFrame.from_dict(count_dict, orient='index')
        df['tweet_id'] = df.index
        df.to_csv(inputP_dict + 'count_{}.csv'.format(self.label))

        return df


inputP_tweet = '/disk/data/share/s1690903/collect_tweets_Ewelina/data/tweets/'
inputP_dict = '/disk/data/share/s1690903/collect_tweets_Ewelina/data/topic_dictionary/'
inputFile = 'all_tweets_finance_health_final.csv'


# label = 'promotion'
# g = getTopic(inputP_tweet, inputP_dict, inputFile, label)
# promotion = g.label_topic()


# label = 'product' # dont lower keywords
# g = getTopic(inputP_tweet, inputP_dict, inputFile, label)
# product = g.label_topic() 

# label = 'price'
# g = getTopic(inputP_tweet, inputP_dict, inputFile, label)
# price = g.label_topic()

label = 'place'
g = getTopic(inputP_tweet, inputP_dict, inputFile, label)
place = g.label_topic()







































       
