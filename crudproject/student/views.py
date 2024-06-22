from django.shortcuts import render
from student.models import Student

# Create your views here.
def index(request):
    construt = {}
    return render(request, 'index.html', construt) 