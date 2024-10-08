import pandas as pd
import numpy as np
import re
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
import nltk

# Descargar stopwords si no están disponibles
nltk.download('stopwords')
stopwords_en = set(stopwords.words("english"))

def load_data(file_path):
    """Loads the CSV file and returns a DataFrame."""
    try:
        df = pd.read_csv(file_path)
        print("File loaded successfully.")
        return df
    except FileNotFoundError:
        print("File not found. Please check the path.")
        return None
    except Exception as e:
        print(f"Error loading file: {e}")
        return None

def preprocess_text(text):
    """Preprocesses the text by converting to lowercase, removing non-alphabetic characters, and filtering stopwords."""
    text = text.lower()
    text = re.sub(r"[^\w\s]", " ", text)  # Remove non-alphabetic characters
    text = " ".join([word for word in text.split() if word not in stopwords_en])
    return text

def generate_wordcloud(text):
    """Generates and displays a word cloud from the given text."""
    wordcloud = WordCloud(width=800, height=400, max_font_size=150, max_words=100,
                          background_color="white", colormap="spring", stopwords=stopwords_en).generate(text)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.show()

def main(file_path):
    # Load the data
    data = load_data(file_path)
    if data is None:
        return

    # Preprocess the text column
    if 'text' in data.columns:
        data['preprocessed'] = data['text'].apply(preprocess_text)
    else:
        print("The 'text' column is not present in the file.")
        return

    # Combine all text for the word cloud
    combined_text = data['preprocessed'].str.cat(sep=" ")
    generate_wordcloud(combined_text)

# Path to your file
file_path = '/content/preprocessed_data.csv'
main(file_path)