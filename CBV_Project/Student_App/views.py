from django.shortcuts import render
from django.urls import reverse_lazy
from Student_App.models import Student
from django.views.generic import (ListView,DetailView,CreateView,UpdateView,DeleteView)

class StudentList_View(ListView):#ListView is equal to ---Student.objects.all() in FBV for reading data from database.
    model = Student #Student.objects.all()
    context_object_name = 'student_list'
    template_name = 'StudentApp/studentlist.html'

class StudentDetails_View(DetailView):
    model = Student  #Student.objects.all()
    context_object_name = 'student'
    template_name = 'StudentApp/studentdetails.html'

class StudentCreate_View(CreateView):
    model = Student #Student.objects.create()
    fields = '__all__'
    context_object_name = 'form'
    template_name = 'StudentApp/student_form.html'#student_form template is used to create and update data.

class StudentUpdate_View(UpdateView):
    model = Student
    fields = '__all__'
    context_object_name = 'form'
    template_name = 'StudentApp/student_form.html'#student_form template is used to create and update data.

class StudentDelete_View(DeleteView):
    model=Student
    success_url = reverse_lazy('student_list')
    context_object_name = 'student'
    template_name = 'StudentApp/student_confirm_delete.html'

