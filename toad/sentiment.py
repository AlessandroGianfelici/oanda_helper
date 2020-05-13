#modulo per sentiment analysis

import logging
from textblob import TextBlob
from textblob.sentiments import PatternAnalyzer
from toad.domain import NewsSentiment
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

#https://textblob.readthedocs.io/en/dev/api_reference.html#module-textblob.en.sentiment
def scoreSentiment(text):   
    opinion = TextBlob(text, analyzer=PatternAnalyzer())
    return opinion.sentiment

#new promising kid: https://pythonprogramming.net/sentiment-analysis-python-textblob-vader/
def scoreSentimentWithVader(text):
    vader = SentimentIntensityAnalyzer()
    return vader.polarity_scores(text)

def scoreSentimentNews(rawNewsWithId):
    if rawNewsWithId.content == "" or rawNewsWithId.content == None:
        logging.warn(f"NEWS {rawNewsWithId.id} has emprty content")
        return NewsSentiment(rawNewsWithId.id, 0, 0) 
    else:
        sentiment = scoreSentiment(rawNewsWithId.content)
        return NewsSentiment(rawNewsWithId.id, sentiment.polarity, sentiment.subjectivity)

if __name__ == '__main__':
    print(scoreSentimentWithVader("You are a stupid badass"))
    print(scoreSentimentWithVader("I have a lot of gold, I can buy whatever I want, life this way is really beautiful"))
