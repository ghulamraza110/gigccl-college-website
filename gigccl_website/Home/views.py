from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

# Slider and principal message
from django.shortcuts import render, get_object_or_404
from .models import SliderImage, PrincipalMessage, HomepageAlert, Notice
from events.models import Event

def home(request):
    alerts = HomepageAlert.objects.filter(is_active=True).order_by('-created_at')
    slider_images = SliderImage.objects.all()  # Fetch all slider images
    principal_message = PrincipalMessage.objects.first()  # Fetch principal message
    latest_events = Event.objects.order_by('-posted_date', '-id')[:6]  # Latest 6 Events
    return render(request, 'Home/home.html', {
        'slider_images': slider_images,
        'principal_message': principal_message,
        'latest_events': latest_events, # Pass latest events to template
        'alerts': alerts
    })

def principal_detail(request):
    principal_message = get_object_or_404(PrincipalMessage)
    return render(request, 'Home/principal_detail.html', {'principal_message': principal_message})

def contact_us(request):
    return render(request, 'Home/contact_us.html')

def developers(request):
    return render(request, 'Home/developers.html')

def notice_board(request):
    notices = Notice.objects.all().order_by('-posted_date', '-id')
    return render(request, 'Home/notice_board.html', {'notices': notices})