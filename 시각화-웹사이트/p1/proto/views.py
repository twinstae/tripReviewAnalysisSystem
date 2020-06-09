from django.shortcuts import get_object_or_404, render
from django.views import generic
from proto.models import Attraction
from django.http import HttpResponse
from django.forms.models import model_to_dict
import json
from django.core.serializers.json import DjangoJSONEncoder
from django.core.serializers import serialize

class LazyEncoder(DjangoJSONEncoder):
    def default(self, obj):
        if isinstance(obj, YourCustomType):
            return str(obj)
        return super().default(obj)

# Create your views here.

import pandas as pd

#url = "C:/Users/taehee/Documents/GitHub/tripReviewAnalysisSystem/시각화-웹사이트/p1/static/proto/static/distance0~176.csv"
#url = r"C:\Users\Jeong\Documents\GitHub\tripReviewAnalysisSystem\시각화-웹사이트\p1\static\proto\static\distance0~176.csv"
#dist_df = pd.read_csv(url)

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
    
    attractions = serialize('json', Attractions, cls=LazyEncoder)  
    
    # json 값을 확인하고 싶다...
    
    #return HttpResponse(json.dumps(context), content_type="application/json")

    return HttpResponse(attractions, content_type="application/json")

"""def new_r(request):
    pk = request.POST.get('pk', None)
    attraction_reviews_posi_nega = get_object_or_404(Attraction, pk=str(int(pk) + 10))
    context = {'good_review' : attraction.positive_review, 'bad_review' : attraction.negative_review}

    return HttpResponse(json.dumps(context), content_type="application/json")"""  # 무엇을 누룰때 어떤것이 나오는지를 설정하는것, 무엇은 정확히..