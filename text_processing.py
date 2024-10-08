import re
import pandas as pd
from collections import Counter
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer

# Download stopwords if not already available
import nltk # type: ignore
nltk.download('stopwords')

stopwords_en = set(stopwords.words('english'))

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
        print(f"Error loading the file: {e}")
        return None

def preprocess_text(text_series):
    """Preprocesses the text by removing non-alphabetic characters, stopwords, and converting to lowercase."""
    # Convert to lowercase and remove non-alphabetic characters and digits
    text_series = text_series.str.lower().str.replace(r"[^\w\s]", " ").str.replace(r"\d", "")
    # Remove stopwords
    text_series = text_series.apply(lambda x: ' '.join([word for word in x.split() if word not in stopwords_en]))
    return text_series

def get_most_common_words(text_series, n=10):
    """Gets the 'n' most common words in the text."""
    words = ' '.join(text_series).split()
    counter = Counter(words)
    return counter.most_common(n)

def compute_bow(text_series):
    """Generates the BoW representation of the text."""
    vectorizer = CountVectorizer()
    bow_rep = vectorizer.fit_transform(text_series)
    return bow_rep, vectorizer.get_feature_names_out()

def main(file_path):
    # Load the data
    df = load_data(file_path)
    if df is None:
        return

    # Preprocess the text
    if 'Dialogue' in df.columns:
        df['preprocessed'] = preprocess_text(df['Dialogue'])
    else:
        print("The column 'Dialogue' does not exist in the file.")
        return

    # Get the most common words
    most_common = get_most_common_words(df['preprocessed'])
    print("Most common words:", most_common)

    # BoW Representation
    bow_rep, features = compute_bow(df['preprocessed'])
    df_bow = pd.DataFrame(bow_rep.toarray(), columns=features)
    print("Bag of Words representation:\n", df_bow)

# File path
file_path = 'path/to/your/dialogues.csv'
main(file_path)