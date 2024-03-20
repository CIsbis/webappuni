import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cat_app_project.settings')
django.setup()

# Import your models
from catapp.models import Student, Cat

def populate():
    # Create some students
    student1 = Student.objects.create(student_name='Alice')
    student2 = Student.objects.create(student_name='Bob')
    student3 = Student.objects.create(student_name='Carol')

    # Create cats for each student
    Cat.objects.create(name='Fluffy', owner=student1)
    Cat.objects.create(name='Whiskers', owner=student2)
    Cat.objects.create(name='Mittens', owner=student3)

    print("Data population completed.")

if __name__ == '__main__':
    populate()
