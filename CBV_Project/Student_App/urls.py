from django.urls import path
from Student_App import views

urlpatterns = [
    path('studentlist/',views.StudentList_View.as_view(),name='student_list'),
    path('',views.StudentList_View.as_view(),name='student_list'),
    path('studentcreate/',views.StudentCreate_View.as_view(),name='student_create'),
    path('student/<int:pk>/detail/',views.StudentDetails_View.as_view(),name='student_detail'),
    path('student/<int:pk>/update/',views.StudentUpdate_View.as_view(),name='student_update'),
    path('student/<int:pk>/delete/',views.StudentDelete_View.as_view(),name='student_delete'),
]