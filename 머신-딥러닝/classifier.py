import pickle
import os
import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score
from mylib.vectorizer import vect

# 이후 클라시파이어에 넣을 것 테스트용
clf = pickle.load(open(os.path.join('./data/pklObject', 'classifier.pkl'), 'rb'))
label = {0: '부정적', 1: '긍정적'}
print(label[1])
while True:
    txt = input('리뷰를 작성하십시오: ')
    if txt == '':
        break

    example = [txt]
    prediction = clf.predict(example)
    print('예측 %s' % label[int(prediction[0])])
    print('확률: %.3f%%' % np.max(clf.predict_proba(example)))