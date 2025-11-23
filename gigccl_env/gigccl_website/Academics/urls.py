from django.urls import path
from . import views

urlpatterns = [
    path('administrations/', views.administrations, name='administrations'),
    path('administrations/<int:administrations_id>/', views.administration_detail, name='administration_detail'),
    path('departments/', views.departments, name='departments'),
    path('departments/<int:departments_id>/', views.department_detail, name='department_detail'),
    path('offered_programs/', views.offered_programs, name='offered_programs'),
    path('inter_timetable/', views.inter_timetable, name='inter_timetable'),
    path('bs_timetable/', views.bs_timetable, name='bs_timetable'),
    path('inter_examination/', views.inter_examination, name='inter_examination'),
    path('bs_examination/', views.bs_examination, name='bs_examination'),
]
