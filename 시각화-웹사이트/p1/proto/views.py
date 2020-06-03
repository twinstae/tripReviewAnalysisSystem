from django.shortcuts import get_object_or_404, render
from django.views import generic
from proto.models import Attraction
from django.http import HttpResponse

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
    pk = request.POST.get('pk', None)
    assert type(pk) == type(1)
    
    end_name_list = list(range(pk+10,pk+15)) # 임시로 넣은 데이터
            
    Attractions = Attraction.objects.filter(pk__in=end_name_list)
    
    attractions = [{"latitude": a_Attraction.latitude, "longitude": a_Attraction.longitude} for a_Attraction in Attractions]
    
    assert len(attractions) > 1 
    context = json.dumps(attractions)
    
    # json 값을 확인하고 싶다...
    
    return HttpResponse(context, content_type="application/json")