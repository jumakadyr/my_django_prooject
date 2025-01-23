from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.template.backends.django import reraise

def hello(request):
    name = request.GET.get('name','Гость')
    greeting = f"<p>Hello, {name}! Welcome to our site.</p>"

    return HttpResponse(greeting)


def sum(request):
    try:
        a = float(request.GET['a'])
        b = float(request.GET['b'])
    except (KeyError, ValueError):
        return JsonResponse({'error': 'Both parameters a and b must be valid numbers and are required.'}, status=400)

    result = a + b

    return JsonResponse({'a': a, 'b': b, 'sum': result})


def check_number(request):
    number = request.GET.get('number')

    if number is not None and number.isdigit():
        number = int(number)

        if number % 2 == 0:
            return HttpResponse(f"{number}--> even numbers")
        else:
            return HttpResponse(f"{number}--> odd numbers")

    else:
        return HttpResponse("Please provide a valid number via the 'number' parameter.")




def filter_words(request):
    text = request.GET.get('text', '')
    n = int(request.GET.get('n', 0))

    words = text.split()

    filtered_words = [word for word in words if len(word) > n]

    return JsonResponse(filtered_words, safe=False)


def palindrome(request):
    word = request.GET.get('word', '')

    if word == word[::-1]:
        return HttpResponse(f'Word {word} is a palindrome')
    else:
        return HttpResponse(f'Word {word} is not a palindrome')

def age_old(request):
    your_old = request.GET.get('your_old', '')
