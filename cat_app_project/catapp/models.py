
from django.db import models

class Student(models.Model):
    student_first_name= models.CharField(max_length=100, default='')
    student_last_name = models.CharField(max_length=100, default='')
    def __str__(self):
        return f"{self.student_first_name} {self.student_last_name}"



class Cat(models.Model):
    owner = models.ForeignKey('Student', on_delete=models.CASCADE, related_name='cats')
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
