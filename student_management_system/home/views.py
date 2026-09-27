from django.shortcuts import render,redirect
from .forms import details
from .models import student_data
from .models import course
from .forms import CourseForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def login_view(request):

    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect('dashboard')

        else:
            return render(
                request,
                'login.html',
                {'error': 'Invalid username or password'}
            )

    return render(request, 'login.html')


def logout_view(request):

    logout(request)

    return redirect('login')

@login_required
def add_student(request):
    form=details()
    if request.method=='POST':
        form=details(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    return render(request,'add_student.html',{'form':form})

@login_required
def admin(request):
    data = student_data.objects.all()
    courses = course.objects.all()
    return render(request, 'admin.html', {
        'data': data,
        'courses': courses
    })

@login_required
def student_details(request,id):
    data1=student_data.objects.get(id=id)
    return render(request,'student_details.html',{'data1':data1})

@login_required
def edit(request, id):
    student = student_data.objects.get(id=id)
    form = details(instance=student)
    if request.method == 'POST':
        form = details(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_details', id=id)
    return render(request, 'edit.html', {'form': form})

@login_required
def delete(request,id):
    data1=student_data.objects.get(id=id)
    data1.delete()
    return redirect('dashboard')

@login_required
def courses(request):
    data = course.objects.all()
    return render(request, 'courses.html', {
        'courses': data
    })

@login_required
def add_course(request):

    form = CourseForm()

    if request.method == 'POST':
        form = CourseForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('courses')

    return render(request, 'add_course.html', {
        'form': form
    })

@login_required
def edit_course(request, id):
    Course = course.objects.get(id=id)

    if request.method == 'POST':
        Course.name = request.POST['name']
        Course.duration = request.POST['duration']
        Course.description = request.POST['description']
        Course.save()

        return redirect('courses')

    return render(request, 'edit_course.html', {'course': Course})

@login_required
def delete_course(request, id):
    Course = course.objects.get(id=id)
    Course.delete()
    return redirect('courses')


@login_required
def search_student(request):

    query = request.GET.get('q', '')

    data = student_data.objects.filter(
        Q(first_name__icontains=query) |
        Q(last_name__icontains=query) |
        Q(email__icontains=query)
    )

    return render(request, 'search.html', {
        'data': data,
        'query': query
    })