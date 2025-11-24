from django.shortcuts import render
from .models import Administration, Department, OfferedProgram, InterTimetable, BsTimetable, InterExamination, BsExamination

# administration

def administrations(request):
    administrations = Administration.objects.all().order_by('-created_at') # Fetch all administrations 
    return render(request, 'Academics/administrations.html', {'administrations': administrations})

# administration detail

def administration_detail(request, administrations_id):
    administration = Administration.objects.get(id=administrations_id)
    return render(request, 'Academics/administration_detail.html', {'administration': administration})
# department
def departments(request):
    departments = Department.objects.all().order_by('-created_at')  # fetch all departments
    return render(request, 'Academics/departments.html', {'departments': departments})

# department detail

def department_detail(request, departments_id):
    department = Department.objects.get(id=departments_id)
    return render(request, 'Academics/department_detail.html', {'department': department})

# offered programs

def offered_programs(request):
    intermediate_programs = OfferedProgram.objects.filter(program_type='Intermediate').order_by('-created_at')
    bs_programs = OfferedProgram.objects.filter(program_type='BS').order_by('-created_at')
    return render(request, 'Academics/offered_programs.html', {
        'intermediate_programs': intermediate_programs,
        'bs_programs': bs_programs
    })

# inter-timetable

def inter_timetable(request):
    timetables = InterTimetable.objects.all().order_by('-posted_date', '-id')
    return render(request, 'Academics/inter_timetable.html', {'timetables': timetables})

# bs-timetable

def bs_timetable(request):
    timetables = BsTimetable.objects.all().order_by('-posted_date', '-id')
    return render(request, 'Academics/bs_timetable.html', {'timetables': timetables})

# inter-examination

def inter_examination(request):
    examinations = InterExamination.objects.all().order_by('-posted_date', '-id')
    return render(request, 'Academics/inter_examination.html', {'examinations': examinations})

# bs-examination

def bs_examination(request):
    examinations = BsExamination.objects.all().order_by('-posted_date', '-id')
    return render(request, 'Academics/bs_examination.html', {'examinations': examinations})