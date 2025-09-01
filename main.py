from utils import sentiment, visualize

#Run sentiment analysis
df_sentiment = sentiment.process_comments()

#Visualize the results
visualize.plot_sentiment_distribution()
