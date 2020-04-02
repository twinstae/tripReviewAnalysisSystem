from django.contrib import admin
from django.urls import path
from proto import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('proto/', views.HomeView.as_view(), name='home'),
    path('proto/attraction/', views.AttractionIndexView.as_view(), name='attraction_index'),
    path('proto/attraction/<int:attraction_id>', views.AttractionDetailView.as_view(), name='attraction_detail'),
    path('proto/sort/', views.SortIndexView.as_view(), name='sort_index'),
    path('proto/sort/<int:big_Sort_id>', views.SortDetailView.as_view(), name='sort_detail'),
]
