import numbers
import math


class GeoUtil:
    """
    Geographical Utils
    """

    @staticmethod
    def degree2radius(degree):
        return degree * (math.pi / 180)

    @staticmethod
    def get_harversion_distance(x1, y1, x2, y2, round_decimal_digits=5):
        """
        경위도 (x1,y1)과 (x2,y2) 점의 거리를 반환
        Harversion Formula 이용하여 2개의 경위도간 거래를 구함(단위:Km)
        """
        if x1 is None or y1 is None or x2 is None or y2 is None:
            return None
        assert isinstance(x1, numbers.Number) and -180 <= x1 and x1 <= 180
        assert isinstance(y1, numbers.Number) and -90 <= y1 and y1 <= 90
        assert isinstance(x2, numbers.Number) and -180 <= x2 and x2 <= 180
        assert isinstance(y2, numbers.Number) and -90 <= y2 and y2 <= 90

        R = 6371  # 지구의 반경(단위: km)
        dLon = GeoUtil.degree2radius(x2 - x1)
        dLat = GeoUtil.degree2radius(y2 - y1)

        a = math.sin(dLat / 2) * math.sin(dLat / 2) \
            + (math.cos(GeoUtil.degree2radius(y1)) \
               * math.cos(GeoUtil.degree2radius(y2)) \
               * math.sin(dLon / 2) * math.sin(dLon / 2))
        b = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        return round(R * b, round_decimal_digits)

    @staticmethod
    def get_euclidean_distance(x1, y1, x2, y2, round_decimal_digits=5):
        """
        유클리안 Formula 이용하여 (x1,y1)과 (x2,y2) 점의 거리를 반환
        """
        if x1 is None or y1 is None or x2 is None or y2 is None:
            return None
        assert isinstance(x1, numbers.Number) and -180 <= x1 and x1 <= 180
        assert isinstance(y1, numbers.Number) and -90 <= y1 and y1 <= 90
        assert isinstance(x2, numbers.Number) and -180 <= x2 and x2 <= 180
        assert isinstance(y2, numbers.Number) and -90 <= y2 and y2 <= 90

        dLon = abs(x2 - x1)  # 경도 차이
        if dLon >= 180:  # 반대편으로 갈 수 있는 경우
            dLon -= 360  # 반대편 각을 구한다
        dLat = y2 - y1  # 위도 차이
        return round(math.sqrt(pow(dLon, 2) + pow(dLat, 2)), round_decimal_digits)

#속도/비교 ---->euclidean 실제 거리----->harversine



import glob
import pandas as pd

def lati_long_splitter(lati_long_str):
    lati_long = lati_long_str.split(',')
    y1 = float(lati_long[0][1:])
    x1 = float(lati_long[1][1:-1])
    return x1, y1
#컴퓨터
#test = glob.glob('C:/Users/USER/Desktop/학교/참빛/tripReviewAnalysisSystem/크롤러-전처리/주소/*.csv'
#노트북
test = glob.glob('C:/Users/dmdwn/OneDrive/바탕 화면/github/tripReviewAnalysisSystem/크롤러-전처리/주소/*.csv')
#6,7,8 lati_long 0~59 ,60~119, 120~179
print("파일 이름: ", test[6])
file = test[6]
df = pd.read_csv(file, encoding = 'utf-8', engine='python', index_col = 0)
print(df)
#Columns: '0'=이름, '1'=lati  ---------->_long df[이름][주소]
x_0, y_0 = lati_long_splitter(df['1'][0])

x_1, y_1 = lati_long_splitter(df['1'][1])

print(df['0'][0], "에서 ", df['0'][1], "까지의 거리")
print(GeoUtil.get_euclidean_distance(x_0, y_0, x_1, y_1)*100, "km")

def lati_long_compare(place_1_lati_long, place_2_lati_long, place_2_name, place_near, compare_distance, place_near_index, i):
    #거리가 a 만큼 일 때


    x_0, y_0 = lati_long_splitter(place_1_lati_long)
    x_1, y_1 = lati_long_splitter(place_2_lati_long)

    if GeoUtil.get_euclidean_distance(x_0, y_0, x_1, y_1)*100 < compare_distance:
        #자기 자신도 제외
        if GeoUtil.get_euclidean_distance(x_0, y_0, x_1, y_1)*100 != 0:
            place_near.append(place_2_name)         #10km 내의 인덱스값들 저장하기
            place_near_index.append(i)
    return place_near

def lati_long_compare_auto(place, distance):
    place_near_list = []
    place_near_list_index = []
    for i in range(0, len(df['1'])):
        lati_long_compare(df['1'][place], df['1'][i], df['0'][i], place_near_list, distance, place_near_list_index, i)
    return place_near_list, place_near_list_index

#사용법 lati
#각 여행지 별로 500m와 1.5km 저장하기
print("Gyeongbokgung Palace에서 0.5km 내외 인 곳: ")
print(lati_long_compare_auto(0, 0.5)[0])
print(lati_long_compare_auto(0, 1.5)[1])
print("Gyeongbokgung Palace에서 1.5km 내외 인 곳: ")
print(lati_long_compare_auto(0, 1.5)[0])
print(lati_long_compare_auto(0, 1.5)[1])
##

#튜플쌍
#lati_long_compare_auto(0, 1.5)[1],
def create_tuple(list_index, i):
    data = list_index
    list_GP = []
    for j in data:
        t1 = (i, j)
        list_GP.append(t1)

    print(list_GP)

for i in range(59):
    print(df['0'][i],"로 부터 0.5km인 튜플 쌍들: ")
    create_tuple(lati_long_compare_auto(i, 0.5)[1], i)
    print(df['0'][i],"로 부터 1.5km인 튜플 쌍들: ")
    create_tuple(lati_long_compare_auto(i, 1.5)[1], i)
"""
해야할 것: 현재 0~60파일로만 되어있음 --------> 0~ 180 모두
csv파일로 저장 (데이터프레임)
"""