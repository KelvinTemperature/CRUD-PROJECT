from django.contrib import admin
from student.models import Student

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'age', 'email', 'phone', 'location', 'hobby']

admin.site.register(Student, StudentAdmin)