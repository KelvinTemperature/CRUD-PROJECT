from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=50)
    age = models.PositiveIntegerField()
    email = models.EmailField()
    phone = models.IntegerField()
    location = models.CharField(max_length=50)
    hobby = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['id']