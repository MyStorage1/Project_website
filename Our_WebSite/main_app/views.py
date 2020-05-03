from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def publications(request):
    return render(request, 'publications.html')


def about_us(request):
    return render(request, 'about_us.html')
