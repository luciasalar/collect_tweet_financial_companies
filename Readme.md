# Collect Tweets

#Folders and Files

collect_tweets.py: collect max (N = 3200) tweets from user timeline using api v1, lib: tweepy, we use this script to collect **user profile**

collect_tweets_api2.py: collect all tweets from each account using api v2. This is a scrappy script, you need to adjust the sleep time if the limit rate has been changed

merge_files: merging tweet with parent tweets, merge tweet with Vader and readability score

collect_referenced_tweet: collect parent tweets

get_conversation: get conversation according to conversation id  **You need an academic endpoint to use this**
https://twarc-project.readthedocs.io/en/latest/twitter-developer-access/#step-2-apply-for-the-special-academic-access-v2-endpoint

env: environment folders, keys, model parameters. These files are in local dir

data: tweets, profile, comments

**The output files are stored in both Json and csv format, if in the later stage you need more variables for the csv format, you can always retrieve them from the Json dump**

# Data 

see data dictionary

# Retrieve timeline

The new API has advanced functions in searching tweets, you can break the 3200 cap. We are currently using *API v2.0*

Twitter recenlty lauched API v.2, the new api enable you to search tweets in a more precise way. For example, You can set  start_time and end_time and paginating through the full results.
https://developer.twitter.com/en/docs/twitter-api/tweets/timelines/introduction 

Unfortunately the library that are commonly used by many --Tweepy, doesn't support api2 yet. We can use scraping technqiues to do it, however, the tweepy library is way more convinient. collect_tweets_api2.py and collect_comments.py are using api v2



### User object
https://developer.twitter.com/en/docs/twitter-api/v1/data-dictionary/object-model/user
https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/tweet








