from django.urls import path
from . import views

urlpatterns = [
    path('job-opportunity/', views.job_opportunities, name='job_opportunities'),
]
