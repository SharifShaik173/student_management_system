from django.contrib import admin
from .models import student_data
from .models import course
# Register your models here.
admin.site.register(student_data)
admin.site.register(course)