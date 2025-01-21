"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

def home(request):
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
        <abbr title="This is DJANGO project">For beginners</abbr>
        </body>
        </html>''')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home)
]

