from django.shortcuts import render
from django.views import generic
from proto.models import Attraction, Big_Sort

# Create your views here.


class HomeView(generic.TemplateView):
    template_name = 'proto/home.html'


class AttractionIndexView(generic.ListView):
    model = Attraction
    template_name = 'proto/attraction_index.html'
    context_object_name = 'attractions_list'

    def get_queryset(self):  # 컨텍스트 오버라이딩
        attractions_list = Attraction.objects.all()[:3]
        return attractions_list


class AttractionDetailView(generic.DetailView):
    model = Attraction
    template_name = 'proto/attraction.html'


class SortIndexView(generic.ListView):
    model = Big_Sort
    template_name = 'proto/sort_index.html'
    context_object_name = 'sorts_list'

    def get_queryset(self):  # 컨텍스트 오버라이딩
        sorts_list = Big_Sort.objects.all()[:3]
        return sorts_list


class SortDetailView(generic.DetailView):
    model = Big_Sort
    template_name = 'proto/sorting.html'

