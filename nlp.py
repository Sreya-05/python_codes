#nlp codes
#tokenisation

import nltk
from nltk.tokenize import word_tokenize
nltk.download("punkt")
nltk.download("punkt_tab")

text="hello hi how are you"
tokens=word_tokenize(text)
print(tokens)

#stop words
import nltk
from nltk.corpus import Stopwords
from nltk.tokenize import word_tokenize
nltk.download("punkt")
nltk.download("punkt_tab")
nltk.download("stopwords")
text=" this is a sample code written by abirami"
words=word_tokenize(text)
stop_words=set(stopwords.words("english"))
filtered_words=[word for word in words if word.lower() not in stop_words]
print("original:",text)
print("filtered:",filtered_words)

#stemming

from nltk.stem import PorterStemmer
stemmer=PorterStemmer()
words=["running","runner","easily","fairly"]
stemmed_words=[stemmer.stem(word)for word in words]
print("Stemmed words:",stemmed_words)

#lemmatisation
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
nltk.download("wordnet")
lemmatizer = WordNetLemmatizer()
words = ["running","eating","best","fairly"]
lemmatized_words = [lemmatizer.lemmatize(word,pos=wordnet.VERB)for word in words]
print("lemmatized_words:",lemmatized_words)

#parts fo speech tagging

import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag
nltk.download("punkt")
nltk.download("averaged_perceptron_tagger")
nltk.download("averaged_perceptron_tagger_eng")
sentence = "The quick brown fox jumps over the lazy dog."
tokens= word_tokenize(sentence)
tagged=pos_tag(tokens)
print(tagged)

#Sytax and parsing
exp = "5+3*3"
result=eval(exp)
print(result)

#Lowercasing
text = "Hello World"
lowercase_text = text.lower()
print(lowercase_text)

#remove a special characters
import re
def remove(text):
    return re.sub(r'[^A-Za-z0-9\s]',"",text)
i = "hello!@@#$$& world"
c = remove(i)
print(c)
