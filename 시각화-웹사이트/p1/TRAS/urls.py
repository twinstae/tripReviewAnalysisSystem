from django.contrib import admin
from django.urls import path, include
from proto import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomeView.as_view(), name='home'),
    path('attraction/', views.AttractionIndexView.as_view(), name='attraction_index'),
    path('attraction/<int:pk>', views.AttractionDetailView.as_view(), name='attraction_detail'),
    path('sort/', views.SortIndexView.as_view(), name='sort_index'),
    path('sort/<int:pk>', views.SortDetailView.as_view(), name='sort_detail'),
]
