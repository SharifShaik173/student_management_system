from django.urls import path
from . import views

urlpatterns=[
    path('',views.login_view,name='login'),
    path('dashboard',views.admin,name='dashboard'),
    path('add_student',views.add_student,name='add_student'),
    path('student_details/<int:id>',views.student_details,name='student_details'),
    path('edit/<int:id>',views.edit,name='edit'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('courses',views.courses,name='courses'),
    path('add_course',views.add_course,name='add_course'),
    path('edit_course/<int:id>/', views.edit_course, name='edit_course'),
    path('delete_course/<int:id>/', views.delete_course, name='delete_course'),
    path('search_student',views.search_student,name='search'),
    path('logout',views.logout_view,name='logout'),
]
