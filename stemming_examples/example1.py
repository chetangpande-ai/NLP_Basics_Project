import nltk
from nltk.stem import PorterStemmer
from collections import Counter

# Download required tokenizer
nltk.download('punkt')

text = "Running runners run and played playing plays"

# Tokenize text into words
words = nltk.word_tokenize(text.lower())

# Initialize stemmer
stemmer = PorterStemmer()

# Apply stemming
stemmed_words = [stemmer.stem(word) for word in words]

# Count stemmed words
word_counts = Counter(stemmed_words)

print("Original words:")
print(words)

print("\nStemmed words:")
print(stemmed_words)

print("\nWord counts after stemming:")
print(word_counts)
