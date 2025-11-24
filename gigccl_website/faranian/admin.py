from django.contrib import admin

# Register your models here.
from .models import Alumni, NewsBulletin, Magazine
from django import forms
from django_ckeditor_5.widgets import CKEditor5Widget

@admin.register(Alumni)
class AlumniAdmin(admin.ModelAdmin):
    list_display = ('name', 'image',)

# News Bulletin Admin Panel

# Custom Form for CKEditor 5 Integration
class NewsBulletinAdminForm(forms.ModelForm):
    class Meta:
        model = NewsBulletin
        fields = "__all__"
        widgets = {
            "description": CKEditor5Widget(config_name="extends"),  # Using CKEditor5Widget
        }

# Register NewsBulletin Model with Custom Form
@admin.register(NewsBulletin)
class NewsBulletinAdmin(admin.ModelAdmin):
    form = NewsBulletinAdminForm
    list_display = ('title', 'posted_date')
    search_fields = ('title',)
    list_filter = ('posted_date',)
    ordering = ('-posted_date',)

# Faranian Magzine

@admin.register(Magazine)
class MagazineAdmin(admin.ModelAdmin):
    list_display = ('title', 'posted_date')
    search_fields = ('title', 'description')
    list_filter = ('posted_date',)
