from django.contrib import admin
from django import forms
from django_ckeditor_5.widgets import CKEditor5Widget
from .models import SliderImage, PrincipalMessage, HomepageAlert, Notice

# Slider Image Admin Panel
@admin.register(SliderImage)
class SliderImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'uploaded_at')
    ordering = ('-uploaded_at',)

# PrincipalMessage Admin Panel (Fix)
class PrincipalMessageAdminForm(forms.ModelForm):
    class Meta:
        model = PrincipalMessage
        fields = "__all__"
        widgets = {
            "short_message": CKEditor5Widget(config_name="extends"), # Use "extends"
            "full_message": CKEditor5Widget(config_name="extends"),  # Use "extends"
        }

@admin.register(PrincipalMessage)
class PrincipalMessageAdmin(admin.ModelAdmin):
    form = PrincipalMessageAdminForm
    list_display = ('title',)

# Alerts Admin Panel

@admin.register(HomepageAlert)
class HomepageAlertAdmin(admin.ModelAdmin):
    list_display = ('message', 'alert_type', 'is_active', 'created_at')
    list_filter = ('alert_type', 'is_active')
    search_fields = ('message',)
    ordering = ('-created_at',)

# notice board admin panel

@admin.register(Notice)
class NoticeAdmin(admin.ModelAdmin):
    list_display = ('title', 'posted_date')
    search_fields = ('title',)
    list_filter = ('posted_date',)
    ordering = ('-posted_date',)

