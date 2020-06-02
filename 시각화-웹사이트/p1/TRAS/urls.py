from django.contrib import admin
from django.urls import path, include
from proto import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomeView.as_view(), name='home'),
    path('attraction/', views.AttractionIndexView.as_view(), name='attraction_index'),
    path('attraction/<int:pk>', views.AttractionDetailView.as_view(), name='attraction_detail'),
    path('map/', views.MapView.as_view(), name='map_index'),
    path('map/new_r', views.new_r, name='new_r')
]
