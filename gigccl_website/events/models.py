from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from django.utils import timezone
# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='events/')
    description = CKEditor5Field(config_name='extends')  # Using CKEditor5Field
    posted_date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.title

# Conferences 
class Conference(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='conferences/')
    description = CKEditor5Field(config_name='extends')  # Using CKEditor5Field
    posted_date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.title
    
    # Curricular_Activities 
class CurricularActivity(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='curricular_activities/')
    description = CKEditor5Field(config_name='extends')  # Using CKEditor5Field
    posted_date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.title