from django.contrib import admin

# Register your models here.
from .models import Administration, Department, OfferedProgram, InterTimetable, BsTimetable, InterExamination, BsExamination

@admin.register(Administration)
class AdministrationAdmin(admin.ModelAdmin):
    list_display = ('name', 'image')
    
@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'image')

# offered programs

@admin.register(OfferedProgram)
class OfferedProgramAdmin(admin.ModelAdmin):
    list_display = ('name', 'program_type', 'shift', 'total_seats')
    list_filter = ('program_type', 'shift')
    search_fields = ('name',)
    fields = ('name', 'program_type', 'shift', 'total_seats', 'roadmap')

# inter-timetable

@admin.register(InterTimetable)
class InterTimetableAdmin(admin.ModelAdmin):
    # list_display = ('title', 'shift', 'posted_date')
    list_display = ('shift', 'posted_date')
    list_filter = ('shift', 'posted_date')

# bs-timetable

@admin.register(BsTimetable)    
class BsTimetableAdmin(admin.ModelAdmin):
    # list_display = ('title', 'shift', 'posted_date')
    list_display = ('shift', 'posted_date')
    list_filter = ('shift', 'posted_date')

# inter-examination

@admin.register(InterExamination)
class InterExaminationAdmin(admin.ModelAdmin):
    # list_display = ('title', 'shift', 'posted_date')
    list_display = ('shift', 'posted_date')
    list_filter = ('shift', 'posted_date')

# bs-examination

@admin.register(BsExamination)
class BsExaminationAdmin(admin.ModelAdmin):
    # list_display = ('title', 'shift', 'posted_date')
    list_display = ('shift', 'posted_date')
    list_filter = ('shift', 'posted_date')
