from django.db import models
class student(models.Model):
    name=models.CharField(max_length=100)
    roll_no=models.CharField(max_length=100,unique=True)
    email=models.EmailField(max_length=100,unique=True)
    admit_date=models.DateField
    def __str__ (self):
        return student.name
