from django.shortcuts import render

# Create your views here.

from .models import Job

def job_opportunities(request):
    jobs = Job.objects.all().order_by('-posted_date', '-id')
    return render(request, 'jobs/job_opportunity.html', {'jobs': jobs})

