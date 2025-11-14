import nltk
from nltk.tokenize import word_tokenize

nltk.download('punkt')

text = "Experienced QA engineer skilled in automation, API testing, and NLP."
tokens = word_tokenize(text)

print(tokens)
