"""
    path('TRAS/', views.home, name='home'),
    path('TRAS/attraction/', views.attraction_index, name='attraction_index'),
    path('TRAS/attraction/<int:attraction_id>', views.attraction, name='attraction'),
    path('TRAS/sort/', views.sort_index, name='sort_index'),
    path('TRAS/sort/<int:big_Sort_id>', views.sorting, name='sorting'),
"""

from django.contrib import admin
from django.urls import path
from proto import views

urlpatterns = [
    path('admin/', admin.site.urls),
]
