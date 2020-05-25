import nltk.stem, nltk.corpus, nltk.tokenize, re
import tomotopy as tp
import pandas as pd
import os
nltk.download('stopwords')

def data_text_cleaning(data):
    # 영문자 이외 문자는 공백으로 변환
    only_english = re.sub('[^a-zA-Z]', ' ', data)

    # 소문자 변환
    no_capitals = only_english.lower().split()

    # 불용어 제거
    stops = set(nltk.corpus.stopwords.words('english'))
    no_stops = [word for word in no_capitals if not word in stops]

    # 어간 추출
    stemmer = nltk.stem.SnowballStemmer('english')
    stemmer_words = [stemmer.stem(word) for word in no_stops]

    # 공백으로 구분된 문자열로 결합하여 결과 반환
    return stemmer_words
"""lemmatizing과 stemming의 차이  
http://blog.naver.com/PostView.nhn?blogId=vangarang&logNo=220963244354
stemmer를 통한 단어는 결과값에서 나오듯 city----> citi, 등 없는말을 만들어내기도 한다
이에 반에 lemmatizing은 단어 가 문장 속에서 어떤 품사로 쓰였는지 판단 가능하다.
"""
github_path = 'C:/Users/USER/Desktop/학교/참빛/tripReviewAnalysisSystem/'

file_list = os.listdir(github_path + '크롤러-전처리/원시자료/')

df = pd.read_csv(github_path + '크롤러-전처리/원시자료/' + file_list[1], encoding='utf-8', engine='python', index_col=0)
print(df['text'])
#토픽의 개수(k), alpha 파라미터, eta 파라미터, 말뭉치 최소 갯수(미만 제거)
model = tp.LDAModel(k=5, alpha=0.1, eta=0.01, min_cf=5)
for text in df['text']:
    model.add_doc(data_text_cleaning(text))  #전처리 결과 넣기

#간단한 num_words, num_vocab에 관하여 알기 위한 줄, 생략가능
model.train(0)
print('Total docs: ', len(model.docs))
print('Total words: ', model.num_words)
print('Vocab size: ', model.num_vocabs)

#200회 반복 동안 log값 기록 출력
for i in range(200):
    print('Iteration {}\tLL per word: {}'.format(i, model.ll_per_word))
    model.train(1)
#top_n -----> 토픽 별 상위 단어 갯수
for i in range(model.k):
    res = model.get_topic_words(i, top_n=10)
    print('Topic #{}'.format(i), end='\t')
    print(', '.join(w for w, p in res))
    
#5/26 이후 각종 가중치를 갖고 건들여 보기