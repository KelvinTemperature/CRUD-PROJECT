from django import forms
from student.models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'age', 'email', 'phone', 'location', 'hobby']