import pandas as pd 
import collections
import text2emotion as te




class emotion_score:
    def __init__(self, inputP, outputP, filename, outputFile):
        '''define the main path'''
        self.inputpath = inputP# input path
        self.outputPath = outputP# output path
        self.filename = filename
        self.outputFile = outputFile

    def tweet_file(self):
        "Read tweet file"  

        file = pd.read_csv(self.inputpath + self.filename)
        file = file.head(1000)

        return file

    def tweet_emo(self):
        "Turn df file to dictionary"
        
        file = self.tweet_file()
        tweet_dict = collections.defaultdict(dict)
        for text, tweetid in zip(file['text'], file['tweet_id']):
            print(tweetid)
            #vader_score = analyser.polarity_scores(text)
            emo_score = te.get_emotion(text)
            tweet_dict[tweetid]["Angry"] = emo_score["Angry"]
            tweet_dict[tweetid]["Fear"] = emo_score["Fear"]
            tweet_dict[tweetid]["Happy"] = emo_score["Happy"]
            tweet_dict[tweetid]["Sad"] = emo_score["Sad"]
            tweet_dict[tweetid]["Surprise"] = emo_score["Surprise"]

        d = pd.DataFrame.from_dict(tweet_dict, orient='index')
        d['tweet_id'] = d.index
        d.to_csv(outputP + self.outputFile)

        return d


inputP = '/disk/data/share/s1690903/collect_tweets_Ewelina/data/tweets/'
outputP = '/disk/data/share/s1690903/collect_tweets_Ewelina/data/'
filename = 'all_tweets_IT.csv'
outputFile = 'emotion_score.csv'

r = emotion_score(inputP=inputP, outputP=outputP, filename=filename, outputFile=outputFile)

d = r.tweet_emo()

