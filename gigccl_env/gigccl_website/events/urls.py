from django.urls import path
from .views import event_list, event_detail
from .views import conference_list, conference_detail
from .views import curricular_activity_list, curricular_activity_detail
urlpatterns = [
    path('event/', event_list, name='event_list'),
    path('event/<int:event_id>/', event_detail, name='event_detail'),
    path('conference/', conference_list, name='conference_list'),
    path('conference/<int:conference_id>/', conference_detail, name='conference_detail'),
    path('curricular_activity/', curricular_activity_list, name='curricular_activity_list'),
    path('curricular_activity/<int:curricular_activity_id>/', curricular_activity_detail, name='curricular_activity_detail'),
]
