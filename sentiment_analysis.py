#!pip install vaderSentiment
#import nltk
#nltk.download()
#!pip install textblob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
#from textblob import TextBlob
import pandas as pd

data = pd.read_csv("/content/archivo.csv")
data.columns

vader = SentimentIntensityAnalyzer()
data['sent_vader'] = data['tweets'].apply(lambda val: vader.polarity_scores(val)['compound'])
data[['tweets', 'sent_vader']].tail()

data[['tweets', 'sent_vader']].sort_values('sent_vader').head()

print(max(data.sent_vader))
print(min(data.sent_vader))

pos_neg = data[['tweets', 'sent_vader']].sort_values('sent_vader')

print(f'El comentario más negativo es:')
pos_neg.iloc[0,0]

print(f'El comentario más positivo es:')
pos_neg.iloc[-1,0]

