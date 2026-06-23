from django.urls import path
from .import views

urlpatterns = [
    path('index/',views.index),
    path('car_list/',views.car_list, name='car_list'),
    path('car_details/<int:id>/',views.car_details, name='car_details'),
    path('car_booking/<int:id>/',views.car_booking, name='car_booking'),
    path('',views.get_register, name='get_register'),
    path('get_login/',views.get_login, name='get_login'),
    path('student_home/',views.student_home, name='student_home'),
    path('add_expense/',views.add_expense, name='add_expense'),
    path('delete/<int:id>/',views.delete_expense,name="delete_expense"),
    path('edit/<int:id>/',views.edit_expense,name="edit_expense"),
    

]