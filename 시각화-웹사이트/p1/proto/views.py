from django.shortcuts import render
from django.views import generic
from proto.models import Attraction

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

class MapView(view?):
    model = Attraction
    template_name = 'proto/map.html'
    context_object_name = 'map_data'