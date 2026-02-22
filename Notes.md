# NLP Hands‑On Guide using NLTK

A beginner‑friendly practical guide to learn Natural Language Processing step‑by‑step using Python and NLTK. Each section explains the concept briefly followed by a runnable example.

---

## 1. Roadmap To Learn NLP

NLP learning progresses from cleaning text → understanding grammar → converting text to numbers → building ML models. Master preprocessing first because every AI system depends on clean input data. Tools used: NLTK, sklearn, gensim.

**Example (setup):**

```bash
pip install nltk scikit-learn gensim
```

```python
import nltk
nltk.download('punkt')
```

---

## 2. Practical Usecases Of NLP

NLP allows computers to understand human language and extract meaning. It powers chatbots, sentiment analysis, spam detection, search engines, and recommendation systems. Almost every AI assistant today relies on NLP pipelines.

**Example:**

```python
text = "Flipkart delivery is very slow and support is useless"
# Expected: Negative sentiment + entity detection
```

---

## 3. Tokenization And Basic Terminologies

Tokenization splits text into sentences or words so machines can process it. It is the first step in any NLP pipeline because raw paragraphs cannot be analyzed directly. Tokens become input to later stages like stemming and POS tagging.

**Example:**

```python
from nltk.tokenize import sent_tokenize, word_tokenize
text = "NLP is amazing. I am learning it!"
print(sent_tokenize(text))
print(word_tokenize(text))
```

---

## 4. Tokenization Practicals

Tokenization handles punctuation and sentence boundaries automatically. It ensures models treat words like 'learning' and 'learning!' the same way. This improves model accuracy.

**Example:**

```python
text = "Hello world! NLP is fun."
print(word_tokenize(text))
```

---

## 5. Text Preprocessing – Stemming Using NLTK

Stemming reduces words to their base root by removing suffixes. It is fast but sometimes produces non‑dictionary words. Used in search engines where speed matters more than grammar correctness.

**Example:**

```python
from nltk.stem import PorterStemmer
stemmer = PorterStemmer()
print(stemmer.stem("studies"))
print(stemmer.stem("playing"))
```

---

## 6. Text Preprocessing – Lemmatization Using NLTK

Lemmatization converts words to proper dictionary form using grammar rules. It is slower but more accurate than stemming. Preferred in modern NLP pipelines.

**Example:**

```python
from nltk.stem import WordNetLemmatizer
import nltk
nltk.download('wordnet')
lemmatizer = WordNetLemmatizer()
print(lemmatizer.lemmatize("running"))
print(lemmatizer.lemmatize("better", pos='a'))
```

---

## 7. Stopwords, POS, Named Entity Recognition

Stopwords are common words removed to reduce noise. POS tagging identifies grammar roles like noun/verb, and NER detects names, places, and organizations. Together they convert text into structured information.

**Example:**

```python
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk

nltk.download('stopwords')
words = word_tokenize("Amazon opened office in Pune")
filtered = [w for w in words if w.lower() not in stopwords.words('english')]
print(filtered)

print(nltk.pos_tag(words))
```

---

## 8. Different Types Of Encoding (BoW & TF‑IDF)

Machines understand numbers, not words. Encoding converts text into vectors using word frequency (BoW) or importance score (TF‑IDF). These are traditional ML representations before embeddings.

**Example:**

```python
from sklearn.feature_extraction.text import CountVectorizer
corpus = ["I love NLP", "NLP is fun"]
cv = CountVectorizer()
print(cv.fit_transform(corpus).toarray())
```

---

## 9. Word Embedding – Word2Vec

Word2Vec creates dense vectors capturing meaning instead of just frequency. Similar words get similar vectors, enabling semantic understanding. Used in recommendation and similarity search.

**Example:**

```python
from gensim.models import Word2Vec
sentences = [["I","love","nlp"],["nlp","is","fun"]]
model = Word2Vec(sentences, vector_size=20, min_count=1)
print(model.wv.most_similar('nlp'))
```

---

## 10. Skip‑Gram Intuition

Skip‑gram predicts surrounding words from a target word to learn context. This helps embeddings understand relationships like king‑queen or car‑automobile. It captures semantics instead of spelling similarity.

**Example Concept:**
Input: love → Predict: I, NLP, learning

---

## 11. Average Word2Vec (Sentence Embedding)

Sentence embedding is created by averaging word vectors. This allows comparing whole sentences for similarity and clustering. Common in search engines and chatbots.

**Example:**

```python
import numpy as np

def sentence_vector(sentence, model):
    words = sentence.split()
    vectors = [model.wv[w] for w in words if w in model.wv]
    return np.mean(vectors, axis=0)

print(sentence_vector("i love nlp", model))
```

