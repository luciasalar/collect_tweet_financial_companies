

## Using converstation id to recover a conversation
You can group tweets according to conversation id to recover a conversation


# files description and data dictionary

##all_tweets_finance_health_final.csv  (1,546,567 lines) 

### description: all the tweets from the accounts on the list

### variables:

text: tweet

author_id: unique id of the post author

created_at: time when the post was created (UTC)

conversation_id: unique id of the conversation. You can group tweets according to conversation id to recover a conversation. However, you need a academic endpoint to query with the conversation id. Just fill in an extra form https://twarc-project.readthedocs.io/en/latest/twitter-developer-access/#step-2-apply-for-the-special-academic-access-v2-endpoint


tweet_id: unique id of the tweet

retweet_count

reply_count

like_count

quote_count

in_reply_to_user_id: author of the parent post

referenced_tweets_type: is the parent post a quote or reply

reference_tweet_id: A list of Tweets this Tweet refers to. For example, if the parent Tweet is a Retweet, a Retweet with comment (also known as Quoted Tweet) or a Reply, it will include the related Tweet referenced to by its parent. *warning:I found this id doesn't match with the parent post id. What I did in the script was to use another lib to retreive the parent post id seperately. Therefore, please ignore this variable*

account_name: the name of the companies (see the Google spreadsheet)

***scores***

**vader scores**

neg: negative

pos: positive

neu: neutral 

compound: combined

*** readability ***

flesch_reading_ease:  The Flesch Reading Ease gives a text a score between 1 and 100, with 100 being the highest readability score. Scoring between 70 to 80 is equivalent to school grade level 8. 

### all_reference_tweets.csv (x lines, still collecting) 

### description: all the parent tweets

reference_text: parent tweet

tweet_id

created_at

retweet_count

like_count

reply_tweet_id: parent tweet id if this tweet is a reply

reference_author: author name

handle: screen name of the author

## handle_list_finance_health_profile.csv

### description: tweeter profile of the companies

user_id: unique id for the company account

screen_name: handle

company: company name on the Google spreadsheet

location: location of the account

user_description

followers_count

friends_count

account_created

favourites_count

statuses_count

user_url

listed_count


















