


# Files Description and Data Dictionary

* Please always use author_id, tweet_id to match the files, company name, account name is only for your reference. 

* Remove the duplicated tweet_ids after you read each file 

* the 'tweet_id' in a reference tweet file (path:/reference_conversation_tweets/) match with 'reference_tweet_id' in the tweet file (path:/tweet_file/), for example: all_tweets_IT_scores_topic.csv and All_IT_tweets_reference.csv, 'tweet_id' in all_reference_c_suit_cmo.csv match with 'reference_tweet_it' in 'all_tweets_c_suit_cmo.csv'
 
# File Description:

## Finance Health
### tweet_file/tweets_all_scores_final_finance.csv  (1,546,567 lines, data from 93 accounts) 

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

## IT tweets

### tweet_file/all_tweets_IT_scores_topic.csv 1,101,151 lines

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

### reference_conversation_tweets/IT_reference_tweets1.csv, referenced tweets from IT firms (part1)
### reference_conversation_tweets/IT_reference_tweets2.csv, referenced tweets from IT firms (part2)


text_reference: referenced text

text: text of the parent tweet

## Airline Tweets

### tweet_file/all_tweets_airline.csv 

all tweets and conversation from airline companies, 

**score** 

*emotion score on separate file* 

### emotion_score/emotion_all_tweets_airline.csv

missing accounts: 

Alaska Air Group
American Airlines Group
United Airlines Holdings

### reference_conversation_tweets/conversation_airline.csv 
conversation from airline companies, here we manage to collect all the conversations in a thread

**conversation is currently still being collected, I can run the emotion score on it once it's finished**

## C suite

### tweet_file/all_tweets_c_suit_company.csv 

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

### tweet_file/all_tweets_c_suit_ceo.csv 
### tweet_file/all_tweets_c_suit_cfo.csv (new)
### tweet_file/all_tweets_c_suit_cmo.csv (new)

*all the tweets from the CEO/CFO/CMO, here the 'account_name' is the CEO/CFO/CMO name*

**Scores:**

Vader score, LIWC in separate file

### vader_score/ceo_tweets_all_vader.csv 
### liwc/liwc_all_tweets_c_suit_ceo.csv

### vader_score/cmo_tweets_all_vader.csv (new)
### liwc/liwc_all_tweets_c_suit_cmo.csv (new)

### vader_score/cfo_tweets_all_vader.csv (new)
### liwc/liwc_all_tweets_c_suit_cfo.csv (new)

## Reference tweet for c-suit
### reference_conversation_tweets/ceo_reference_tweets_all.csv, all the referenced tweets from the CEO,

to be determined: you need another script to match whether the retweet is from the CEO's company

**Scores:**

Vader score, LIWC in separate file

### vader_score/ceo_tweets_reference_vader.csv
### liwc/liwc_ceo_reference_tweets_all.csv

### vader_score/cfo_tweets_reference_vader.csv (new)
### liwc/liwc_cfo_reference_tweets_all.csv (new)

### vader_score/cmo_tweets_reference_vader.csv (new)
### liwc/liwc_cmo_reference_tweets_all.csv (new)

## ceo missing accounts:
Nvidia Corporation
Oracle Corporation
Procter & Gamble
Philip Morris International
PayPal
Qualcomm
Raytheon Technologies
Southern Company
Simon Property Group
AT&T Inc.
Target Corporation
Thermo Fisher Scientific
Texas Instruments
UnitedHealth Group
Union Pacific Corporation
United Parcel Service
U.S. Bancorp
Visa Inc.
Walgreens Boots Alliance
Wells Fargo
Walmart
Exxon Mobil Corp.


## cfo missing accounts:

Philip Morris International
PayPal
Qualcomm
Raytheon Technologies
Starbucks Corp.
Southern Company
Simon Property Group
AT&T Inc.
Target Corporation
Thermo Fisher Scientific
Tesla, Inc.
Texas Instruments
UnitedHealth Group
Union Pacific Corporation
United Parcel Service
U.S. Bancorp
Visa Inc.
Verizon Communications
Walgreens Boots Alliance
Wells Fargo
Walmart
Exxon Mobil Corp.

## cmo missing accounts

Pfizer Inc.
Procter & Gamble
Philip Morris International
PayPal
Qualcomm
Raytheon Technologies
Starbucks Corp.
Southern Company
Simon Property Group
AT&T Inc.
Target Corporation
Thermo Fisher Scientific
Tesla, Inc.
Texas Instruments
UnitedHealth Group
Union Pacific Corporation
United Parcel Service
U.S. Bancorp
Walgreens Boots Alliance
Wells Fargo
Walmart
Exxon Mobil Corp.

# Variable Descriptions for Tweet File:

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

reference_tweet_id: A list of Tweets this Tweet refers to. For example, if the parent Tweet is a Retweet, a Retweet with comment (also known as Quoted Tweet) or a Reply, it will include the related Tweet referenced to by its parent. 

account_name: the name of the companies (see the Google spreadsheet)

**Scores:**

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

# Variable Descriptions for Reference Tweet Files

### description: all the parent tweets

reference_text: parent tweet

tweet_id

created_at

retweet_count

like_count

reply_tweet_id: parent tweet id if this tweet is a reply

reference_author: author name

handle: screen name of the author

# Account Profile 

Twitter Profile of the collected accounts 

### /account profiles

### handle_list_finance_health_profile.csv

### handle_list_IT_profile.csv

### handle_list_airline_profile.csv

### handle_c_suite.csv_profile_ceo.csv

### handle_c_suite.csv_profile.csv

## description: tweeter profile of the companies

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


















