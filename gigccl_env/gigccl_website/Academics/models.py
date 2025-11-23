from django.db import models
from django_ckeditor_5.fields import CKEditor5Field 
from django.utils import timezone
# Create your models here.

# Administration model
class Administration(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='administration/')
    administration_detail = CKEditor5Field(config_name='extends')
    created_at = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.name
# Departments model
class Department(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='department/')
    department_detail = CKEditor5Field(config_name='extends')
    created_at = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.name

# offered programs model

SHIFT_CHOICES = (
    ('Morning', 'Morning'),
    ('Evening', 'Evening'),
    ('Both', 'Both'),
)

PROGRAM_TYPE = (
    ('Intermediate', 'Intermediate'),
    ('BS', 'BS'),
)

class OfferedProgram(models.Model):
    name = models.CharField(max_length=100)
    total_seats = models.PositiveIntegerField()
    shift = models.CharField(max_length=10, choices=SHIFT_CHOICES)
    roadmap = models.FileField(upload_to='roadmaps/')  # No null=True or blank=True
    program_type = models.CharField(max_length=20, choices=PROGRAM_TYPE)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


# inter-timetable model

class InterTimetable(models.Model):
    SHIFT_CHOICES = [
        ('Morning', 'Morning'),
        ('Evening', 'Evening'),
    ]

    # title = models.CharField(max_length=100)
    shift = models.CharField(max_length=10, choices=SHIFT_CHOICES)
    posted_date = models.DateField(default=timezone.now)
    file = models.FileField(upload_to='inter_timetables/')
    preview_image = models.ImageField(upload_to='timetable_previews/', blank=True, null=True)

    def __str__(self):
        return self.shift

# bs-timetable model

class BsTimetable(models.Model):
    SHIFT_CHOICES = [
        ('Morning', 'Morning'),
        ('Evening', 'Evening'),
    ]

    # title = models.CharField(max_length=100)
    shift = models.CharField(max_length=10, choices=SHIFT_CHOICES)
    posted_date = models.DateField(default=timezone.now)
    file = models.FileField(upload_to='bs_timetables/')
    preview_image = models.ImageField(upload_to='timetable_previews/', blank=True, null=True)

    def __str__(self):
        return self.shift
    
# inter-examination model

class InterExamination(models.Model):
    SHIFT_CHOICES = [
        ('Morning', 'Morning'),
        ('Evening', 'Evening'),
    ]

    # title = models.CharField(max_length=100)
    shift = models.CharField(max_length=10, choices=SHIFT_CHOICES)
    posted_date = models.DateField(default=timezone.now)
    file = models.FileField(upload_to='inter_examinations/')
    preview_image = models.ImageField(upload_to='examination_previews/', blank=True, null=True)

    def __str__(self):
        return self.shift
    
# bs-examination model

class BsExamination(models.Model):
    SHIFT_CHOICES = [
        ('Morning', 'Morning'),
        ('Evening', 'Evening'),
    ]

    # title = models.CharField(max_length=100)
    shift = models.CharField(max_length=10, choices=SHIFT_CHOICES)
    posted_date = models.DateField(default=timezone.now)
    file = models.FileField(upload_to='bs_examinations/')
    preview_image = models.ImageField(upload_to='examination_previews/', blank=True, null=True)

    def __str__(self):
        return self.shift