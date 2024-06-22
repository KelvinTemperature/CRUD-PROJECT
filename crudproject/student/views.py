from django.shortcuts import render
from student.models import Student
from student.form import StudentForm


# Create your views here.
def index(request):
    context = {}
    form = StudentForm()
    students = Student.objects.all()
    context['students'] = students
    context['form'] = form
    return render(request, 'index.html', context)