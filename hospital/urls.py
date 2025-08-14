from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('patients/', views.patients, name='patients'),
    path('doctors/', views.doctors, name='doctors'),
    path('appointments/', views.appointments, name='appointments'),
]