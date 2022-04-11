from django.contrib import admin
from Student_App.models import Student
#Create Student admin Class
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id','sname','marks','email','mobile','address']

admin.site.register(Student,StudentAdmin)
