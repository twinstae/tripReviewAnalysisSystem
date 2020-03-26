from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import accuracy_score
import pickle
import os
from time import time
import pandas as pd
import numpy as np
from mylib.tokenizer import tokenizer, tokenizer_porter
import nltk

github_path = 'C:/Users/dmdwn/OneDrive/바탕 화면/github/tripReviewAnalysisSystem/'
#engine='python' 을 넣어줘야 판다스가 한국어로 된 폴더명을 인식한다.

from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split


def model_tfidf(df, train_size, c_value):
    '''
    입력 : text와 sentiment가 포함된 리뷰들의 데이터 프레임
    출력 : 훈련이 끝난 분류기와 정확도를 리턴.
    '''

    X = df.loc[:, 'text'].values
    y = df.loc[:, 'sentiment'].values

    X_train, X_test, y_train, y_test = train_test_split(X, y,
                                                        test_size=1 - train_size,
                                                        random_state=14,
                                                        stratify=y)

    tfidf = TfidfVectorizer(lowercase=False, tokenizer=tokenizer)
    Ir_tfidf = Pipeline([('vect', tfidf), ('clf', LogisticRegression(C=c_value, penalty='l2', random_state=0, solver='liblinear'))])

    Ir_tfidf.fit(X_train, y_train)
    y_pred = Ir_tfidf.predict(X_test)
    test_accuracy = accuracy_score(y_test, y_pred)
    print('정확도: %.3f' % test_accuracy)

    return Ir_tfidf, test_accuracy


# 리뷰 리스트 불러오기기
file_list = os.listdir(github_path + '크롤러-전처리/원시자료/')

print("file_list: {}".format(file_list[:10]))

result = pd.read_csv(github_path + '크롤러-전처리/원시자료/' + file_list[0], encoding='utf-8', engine='python')
result.head()


def all_reviews(github_path, file_list, size):
    result = pd.read_csv(github_path + '크롤러-전처리/원시자료/' + file_list[0], encoding='utf-8', engine='python', index_col=0)
    stime = time()
    print('데이터 로딩 start')

    for file_path in file_list[:size]:
        new_data = pd.read_csv(github_path + '크롤러-전처리/원시자료/' + file_path, encoding='utf-8', engine='python',
                               index_col=0)
        # 새 데이터를 리스트로 합쳐서 concat시키면 행이 계속 추가 된다.
        # ignore_index로 기존 인덱스를  무시하고 합친 결과를 다시 인덱스해준다. 이거 안 하면 index must be monotonic increasing or decreasing 에러가 뜰 것이다.
        result = pd.concat([result, new_data], ignore_index=True, sort=False)

    print('데이터 로딩 종료: 소요시간 [%d]초' % (time() - stime))

    result['sentiment'] = np.where(result.star_point > 3, '1', '0')

    return result


data_all = all_reviews(github_path, file_list, len(file_list))
model = model_tfidf(data_all, train_size=0.7, c_value=1.0)

# 머신러닝 결과 파일로 저장(머신러닝 알고리즘을 계속 불러오지 않기 위하여)
curDir = os.getcwd()
dest = os.path.join(curDir, 'data', 'pklObject')
if not os.path.exists(dest):
    os.makedirs(dest)

path_save = os.path.join(dest, 'classifier.pkl')
pickle.dump(model, open(path_save, 'wb'), protocol=4)
print(path_save + '분류기 머신러닝 모델 저장 완료')
