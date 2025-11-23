from django.contrib import admin
# Register your models here.
from django import forms
from django_ckeditor_5.widgets import CKEditor5Widget
from .models import Event, Conference, CurricularActivity

# Custom Form for CKEditor 5 Integration
class EventAdminForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = "__all__"
        widgets = {
            "description": CKEditor5Widget(config_name="extends"),  # Using CKEditor5Widget
        }

# Register Event Model with Custom Form
@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    form = EventAdminForm
    list_display = ('title', 'posted_date')
    search_fields = ('title',)
    list_filter = ('posted_date',)
    ordering = ('-posted_date',)

# Conference 
class ConferenceAdminForm(forms.ModelForm):
    class Meta:
        model = Conference
        fields = "__all__"
        widgets = {
            "description": CKEditor5Widget(config_name="extends"),  # Using CKEditor5Widget
        }

# Register Conference Model with Custom Form
@admin.register(Conference)
class ConferenceAdmin(admin.ModelAdmin):
    form = ConferenceAdminForm
    list_display = ('title', 'posted_date')
    search_fields = ('title',)
    list_filter = ('posted_date',)
    ordering = ('-posted_date',)

    # CurricularActivity 
class CurricularActivityAdminForm(forms.ModelForm):
    class Meta:
        model = CurricularActivity
        fields = "__all__"
        widgets = {
            "description": CKEditor5Widget(config_name="extends"),  # Using CKEditor5Widget
        }

# Register CurricularActivity Model with Custom Form
@admin.register(CurricularActivity)
class CurricularActivityAdmin(admin.ModelAdmin):
    form = CurricularActivityAdminForm
    list_display = ('title', 'posted_date')  
    search_fields = ('title',)
    list_filter = ('posted_date',)
    ordering = ('-posted_date',)