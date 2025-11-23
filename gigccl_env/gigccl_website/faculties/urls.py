from django.urls import path
from . import views

urlpatterns = [
    path('hods/', views.hod_list, name='hod_list'),                 # hods
    path('hods/<int:hods_id>/', views.hod_detail, name='hod_detail'), 
    path('professors/', views.professor_list, name='professor_list'),
    path('professors/<int:professors_id>/', views.professor_detail, name='professor_detail'),
]
