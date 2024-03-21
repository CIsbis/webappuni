from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Student , Cat

admin.site.register(Student)
admin.site.register(Cat)
