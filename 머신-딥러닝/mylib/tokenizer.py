from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords
import nltk
nltk.download('stopwords')
porter = PorterStemmer()
stop = stopwords.words('english')

#공백으로 단어 분리
def tokenizer(text):
    return text.split()

# Porter Stemming 알고리즘을 이용해 단어 분리
def tokenizer_porter(text):
    return [porter.stem(word) for word in text.split()]
