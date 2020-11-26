from django.urls import path
from . import views
urlpatterns=[
    path('home',views.index),
    path('contact',views.view),
    path('add',views.addition),
    path('emp',views.employee),
    path('emp/<id>',views.each_employee,name="Emp"),
    path('student',views.displayform),
    path('formv',views.formvalidation),
    path('stu',views.new_stud),
    path('mail',views.email),
    # path('mail1',views.emailmethod),
    path('ses',views.demo_login,name='login'),
    path('home3',views.home3,name='home3')
]