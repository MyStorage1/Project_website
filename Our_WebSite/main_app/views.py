from django.shortcuts import render


def login_page(request):
    return render(request, 'main_app/login.html')


def register_page(request):
    return render(request, 'main_app/register.html')


def logout_page(request):
    # FIXME
    pass


def home(request):
    return render(request, 'main_app/home.html')


def publications(request):
    return render(request, 'main_app/publications.html')


def about_us(request):
    return render(request, 'main_app/about_us.html')
