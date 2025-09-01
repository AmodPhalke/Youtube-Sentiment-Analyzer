import plotly.express as px
import pandas as pd

def plot_sentiment_distribution(file_path="G:/My Drive/Amod Side Projects/Youtube Sentiment Analyzer/utils/YouTubeComments_Sentiment.csv"):
    df = pd.read_csv(file_path, encoding='latin1')
    fig = px.histogram(df, x='sentiment', color='sentiment',
                       title="YouTube Comments Sentiment Distribution",
                       text_auto=True,
                       color_discrete_map={'Positive':'green','Neutral':'blue','Negative':'red'})
    fig.show()
