import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer
import string

# Download NLTK resources (only need to run this once)
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')

def preprocess_text(description):
    # Tokenize the text
    words = word_tokenize(description)

    # Remove stop words
    stop_words = set(stopwords.words('english'))
    words = [word for word in words if word.lower() not in stop_words]

    # Remove punctuation
    words = [word for word in words if word not in string.punctuation]

    # Perform stemming
    porter_stemmer = PorterStemmer()
    words = [porter_stemmer.stem(word) for word in words]

    # Perform lemmatization
    lemmatizer = WordNetLemmatizer()
    words = [lemmatizer.lemmatize(word) for word in words]

    # Join the processed words back into a string
    processed_text = ' '.join(words)

    return processed_text


