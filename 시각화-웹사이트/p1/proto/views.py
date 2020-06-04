from django.shortcuts import get_object_or_404, render
from django.views import generic
from proto.models import Attraction
from django.http import HttpResponse
import json
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
        attractions_list = Attraction.objects.all()[:3]
        return attractions_list
        
def new_r(request):
    pk = request.POST.get('pk', None)
    attraction = get_object_or_404(Attraction, pk= str(int(pk) + 10))
    context = {'latitude' : attraction.latitude ,
               'longitude': attraction.longitude }
    
    return HttpResponse(json.dumps(context), content_type="application/json")


"""def new_r(request):
    pk = request.POST.get('pk', None)
    attraction_reviews_posi_nega = get_object_or_404(Attraction, pk=str(int(pk) + 10))
    context = {'good_review' : attraction.positive_review, 'bad_review' : attraction.negative_review}
    
    return HttpResponse(json.dumps(context), content_type="application/json")"""

