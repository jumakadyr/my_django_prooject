from django.db.models.expressions import result
from django.shortcuts import render
from django.http import HttpResponse
# from django.http import JsonResponse

import random
import string


def task_1(request):
    name = request.GET.get('name', 'Aktan')
    return render(request, 'blog/task_1.html', {'name': name})

# def task_2(request):
#     try:
#         a = float(request.GET.get('a', '2'))
#         b = float(request.GET.get('b', '8'))
#     except (KeyError, ValueError):
#         return JsonResponse({'error': 'Both parameters a and b must be valid numbers and are required.'}, status=400)
#
#     result = a + b
#
#     return render(request , 'blog/task_2.html',dict(a=a, b=b, sum=result))
def task_2(request):
    a = int(request.GET.get("a", '2'))
    b = int(request.GET.get("b", '8'))

    result = a + b
    return render(request, 'blog/task_2.html', {"result": result})

def task_3(request):
    try:
        number = int(request.GET.get('number', '8'))
        result = 'even' if number % 2 == 0 else 'odd'
    except ValueError:
        number = None
        result = 'invalid'

    return render(request, 'blog/task_3.html', {'number': number, 'result': result})




def task_4(request):
    text = request.GET.get('text', 'Django rest freymwork')
    n = request.GET.get('n', '0')

    if not n.isdigit():
        n = 0
    else:
        n = int(n)

    words = text.split()
    filtered_words = [word for word in words if len(word) > n]

    return render(request, 'blog/task_4.html', {'filtered_words': filtered_words})

from django.shortcuts import render

def task_5(request):
    word = request.GET.get('word', 'level')

    if word == word[::-1]:
        result = f"The word '{word}' is a palindrome!"
    else:
        result = f"The word '{word}' is not a palindrome."

    return render(request, 'blog/task_5.html', {'result': result, 'word': word})

def task_6(request):
    year_old = request.GET.get('year_old', '2007')

    if not year_old:
        return HttpResponse("Please indicate the year of birth using the 'year' parameter.")

    if not year_old.isdigit():
        return HttpResponse("Invalid year format. Please enter an integer.")

    birth_year = int(year_old)
    current_year = 2025
    age = current_year - birth_year

    if age < 0:
        return HttpResponse(f"The year of birth is incorrect.")

    return render(request, 'blog/task_6.html', {'year_old': year_old})


def task_7(request):
    number = int(request.GET.get('n', '5'))
    context = [f'{number} x {i} = {number * i}' for i in range(1,11)]

    return render(request, 'blog/task_7.html', {'context':context})



def task_8(request):
    numbers_param = request.GET.get('numbers', '')
    if not numbers_param:
        return HttpResponse("Please provide a list of numbers using the 'numbers' parameter.")

    try:
        numbers = [int(num.strip()) for num in numbers_param.split(',')]
    except ValueError:
        return HttpResponse("Invalid number format. Please provide a list of numbers separated by commas.")
    if not numbers:
        return HttpResponse("The list of numbers is empty. Please provide at least one number.")
    maximum_number = max(numbers)

    return render(request, 'blog/task_8.html', {'maximum_number': maximum_number, 'numbers': numbers_param})

def task_9(request):
    celsius_param = request.GET.get('celsius', '36')
    if not celsius_param:
        return HttpResponse("Please provide a temperature in Celsius using the 'celsius' parameter.")

    try:
        celsius = float(celsius_param)
    except ValueError:
        return HttpResponse("Invalid temperature format. Please provide a numeric value for Celsius.")

    fahrenheit = (celsius * 9/5) + 32

    return render(request, "blog/task_9.html", {'fahrenheit': fahrenheit, 'celsius': celsius_param})



def task_10(request):
    length_param = request.GET.get('length', '5')
    if not length_param:
        return HttpResponse("Please provide the password length using the 'length' parameter.")

    if not length_param.isdigit():
        return HttpResponse("Invalid length format. Please provide a numeric value for the password length.")

    length = int(length_param)
    if length <= 0:
        return HttpResponse("Password length must be greater than 0.")

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choices(characters, k=length))

    return render(request, 'blog/task_10.html', {'password': password, 'length': length_param})


