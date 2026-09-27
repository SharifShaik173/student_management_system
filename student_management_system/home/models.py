from django.db import models

# Create your models here.

class course(models.Model):
    name = models.CharField(max_length=100)
    duration = models.CharField(max_length=50)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class student_data(models.Model):
    first_name=models.CharField(max_length=32)
    middle_name=models.CharField(max_length=32, blank=True)
    last_name=models.CharField(max_length=32)
    email=models.EmailField()
    phone=models.PositiveBigIntegerField()
    dob=models.DateField()
    course=models.ForeignKey(course,on_delete=models.SET_NULL, null=True)
    marks=models.FloatField()
    address=models.CharField(max_length=100)

    def __str__(self):
        return self.first_name

