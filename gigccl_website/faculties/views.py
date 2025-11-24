from django.shortcuts import render
from .models import Hod, Professor
# Create your views here.

# hod
def hod_list(request):
    hods = Hod.objects.all().order_by('-created_at')
    return render(request, 'faculties/hod.html', {'hods': hods})

# hod detail

def hod_detail(request, hods_id):
    hod = Hod.objects.get(id=hods_id)
    return render(request, 'faculties/hod_detail.html', {'hod': hod})

# professors

def professor_list(request):
    professors = Professor.objects.all().order_by('-created_at')
    return render(request, 'faculties/professor.html', {'professors': professors})

# professor detail

def professor_detail(request, professors_id):
    professor = Professor.objects.get(id=professors_id)
    return render(request, 'faculties/professor_detail.html', {'professor': professor})