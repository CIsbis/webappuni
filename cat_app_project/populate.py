import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cat_app_project.settings')
django.setup()

# Import your models
from catapp.models import Student, Cat

def populate():

    student1 = Student.objects.create(student_first_name='Alice', student_last_name='Smith')
    student2 = Student.objects.create(student_first_name='Bob', student_last_name='Jones')
    student3 = Student.objects.create(student_first_name='Carol', student_last_name='Doe')


    Cat.objects.create(name='Fluffy', owner=student1)
    Cat.objects.create(name='Spot', owner=student1)
    Cat.objects.create(name='Whiskers', owner=student2)
    Cat.objects.create(name='Mittens', owner=student3)

    print("Population Done")

if __name__ == '__main__':
    populate()
