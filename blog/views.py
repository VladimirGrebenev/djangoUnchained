from django.shortcuts import render
from .models import News

# Create your views here.


def home(request):
    data = {
        'title': 'Главная',
        'news': News.objects.all(),
    }
    return render(request, 'blog/home.html', data)


def services(request):
    data = {
        'title': 'Услуги',
    }
    return render(request, 'blog/servises.html', data)


def contacts(request):
    data = {
        'title': 'Контакты',
    }
    return render(request, 'blog/contacts.html', data)

