from django.shortcuts import render
from student.models import Student

# Create your views here.
def index(request):
    context = {}
    students = Student.objects.all()
    context['students'] = students
    return render(request, 'index.html', context) 