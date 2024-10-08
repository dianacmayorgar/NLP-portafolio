import re
import pandas as pd
from collections import Counter

from nltk.corpus import stopwords
stopwords_sp = stopwords.words('spanish')

from sklearn.feature_extraction.text import CountVectorizer

df = pd.read_csv("G:/Mi unidad/NANI/_ESTUDIOS/_Especialización/Semestre 2/NLP/dialogos.csv")
df

texto = df['Locución']
texto = texto.str.lower()
texto = texto.str.replace(r"[\W\d]", " ") 
texto = texto.str.strip('()')

df['pre_procesado'] = texto

df['pre_procesado'] = df['pre_procesado'].str.split(' ').apply(lambda x: ' '.join(palabra for palabra in x if palabra not in stopwords_sp))
df

palabra = df.pre_procesado.values
counter = Counter(palabra)
mas_usadas = counter.most_common(10)
mas_usadas



count_vect = CountVectorizer()
bow_rep = count_vect.fit_transform(df.pre_procesado.values)
df['bow'] = [row for row in bow_rep.toarray()]
df



Cuando queremos tener más contexto y el orden. Por ejemplo, para trabajar con expresiones coloquiales que son compuestas, nombres de ciudades, entre otros.

South Park

