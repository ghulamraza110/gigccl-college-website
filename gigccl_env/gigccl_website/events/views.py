from django.shortcuts import render, get_object_or_404
from .models import Event, Conference, CurricularActivity

def event_list(request):
    events = Event.objects.all().order_by('-posted_date', '-id')
    return render(request, 'events/event.html', {'events': events})

def event_detail(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    return render(request, 'events/event_detail.html', {'event': event})

# Conferences 

def conference_list(request):
    conferences = Conference.objects.all().order_by('-posted_date', '-id')
    return render(request, 'events/conference.html', {'conferences': conferences})

def conference_detail(request, conference_id):
    conference = get_object_or_404(Conference, id=conference_id)
    return render(request, 'events/conference_detail.html', {'conference': conference})

# Curricular_Activities 

def curricular_activity_list(request):
    curricular_activities = CurricularActivity.objects.all().order_by('-posted_date', '-id')
    return render(request, 'events/curricular_activity.html', {'curricular_activities': curricular_activities})

def curricular_activity_detail(request, curricular_activity_id):
    curricular_activity = get_object_or_404(CurricularActivity, id=curricular_activity_id)
    return render(request, 'events/curricular_activity_detail.html', {'curricular_activity': curricular_activity})