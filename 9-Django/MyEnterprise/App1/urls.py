# App1/urls.py
from django.urls import path
from App1 import views

urlpatterns = [
    path('',views.index),
    path('solicitudes/',views.solicitudes),
    path('formulario/',views.form),
]
