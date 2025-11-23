# urls.py
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('principal-message/', views.principal_detail, name='principal_detail'),
    path('contact-us/', views.contact_us, name='contact_us'),
    path('notice-board/', views.notice_board, name='notic_board'),
    path('developers/', views.developers, name='developers'),
]
