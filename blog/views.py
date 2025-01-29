from django.shortcuts import render
from django.http import HttpResponse
# from django.http import JsonResponse
import random
import string



def home(request):
    return render(request, 'base.html')

# def task_0(request):
#     email = request.POST.get('email')
#     password = request.POST.get('password')
#
#     if password == '12345' and email == 'exampl@gmail.com':
#         return render(request, 'blog/task_0_success.html')
#     context = {
#         'is_true': True if email else None,
#         'Error': "Email or password is incorrect!"
#     }
#     return render(request, 'blog/task_0.html', context=context)
#

def task_0(request):
    context = {'error': "Email or password is incorrect!"}
    return render(request, 'blog/task_0.html', context=context)

def task_1(request):
    email = request.POST.get('email')
    password = request.POST.get('password')

    if password == '12345' and email == 'example@gmail.com':
        return render(request, 'blog/task_0_success.html')
    name = request.GET.get('name', 'Aktan')
    return render(request, 'blog/task_1.html', {'aty': name})
