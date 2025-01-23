from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('''
        <!DOCTYPE html>
        <html>
        <head>
        <meta charset = utf-8>
        <title>Home</title>
        </head>                      
        <body>
        <h1><em>Первый урок на HTML</em></h1>
        <input type="text"
        placeholder="Ведите текст">
        <button>Готово</button>
        <p>Первый проект</p>
        <abbr title="Github Jumakadyr"><a href="https://github.com/jumakadyr">This is my github</a></abbr>
        </body>
        </html>''')

def factorial(request):
    number = int(request.GET.get('number', 10))
    result = 1
    for i in range(1,number+1):
        result *= i
    return HttpResponse(f"<h1>result: {result}</h1>")


def info(request):
    print(request.GET)
    return HttpResponse(
        f'<h1>Info</h1><br>'
        f'<p>{request.build_absolute_uri()}</p>'
        f'<p>{request.method}</p>'
        f'<p>{request.GET['name']}<br>Age:{request.GET['age']}</p>'
    )