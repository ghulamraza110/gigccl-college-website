from django.contrib import admin

# Register your models here.
from .models import Job

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'department', 'category', 'posted_date', 'apply_by')
    list_filter = ('category', 'department', 'posted_date')
    search_fields = ('title', 'department', 'location')
