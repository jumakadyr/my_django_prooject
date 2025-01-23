from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index),
    path('factorial/',views.factorial),
    path('info/',views.info)
]