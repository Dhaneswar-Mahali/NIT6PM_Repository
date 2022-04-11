from django.db import models
from django.urls import reverse #First we need to import reverse to reverse to student_list

class Student(models.Model):
    sname = models.CharField(max_length=50)
    marks = models.IntegerField()
    email = models.EmailField(unique=True)
    mobile = models.BigIntegerField(unique=True)
    address = models.CharField(max_length=50)

    def __str__(self):
        return self.sname


    def get_absolute_url(self): #Error-No URL to redirect to.  Either provide a url or define a get_absolute_url method on the Model.
        return reverse('student_list')#At the time of student createview it needs to define in order to redirect student_list view.
