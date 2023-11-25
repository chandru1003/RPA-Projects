import json
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer
import string

def preprocess_text(descriptions_json):
    descriptions = json.loads(descriptions_json)

    preprocessed_texts = []

    for description in descriptions:
        # Tokenize the text
        words = word_tokenize(description)

        # Remove stop words
        stop_words = set(stopwords.words('english'))
        words = [word for word in words if word.lower() not in stop_words]

        # Remove punctuations
        words = [word for word in words if word not in string.punctuation]

        # Perform stemming
        porter_stemmer = PorterStemmer()
        words = [porter_stemmer.stem(word) for word in words]

        # Perform lemmatization
        lemmatizer = WordNetLemmatizer()
        words = [lemmatizer.lemmatize(word) for word in words]

        # Join the processed words back into a string
        processed_text = ' '.join(words)
        preprocessed_texts.append(processed_text)

    return str(preprocessed_texts)
