from django import forms
from .models import student_data
from .models import course


class details(forms.ModelForm):
    class Meta():
        model=student_data
        fields='__all__'


class CourseForm(forms.ModelForm):

    class Meta:
        model = course
        fields = ['name', 'duration', 'description']