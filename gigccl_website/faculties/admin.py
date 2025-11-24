from django.contrib import admin

from .models import Hod, Professor
# Register your models here.

# hod admin register
@admin.register(Hod)
class HodAdmin(admin.ModelAdmin):
    list_display = ('name', 'image')

# professor admin register
@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):
    list_display = ('name', 'image')