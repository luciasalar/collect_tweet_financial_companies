import pandas as pd 
from readability import Readability
import textstat


class Readability_score:
    def __init__(self, inputP, outputP, filename):
        '''define the main path'''
        self.inputpath = inputP# input path
        self.outputPath = outputP# output path
        self.filename = filename

    def tweet_file(self):
        "Read tweet file"  

        file = pd.read_csv(self.inputpath + self.filename)
        #file = file.head(100)

        return file

    def tweet_readability(self):
        "Turn df file to dictionary"

        file = self.tweet_file()
        tweet_dict = {}
        for text, tweetid in zip(file['text'], file['tweet_id']):
            print(tweetid)
            readability_score = textstat.flesch_reading_ease(text)
            tweet_dict[tweetid] = readability_score

        d = pd.DataFrame.from_dict(tweet_dict, orient='index')
        d['tweet_id'] = d.index
        d.columns = ['flesch_reading_ease', 'tweet_id']
        d.to_csv(outputP + 'readability_score.csv')

        return d


inputP = '/disk/data/share/s1690903/collect_tweets_Ewelina/data/tweets/'
outputP = '/disk/data/share/s1690903/collect_tweets_Ewelina/data/'
filename = 'all_tweets_finance_health_final.csv'

r = Readability_score(inputP=inputP, outputP=outputP, filename=filename)

d = r.tweet_readability()


#text = 'Wikis are enabled by wiki software, otherwise known as wiki engines. A wiki engine'
#rea = textstat.flesch_reading_ease(text)

