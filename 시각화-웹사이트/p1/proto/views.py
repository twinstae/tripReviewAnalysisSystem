from django.shortcuts import render
from django.views import generic

from .models import Attraction, Big_Sort

# Create your views here.

class HomeView(generic.TemplateView):
    template_name = 'proto/home.html'

class AttractionIndexView(generic.ListView):
    model = Attraction
    template_name = 'proto/attraction_index.html'
    context_object_name = 'three_attractions_list'
    paginate_by = 9

    def get_queryset(self):  # 컨텍스트 오버라이딩
        Attraction_list = Attraction.objects.order_by('big_sort')[:9]
        result = [Attraction_list[i * 3:(i + 1) * 3] for i in range((len(Attraction_list) + 3 - 1) // 3)]
        return result

class AttractionDetailView(generic.DetailView):
    model = Attraction
    template_name = 'proto/attraction.html'

class SortIndexView(generic.ListView):
    model = Big_Sort
    template_name = 'proto/sort_index.html'
    context_object_name = 'three_sorts_list'
    paginate_by = 18

    def get_queryset(self):  # 컨텍스트 오버라이딩
        Sort_list = Big_Sort.objects.order_by('sort_name')[:9]
        result = [Sort_list[i * 3:(i + 1) * 3] for i in range((len(Sort_list) + 3 - 1) // 3)]
        return result

class SortDetailView(generic.DetailView):
    model = Big_Sort
    template_name = 'proto/sorting.html'