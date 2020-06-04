from django.shortcuts import get_object_or_404, render
from django.views import generic
from proto.models import Attraction
from django.http import HttpResponse
from django.forms.models import model_to_dict
import json
# Create your views here.

import pandas as pd

url = "C:/Users/taehee/Documents/GitHub/tripReviewAnalysisSystem/시각화-웹사이트/p1/static/proto/static/distance0~176.csv"
dist_df = pd.read_csv(url)

class HomeView(generic.TemplateView):
    template_name = 'proto/home.html'

class AttractionIndexView(generic.ListView):
    model = Attraction
    template_name = 'proto/attraction_index.html'
    context_object_name = 'attractions_list'

    def get_queryset(self):  # 컨텍스트 오버라이딩
        attractions_list = Attraction.objects.all()[:9]
        return attractions_list


class AttractionDetailView(generic.DetailView):
    model = Attraction
    context_object_name = 'attraction'
    template_name = 'proto/attraction.html'

class MapView(generic.ListView):
    model = Attraction
    template_name = 'proto/map.html'
    context_object_name = 'attractions_list'
    
    def get_queryset(self):  # 컨텍스트 오버라이딩
        #별점이 최상위인 여행지 5개를 넣고 싶다!
        attractions_list = Attraction.objects.all()[:5]
        
        assert len(attractions_list) > 1
        return attractions_list
        
def new_r(request):
    name = request.POST.get('name', None)
    pk = int(request.POST.get('pk', None))
    assert type(pk) == type(1), type(pk)
    
    end_name_list = list(range(pk+10,pk+12)) # 임시로 넣은 데이터
            
    Attractions = Attraction.objects.filter(pk__in=end_name_list)
    
    #파이썬 객체를 dictionary로 만듭니다. 워드클라우드는 이미지라 json으로 못 만들어서 버렸습니다.
    attractions = [model_to_dict(attraction, fields = ["name","latitude","longitude"]) for attraction in Attractions]
    
    assert len(attractions) > 1 
    context = json.dumps(attractions)
    
    # json 값을 확인하고 싶다...
    
<<<<<<< HEAD
    return HttpResponse(json.dumps(context), content_type="application/json")


"""def new_r(request):
    pk = request.POST.get('pk', None)
    attraction_reviews_posi_nega = get_object_or_404(Attraction, pk=str(int(pk) + 10))
    context = {'good_review' : attraction.positive_review, 'bad_review' : attraction.negative_review}
    
    return HttpResponse(json.dumps(context), content_type="application/json")"""

=======
    return HttpResponse(context, content_type="application/json")
>>>>>>> 81f18f050c44b48372ced0fddb7c2082f6d7e501
