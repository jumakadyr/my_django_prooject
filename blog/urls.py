from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello),
    path('calculate/', views.sum),
    path('check/', views.check_number),
    path('filter_words/', views.filter_words),
    path('palindrome/', views.palindrome),

]