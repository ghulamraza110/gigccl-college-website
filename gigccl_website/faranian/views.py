from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import Alumni, NewsBulletin, Magazine
def alumni_list(request):
    alumni_list = Alumni.objects.all().order_by('-created_at')  # Latest first
    return render(request, 'faranian/alumni.html', {'alumni_list': alumni_list})

# News Bulletin

def news_bulletin_list(request):
    news_bulletins = NewsBulletin.objects.all().order_by('-posted_date', '-id')
    return render(request, 'faranian/news_bulletin.html', {'news_bulletins': news_bulletins})

def news_bulletin_detail(request, news_bulletin_id):
    news_bulletin = get_object_or_404(NewsBulletin, id=news_bulletin_id)
    return render(request, 'faranian/news_bulletin_detail.html', {'news_bulletin': news_bulletin})

# Magazines

def magazine_list(request):
    magazines = Magazine.objects.order_by('-posted_date', '-id')
    return render(request, 'faranian/faranian_magzine.html', {'magazines': magazines})
