from django.db import models
from django.utils import timezone
# Create your models here.
from django_ckeditor_5.fields import CKEditor5Field  # Make sure it's installed

# Slider 
class SliderImage(models.Model):
    image = models.ImageField(upload_to='slider_images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Slider Image {self.id}"

# Principal message
class PrincipalMessage(models.Model):
    title = models.CharField(max_length=255)
    short_message = CKEditor5Field(config_name='extends')
    full_message = CKEditor5Field(config_name='extends')
    principal_image = models.ImageField(upload_to='principal/')

    def __str__(self):
        return self.title

# alerts

class HomepageAlert(models.Model):
    ALERT_CHOICES = [
        ('success', 'Exciting News (Green)'),
        ('error', 'Alert (Red)'),
        ('info', 'Information (Blue)'),
    ]

    message = CKEditor5Field(config_name='extends')
    alert_type = models.CharField(max_length=10, choices=ALERT_CHOICES, default='info')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.get_alert_type_display()} - {self.message[:50]}"
    
# notice board

class Notice(models.Model):
    title = models.CharField(max_length=100)
    posted_date = models.DateField(default=timezone.now)
    file = models.FileField(upload_to='notices/')

    def __str__(self):
        return self.title


