from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from django.utils import timezone
# Create your models here.

class Alumni(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='alumni_images/')
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

# News Bulletin Model

class NewsBulletin(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='news_bulletins/')
    description = CKEditor5Field(config_name='extends')  # Using CKEditor5Field
    posted_date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.title
    
# Fanian_magzine Model

class Magazine(models.Model):
    title = models.CharField(max_length=200)
    cover_image = models.ImageField(upload_to='magazines/covers/')
    posted_date = models.DateField(default=timezone.now)
    description = CKEditor5Field(config_name='extends')  # Using CKEditor5Field
    magzine = models.FileField(upload_to='magazines/pdfs/')

    def __str__(self):
        return self.title
