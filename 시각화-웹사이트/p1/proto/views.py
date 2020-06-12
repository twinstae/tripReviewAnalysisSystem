from django.shortcuts import get_object_or_404, render
from django.views import generic
from proto.models import Attraction, Route
from django.http import HttpResponse
from django.forms.models import model_to_dict
import json
from django.core.serializers.json import DjangoJSONEncoder
from django.core.serializers import serialize

import numpy as np
import pandas as pd
import json

class LazyEncoder(DjangoJSONEncoder):
    def default(self, obj):
        if isinstance(obj, YourCustomType):
            return str(obj)
        return super().default(obj)

# Create your views here.


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
    raw_list = request.POST.get('list', None)
    selected_attractions = json.loads(raw_list)
    raw_pk =request.POST.get('pk', None)
    pk = int(raw_pk)
    assert type(pk) == type(1), type(pk)
    
    new_pk_list = recommend(selected_attractions, pk)

    Attractions = Attraction.objects.filter(pk__in = new_pk_list)
    
    attractions = serialize('json', Attractions, cls=LazyEncoder)  
    assert len(attractions) > 1 

    return HttpResponse(attractions, content_type="application/json")

def recommend(selected_attractions, pk):

    candidate_df = distance_r(selected_attractions, pk)
    candidate_df['star'] = star_r(candidate_df['end_pk']) 
    candidate_df['rating'] = candidate_df['dist'] * candidate_df['star'] 
    
    
    top_5 = candidate_df.sort_values(by='rating')[-5:]
    
    print(top_5)
    print(top_5.end_pk)
    print(list(top_5.end_pk))
    
    new_pk_list = list(top_5.end_pk) #상위 5개의 end_pk값을 가져온다.
    
    return new_pk_list
    
def distance_r(selected_attractions, pk):

    candidate_df = pd.DataFrame(np.zeros(shape = (15,3)), columns = ['rating', 'end_pk', 'dist'])
    start = Attraction.objects.get(pk = pk)

    now_i = 0

    for distance in ['5','15','30']:
        route_qs = Route.objects.filter(start_pk = start, dist = distance)
        for route in route_qs.values_list('end_pk', 'dist', named=True):
            if route.end_pk not in selected_attractions and now_i < 15 :
                candidate_df.loc[now_i, 'end_pk'] = route.end_pk
                candidate_df.loc[now_i, 'dist'] = (100 - route.dist) / 100
                #candidate_df.loc[now_i, 'dist'] = route.rating
                now_i += 1
                        
    return candidate_df
    
def star_r(end_pk_series):
    star_qs = Attraction.objects.filter(pk__in = list(end_pk_series))
    
    star_list = []
    for attr in star_qs:
        try:
            star_list.append(json.loads(attr.star_info)['avg'] / 5)
        except:
            star_list.append(4 / 5)
    
    if len(star_list) != 15:
        star_list.extend([0]*(15-len(star_list)))
    
    return star_list
    #return Attraction.objects.filter(pk__in = list(end_pk_series)).values_list('star_rating', flat=True)
    
    

"""def new_r(request):
    pk = request.POST.get('pk', None)
    attraction_reviews_posi_nega = get_object_or_404(Attraction, pk=str(int(pk) + 10))
    context = {'good_review' : attraction.positive_review, 'bad_review' : attraction.negative_review}

    return HttpResponse(json.dumps(context), content_type="application/json")"""  # 무엇을 누룰때 어떤것이 나오는지를 설정하는것, 무엇은 정확히..