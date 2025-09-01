import pandas as pd
import data

my_file = pd.read_csv("G:/My Drive/Amod Side Projects/Youtube Sentiment Analyzer/data/comments.csv")
df = pd.DataFrame(my_file)

print("Before Cleanup : ")

print("Size : ", df.size) #rxc
print("Shape : ", df.shape) #no of r & c
print("Columns : ", df.columns) #name of the columns

df_cleaned = df.dropna(subset=['name', 'comment', 'likes'])

print("After Cleanup : ")

print("Size : ", df_cleaned.size) #rxc
print("Shape : ", df_cleaned.shape) #no of r & c
print("Columns : ", df_cleaned.columns) #name of the colum

df_cleaned.to_csv("G:/My Drive/Amod Side Projects/Youtube Sentiment Analyzer/utils/YouTubeComments.csv", index=False)


