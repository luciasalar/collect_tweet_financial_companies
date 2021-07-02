


# files description and data dictionary

* Please always use author_id, tweet_id to match the files, company name, account name is only for your reference. 

* Remove the duplicated tweet_ids after you read each file 

# tweet files:
## all_tweets_finance_health_final.csv  (1,546,567 lines, data from 93 accounts) 

*all the tweets from finance companies*

**Scores:**
* vader, readability are all in the same file*

### description: all the tweets from 93 accounts on the list. 

missing accounts:

Affiliated Managers Group Inc.
Berkshire Hathaway
Chubb Limited
Cincinnati Financial
Everest Re Group Ltd.
Huntington Bancshares
Intercontinental Exchange
Leucadia National Corp.
Loews Corp.
Marsh & McLennan
People's United Financial
Prudential Financial
S&P Global Inc.
Abbott Laboratories
Align Technology
Allergan
Celgene
Danaher
Envision Healthcare
HCA
IDEXX Laboratories
Laboratory
Mettler-Toledo International
Mylan
Patterson Companies
Perrigo Company
Stryker

## finance_health_reference_tweets.csv (extra, you can ignore this file)


## all_tweets_IT_scores_topic.csv 1,101,151 lines

*all the tweets from IT firms*

**Scores:**
* vader, keyword count all in one file*

missing accounts:

Alliance Data Systems
Alphabet A (ex Google)
Alphabet C (ex Google)
Amphenol
Apple
Applied Materials
CA
eBay
F5 Networks
Harris
IBM
KLA-Tencor
Micron Technology
Microsoft
Time Warner
Total System Services
Visa

## All_IT_tweets_reference.csv, all the referenced tweets from IT firms

text_reference: referenced text

text: text of the parent tweet

## all_tweets_airline.csv 

all tweets and conversation from airline companies, 
to do task: emotion

missing accounts: 

Alaska Air Group
American Airlines Group
United Airlines Holdings

## conversation_airline.csv 
conversation from airline companies, here we manage to collect all the conversations in a thread

## all_tweets_c_suit_company.csv 

all the tweets from the c-suite companies, 

missing accounts:

American Tower
Boeing Co.
Biogen
Berkshire Hathaway
Costco Wholesale Corp.
DuPont de Nemours Inc.
Danaher Corporation
The Walt Disney Company
Alphabet Inc. (Class A)
Linde plc
Medtronic plc
Microsoft
Raytheon Technologies
Simon Property Group
Tesla, Inc.
Visa Inc.

## all_tweets_c_suit_ceo.csv 

*all the tweets from the CEO, here the 'account_name' is the CEO name*

**scores**
Vader score, LIWC in separate file



## ceo_reference_tweets_all.csv, all the referenced tweets from the CEO,

to be determined: you need another script to match whether the retweet is from the CEO's company

**scores**
Vader score, LIWC in separate file

# variable descriptions for tweet file:

text: tweet

author_id: unique id of the post author

created_at: time when the post was created (UTC)

conversation_id: unique id of the conversation. You can group tweets according to conversation id to recover a conversation. However, you need a academic endpoint to query with the conversation id. Just fill in an extra form https://twarc-project.readthedocs.io/en/latest/twitter-developer-access/#step-2-apply-for-the-special-academic-access-v2-endpoint


tweet_id: unique id of the tweet, you may need to convert tweet id to integer before merging it astype(int)

retweet_count

reply_count

like_count

quote_count

in_reply_to_user_id: author of the parent post

referenced_tweets_type: is the parent post a quote or reply

reference_tweet_id: A list of Tweets this Tweet refers to. For example, if the parent Tweet is a Retweet, a Retweet with comment (also known as Quoted Tweet) or a Reply, it will include the related Tweet referenced to by its parent. *warning:I found this id doesn't match with the parent post id. What I did in the script was to use another lib to retreive the parent post id seperately. Therefore, please ignore this variable*

account_name: the name of the companies (see the Google spreadsheet)

***scores***

**vader scores** (both finance and IT firms) 
https://pypi.org/project/vaderSentiment/ 

neg: negative

pos: positive

neu: neutral 

compound: combined

***keyword count*** (only IT firms have this one, I compute the labels for finance as well but you can ignore it)

keyword count for various topics

promotion

price

product

place

*** readability *** Finance
https://pypi.org/project/textstat/

flesch_reading_ease:  The Flesch Reading Ease gives a text a score between 1 and 100, with 100 being the highest readability score. Scoring between 70 to 80 is equivalent to school grade level 8. 

# variable descriptions for reference tweet files

finance_health_reference_tweets.csv (extra, you can ignore this file)

All_IT_tweets_reference.csv, all the referenced tweets from IT firms

conversation_airline.csv, conversation from airline companies

ceo_reference_tweets_all.csv, all the referenced tweets from the CEO, you need another script to match whether the retweet is from the CEO's company

### description: all the parent tweets

reference_text: parent tweet

tweet_id

created_at

retweet_count

like_count

reply_tweet_id: parent tweet id if this tweet is a reply

reference_author: author name

handle: screen name of the author

# account profile

## handle_list_finance_health_profile.csv

## handle_list_IT_profile.csv

## handle_list_airline_profile.csv

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


















