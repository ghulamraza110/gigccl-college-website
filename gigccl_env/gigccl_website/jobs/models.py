from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from django.utils import timezone
# Create your models here.

class Job(models.Model):
    CATEGORY_CHOICES = [
        ('Administration', 'Administration'),
        ('Faculty', 'Faculty'),
        ('Staff', 'Staff'),
    ]

    title = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    posted_date = models.DateField(default=timezone.now)
    apply_by = models.DateField(default=timezone.now)
    eligibility = CKEditor5Field(config_name='extends')
    job_details = models.FileField(upload_to='job_details/')
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)

    def __str__(self):
        return self.title
