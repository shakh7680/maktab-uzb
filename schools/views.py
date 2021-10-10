from django import http
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import Schools, Teacher, Student, Comment
from accounts.models import User
from django.http import JsonResponse
from .choices import region_choices, school_type_choices
from django.contrib import messages

# Schools
def schools(request):
    if request.user.is_authenticated and request.user.is_staff:
        return redirect('admin_dashboard')
    else:
        schools = Schools.objects.order_by('-created_at')
        
        if 'region' and 'school_type' and 'school_name' in request.GET:
            region = request.GET['region']
            school_type = request.GET['school_type']
            school_name = request.GET['school_name']
            if region and school_type and school_name :
                schools = schools.filter(region=region, school_type=school_type, schoolname=school_name)
        # Pagination
        paginator = Paginator(schools,4)
        page = request.GET.get('page')
        paged_schools = paginator.get_page(page)

        context ={
            'schools':paged_schools,
            'region_choices': region_choices,
            'school_type_choices': school_type_choices,
        }

        return render(request, 'schools/schools.html', context)

# Teachers
def teachers(request, id):
    if request.user.is_authenticated and request.user.is_staff:
        return redirect('admin_dashboard')
    else:
        users = User.objects.all()
        lista = request.path.split('/')
        teachers = Teacher.objects.filter(school_id=id)
        teachers_choices = teachers.values_list('first_name','last_name', 'role')
        # teachers name
        teachers_name =[]
        teachers_surname = []
        teachers_role = []

        for i in range(0, len(teachers_choices)):
            teachers_name.append(teachers_choices[i][0])
            teachers_surname.append(teachers_choices[i][1])
            teachers_role.append(teachers_choices[i][2])    
        
        if ('teacher_name' and 'teacher_surname' and 'teacher_role') in request.GET:
            teacher_name = request.POST.get('teacher_name')
            teacher_surname = request.POST.get('teacher_surname')
            teacher_role = request.POST.get('teacher_role')
            if teacher_name and teacher_surname and teacher_role:
                teachers = teachers.filter(first_name=teacher_name, last_name = teacher_surname, role=teacher_role)

        if 'teacher_name' in request.GET:
            teacher_name = request.GET['teacher_name']
            if teacher_name:
                teachers = teachers.filter(first_name=teacher_name)

        if 'teacher_surname' in request.GET:
            teacher_surname = request.GET['teacher_surname']
            if teacher_surname:
                teachers = teachers.filter(last_name=teacher_surname)
        if 'teacher_role' in request.GET:
            teacher_role = request.GET['teacher_role']
            if teacher_role:
                teachers = teachers.filter(role=teacher_role)

        context = {
            'teachers': teachers,
            'teachers_name': teachers_name,
            'teachers_surname':teachers_surname,
            'teachers_role': teachers_role,
            'school_id': lista[2],
            'users':users
        }
        
        return render(request, 'schools/teachers.html', context)

# Students   
def students(request, id ):
    students = Student.objects.filter(school_id =id)
    
    context = {
        'students': students
    }
   
    return render(request, 'schools/students.html', context)

#Comments save 
def comment_save(request):
    if request.method == 'POST':
        comment = request.POST['comment']
        if comment is not None:
            id = request.POST['teacher_id']
            global school_id
            school_id = request.POST['school_id']
            if comment:
                comments = Comment.objects.filter(teacher_id_id = id).create(comment=comment, teacher_id_id = id)
                comments.save()
                messages.success(request, 'Successfully commented!')
                return redirect(f'{school_id}/teachers')
            return redirect('comment_save')
    return redirect(f'{school_id}/teachers')
    
# Read comment with ajax
def read_comment(request, id):
  return JsonResponse(list(Comment.objects.filter(teacher_id_id=id, hidden=False).values()), safe=False)

# School name
def school_name(request,region,school_type_det):
  return JsonResponse(list(Schools.objects.filter(region=region, school_type=school_type_det).values()), safe=False)

#Teaher rating with ajax 
def teacher_rating(request, teacher_id, rating):
    teacher_rating_val = Teacher.objects.filter(id = teacher_id)
    for value in teacher_rating_val:
        final_rating = (value.ranking+float(rating))/2
        final_rating = round(final_rating,2)
        value.ranking =final_rating
        value.save()
    return HttpResponse(final_rating)
