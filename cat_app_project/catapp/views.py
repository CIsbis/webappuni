from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

from catapp.models import Student

from catapp.models import Cat


# Create your views here.
def index(request):
    students = Student.objects.all().order_by('student_last_name')
    return render(request, 'catapp/index.html',  {'students': students})



def about(request):
    cats = Cat.objects.all()
    return render(request, 'catapp/cats.html', {'cats': cats})
