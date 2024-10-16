import pandas as pd

data = pd.read_csv("/content/preprocessed_data.csv")
data.columns


# In[13]:


#import nltk
#nltk.download('stopwords')

import numpy as np

from wordcloud import WordCloud, ImageColorGenerator

from nltk.corpus import stopwords
stopwords = stopwords.words("english")

import matplotlib.pyplot as plt
import PIL.Image
from IPython.display import display

import re 


# In[14]:


palabras = data.text.str.cat(sep=" ")
wordcloud = WordCloud().generate(palabras)


# In[15]:


def pre_procesado(texto):
    texto = texto.lower()
    texto = re.sub(r"[\W\d_]+", " ", texto)
    texto = [palabra for palabra in texto.split() if palabra not in stopwords]
    texto = " ".join(texto)
    return texto


# In[16]:


data['pp'] = data.text.apply(lambda texto: pre_procesado(texto))
data.head()


# In[17]:


palabras = data.pp.str.cat(sep=" ")
wordcloud = WordCloud(width=800, height=400,
                      max_font_size=150, max_words=100,
                      background_color="white", colormap="spring",
                      stopwords=stopwords).generate(palabras)


# In[18]:


plt.figure(figsize=(10,8))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.tight_layout(pad=0)
plt.show()

