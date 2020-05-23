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
test = glob.glob('C:/Users/USER/Desktop/학교/참빛/tripReviewAnalysisSystem/크롤러-전처리/주소/*.csv')
file = test[6]
df = pd.read_csv(file, encoding = 'utf-8', engine='python', index_col = 0)
print(df)
#Columns: '0'=이름, '1'=lati_long
x_0, y_0 = lati_long_splitter(df['1'][0])

x_1, y_1 = lati_long_splitter(df['1'][1])

print(df['0'][0], "에서 ", df['0'][1], "까지의 거리")
print(GeoUtil.get_euclidean_distance(x_0, y_0, x_1, y_1)*100, "km")