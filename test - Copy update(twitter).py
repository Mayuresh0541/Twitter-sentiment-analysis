import tweepy,csv,re
from textblob import TextBlob
from matplotlib import pyplot as plt
import numpy as np

class TweeterSentiment:

    def __init__(self):
        self.tweets = []
        self.tweetText = []
    
    def downloadData(self):
        consumer_key = 'your consumer key'
        consumer_secret = 'consumer secret key'

        access_token = 'personal access token'
        access_token_secret = 'personal secret token'

        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

        auth.set_access_token(access_token,access_token_secret)

        api = tweepy.API(auth)

        search_term = input("Enter the keyword: => ")

        no_of_terms = int(input("Enter how many tweets you want to fetch => "))

        self.tweets = tweepy.Cursor(api.search,q=search_term,lang = 'en').items(no_of_terms)

        csv_file = open('test.csv','a')

        csv_writer = csv.writer(csv_file)

        polarity = 0
        neutral = 0
        weakly_positive = 0
        positive = 0
        strongly_positive = 0
        weakly_negative = 0
        negative = 0
        strongly_negative = 0

        for tweet in self.tweets:
            self.tweetText.append(self.cleantext(tweet.text).encode('utf-8'))
            analysis = TextBlob(tweet.text)

            polarity += analysis.sentiment.polarity
            
        csv_writer.writerow(self.tweetText)
        csv_file.close()

        total = polarity / no_of_terms


        if total == 0:
            neutral += 1
        if total > 0 and total <= 0.3 :
            weakly_positive += 1
        if total > 0.3 and total <= 0.6 :
            positive += 1
        if total > 0.6 and total <= 1 :
            strongly_positive += 1
        if total < 0 and total >= -0.3 :
            weakly_negative += 1
        if total < -0.3 and total >= -0.6 :
            negative += 1
        if total < -0.6 and total >= -1 :
            strongly_negative +=1

        var = ["strongly_negative", "negative", "weakly_negative", "neutral", "weakly_positive", "positive", "strongly_positive"]

        data = [strongly_negative, negative, weakly_negative, neutral, weakly_positive, positive, strongly_positive]

        fig = plt.figure(figsize =(10, 7)) 
        plt.pie(data, labels = var) 

        plt.show()


    def cleantext(self,tweet):
        return ' '.join(re.sub("(@[A-Za-z0-9]+) | (0-9A-Za-z \t) | (\w + :\ / \ / \S +)","",tweet).split())


if __name__ == "__main__":
    ts = TweeterSentiment()
    ts.downloadData()













