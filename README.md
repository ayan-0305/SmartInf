# SmartInf
Find influential users in Twitter based on temporal sequence of retweets


#### **Required Packages**
* numpy
* scipy
* scikit-learn
* networkx

#### **Input and Output**
* Input graph: 'sample-follower-network.p' which is a dictionary containing the list of followers for a given user ID as key
* Input cascade time intervals: 'sample-time-intervals.txt' which is a text file containing cascade ID followed by consecutive inter-retweet time intervals for retweets in each line
* Input ordered user sequence for cascades: 'sample-cascade-sorted-user-sequence.txt' which is a text file containing cascade id followed by user IDS for retweeting users sorted based on timestamps of retweets in each line

* Output rankings: 'final-ranked-list-after-refinement-S.txt' which is a text file containing ranked list of user ids of influential users

#### **How To Run**
Run python files in this sequence:
* 'peak-and-fall-detection.py': Creates two dictionaries 'typeI-peakInd.p' and 'typeI-fallInd.p' storing the index of peak and fall indices in the sequence of inter-retweet time intervals for the cascade denoted by the key which is cascade ID
* 'SmartInf-Temp.py' : Creates the file 'ranked-list-T.txt' containing the ranked list of influential users, without applying refinement
* 'SmartInf.py' : Returns the final ranked list by refining the list given in ''ranked-list-T.txt'

#### **How To Crawl Tweets related to specific hashtags**
Use the folder 'twitter_crawler_scripts.zip'
* 'twitter-crawler.py': Used to download tweet metadata for messages containing specific hashtag eg. #IPL2018
* 'getAccessToken.py' : Used to get the set of Twitter API keys and access token required for Twitter crawling
* 'extract_tweet_details_json.py' : Used to store the detailed metadata of tweets crawled in csv format
