from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd 
import collections




class Vader_score:
    def __init__(self, inputP, outputP, filename):
        '''define the main path'''
        self.inputpath = inputP# input path
        self.outputPath = outputP# output path
        self.filename = filename

    def tweet_file(self):
        "Read tweet file"  

        file = pd.read_csv(self.inputpath + self.filename)
        

        return file

    def tweet_vader(self):
        "Turn df file to dictionary"

        analyser = SentimentIntensityAnalyzer()

        file = self.tweet_file()
        tweet_dict = collections.defaultdict(dict)
        for text, tweetid in zip(file['text'], file['tweet_id']):
            print(tweetid)
            vader_score = analyser.polarity_scores(text)
            tweet_dict[tweetid]["neg"] = vader_score['neg']
            tweet_dict[tweetid]["neu"] = vader_score['neu']
            tweet_dict[tweetid]["pos"] = vader_score['pos']
            tweet_dict[tweetid]["compound"] = vader_score['compound']

        d = pd.DataFrame.from_dict(tweet_dict, orient='index')
        d['tweet_id'] = d.index
        d.to_csv(outputP + 'vader_score.csv')

        return d


inputP = '/disk/data/share/s1690903/collect_tweets_Ewelina/data/tweets/'
outputP = '/disk/data/share/s1690903/collect_tweets_Ewelina/data/'
filename = 'all_tweets_finance_health_final.csv'

r = Vader_score(inputP=inputP, outputP=outputP, filename=filename)

d = r.tweet_vader()

