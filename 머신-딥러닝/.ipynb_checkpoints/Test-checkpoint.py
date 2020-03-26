from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import accuracy_score
import pickle
import os
from time import time
import pandas as pd
import numpy as np
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

df = pd.read_csv('C:/Users/dmdwn/OneDrive/바탕 화면/github/tripReviewAnalysisSystem/크롤러-전처리/원시자료/63 City.txt')
print(df.columns)
s1 = pd.Series(dtype=int)
df['sentiment'] = s1
df['sentiment'] = np.where(df.star_point > 3, '1', '0')

print(df.columns)
print(df.head())

from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import accuracy_score


X_train = df.loc[:56, 'text'].values
y_train = df.loc[:56, 'sentiment'].values #긍.부정
X_test = df.loc[57: ,'text'].values
y_test = df.loc[57: , 'sentiment'].values

tfidf = TfidfVectorizer(lowercase=False, tokenizer=tokenizer)
Ir_tfidf = Pipeline([('vect', tfidf), ('clf', LogisticRegression(C=10.0, penalty='l2', random_state=0))])

stime=time()
print('머신러닝 start')
Ir_tfidf.fit(X_train, y_train)
print('머신러닝 종료')

y_pred = Ir_tfidf.predict(X_test)
print('테스트 종료: 소요시간 [%d]초' %(time()-stime))
print('정확도: %.3f' %accuracy_score(y_test, y_pred))

#머신러닝 결과 파일로 저장(머신러닝 알고리즘을 계속 불러오지 않기 위하여)
curDir=os.getcwd()
dest = os.path.join(curDir, 'data', 'pklObject')
if not os.path.exists(dest):
    os.makedirs(dest)

pickle.dump(Ir_tfidf, open(os.path.join(dest, 'classifier.pkl'), 'wb'), protocol=4)
print('머신러닝 데이터 저장 완료')