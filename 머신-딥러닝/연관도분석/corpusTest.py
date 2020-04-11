import nltk
import numpy as np
import pandas as pd
import glob
"""
nltk패키지를 받아줘야한다
"""
#nltk.download('punkt')
#nltk.download('averaged_perceptron_tagger')
github_path = glob.glob('C:/Users/dmdwn/OneDrive/바탕 화면/github/tripReviewAnalysisSystem/크롤러-전처리/원시자료/*.csv')

#C:\Users\dmdwn\OneDrive\바탕 화면\github\tripReviewAnalysisSystem\크롤러-전처리\sorting

dataset = []  #연관도 분석을 위한 데이터의 집합
p = 0 #dataset의 인덱스
for i in github_path:
    df = pd.read_csv(i, encoding = 'utf-8', engine='python', index_col = 0)
    #print(df)
    #print(df.columns)

    #토크나이징
    from nltk.tokenize import word_tokenize
    #print(df.text)
    #print(df.text[0]) #어떤 글인지 확인
    words = []

    for i in df.index:
        words += word_tokenize(df.text[i])

    #print(words)
    #품사 태깅, 단어들에 품사가 태깅 된다
    tagged = nltk.pos_tag(words)
    #명사 추출, 모든 단어 중 명사들이 추출 된다. (중복값 발생)
    allnoun = [word for word, pos in tagged if pos in ['NN', 'NNP']]

    #print(allnoun)
    """ 소문자화 
    lower_allnoun = []
    for word in allnoun:
        lower_allnoun += word.lower()
    
    print(lower_allnoun)
    
    # 왜 출력이 letter 별로 되는가?
    """
    from nltk import Text

    text = Text(allnoun) #nltk에 text 패키지 이용


    fd = text.vocab()
    print(fd.N()) #명사의 개수 출력
    numNoun = fd.N()
    if numNoun == 0:
        continue

    print(fd.most_common(5)) #가장 많이 등장한 단어 5가지 출력 (단어, 횟수)
    line = [] #임시 리스트
    for j in range(0, 5):
        line.append((fd.most_common(5)[j][0]))
    dataset.append(line)

"""연관도 분석을 위한 데이터 저장방법에 대한 고민
    어떻게 하는게 best인가? 
    1. 모든 글들을 새로운 데이터 프레임에 저장하여 정리(분류값, most_common-->가장 흔한 단어)
    2. 각각의 글들을 데이터베이스에 저장 후 비교
"""

"""
    추가적으로 간단하게 이것을 이용하여 대표 키워드를 뽑기는 쉽다. 예를 들어 museum, seoul, park 등의 키워드는 
    많은 반복을 보인다.
"""
print(dataset)

import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori

te = TransactionEncoder()
te_ary = te.fit(dataset).transform(dataset)
df = pd.DataFrame(te_ary, columns=te.columns_)
print(df.columns)
frequent_itemsets = apriori(df, min_support=0.5, use_colnames=True)
print(frequent_itemsets)
