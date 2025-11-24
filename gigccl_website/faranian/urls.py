from django.urls import path
from . import views
from .views import news_bulletin_list, news_bulletin_detail

urlpatterns = [
    path('alumni/', views.alumni_list, name='alumni'),
    path('news_bulletin/', news_bulletin_list, name='news_bulletin_list'),
    path('news_bulletin/<int:news_bulletin_id>/', news_bulletin_detail, name='news_bulletin_detail'),
    path('magazines/', views.magazine_list, name='magazine_list'),
]
