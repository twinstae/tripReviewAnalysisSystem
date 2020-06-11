import pandas as pd
import csv
import numpy as np
from collections import Counter
#warning창 끄기
pd.options.mode.chained_assignment = None
#tag
all_sel = ['shopping', 'walking', 'touring']
#데이터레임 생성
df = pd.DataFrame(data=np.arange(537).reshape(179, 3), columns=["names", "words", "tags"])


#테그 인풋 함수
def append_tags():
    global all_sel
    tag_sel = []
    print(all_sel)
    while True:
        tags = input("select tags: ")
        if tags == "":
            break
        tag_sel.append(tags)

    return tag_sel
#메인문
if __name__ == '__main__':
    n=0
    with open('keys_for_one_each.csv', 'r') as f:
        reader = csv.DictReader(f)

        for c in reader:
            for k, v in c.items():
                #print(k, v)
                df["names"][n] = k
                df["words"][n] = v
                print(k, v)
                tags = append_tags()
                df["tags"][n] = tags
                n+=1


    print(df)
    df.to_csv("tags.csv")