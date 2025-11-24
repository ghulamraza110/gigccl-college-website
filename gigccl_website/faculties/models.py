from django.db import models
from django.utils import timezone
from django_ckeditor_5.fields import CKEditor5Field 
# Create your models here.

# hod model
class Hod(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='hod/')
    hod_detail = CKEditor5Field(config_name='extends')
    created_at = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.name
    
# professors model

class Professor(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='professors/')
    professor_detail = CKEditor5Field(config_name='extends')
    created_at = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.name

