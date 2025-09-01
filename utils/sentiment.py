from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd

vader_analyzer = SentimentIntensityAnalyzer()

def analyze_sentiment_textblob(comment):
    blob = TextBlob(comment)
    return{
        'polarity': blob.sentiment.polarity,
        'subjectivity': blob.sentiment.subjectivity
    }

def analyze_sentiment_vader(comment):
    scores = vader_analyzer.polarity_scores(comment)

    if scores['compound'] >= 0.05:
        sentiment = 'Positive'
    elif scores['compound'] <= -0.05:
        sentiment = 'Negative'
    else:
        sentiment = 'Neutral'
    return {**scores, 'sentiment': sentiment}

def process_comments():
    my_file = pd.read_csv("G:/My Drive/Amod Side Projects/Youtube Sentiment Analyzer/utils/YouTubeComments.csv", encoding='latin1')
    my_file['sentiment'] = my_file['comment'].apply(lambda x: analyze_sentiment_vader(x)['sentiment'])
    my_file['compound'] = my_file['comment'].apply(lambda x: analyze_sentiment_vader(x)['compound'])
    my_file.to_csv('G:/My Drive/Amod Side Projects/Youtube Sentiment Analyzer/utils/YouTubeComments_Sentiment.csv', index=False)
    print(f"Sentiment analysis complete.")
    return my_file
