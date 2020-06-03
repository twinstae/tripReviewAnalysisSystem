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
        #별점이 최상위인 여행지 5개
        attractions_list = Attraction.objects.all()[:3]
        return attractions_list
        
def new_r(request):
    name = request.POST.get('name', None)
    start_attraction_row = dist_df[dist_df["Name"] == name]
    end_name_list = []  
    
            
    Attractions = Attraction.objects.filter(name__in=end_name_list)
    
    attractions = [{"latitude": a_Attraction.latitude, "longitude": a_Attraction.longitude} for a_Attraction in Attractions]
    
    context = attractions
    
    return HttpResponse(json.dumps(context), content_type="application/json")