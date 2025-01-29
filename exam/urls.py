from django.urls import path
from . import views

urlpatterns = [
    path('exam-1/', views.exam_1, name='exam-1')
]