from django.shortcuts import render, redirect
from .form import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, logout, login


def register_page(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form_ = CreateUserForm()

        if request.method == 'POST':
            form_ = CreateUserForm(request.POST)
            if form_.is_valid():
                form_.save()
                user = form_.cleaned_data.get('username')
                messages.success(request, "Account was created for " + user)
                return redirect('login')

        context = {
            'form': form_
        }
        return render(request, 'main_app/register.html', context)


def login_page(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, "Username OR Password is incorrect")

        context = {}
        return render(request, 'main_app/login.html', context)


def logout_page(request):
    logout(request)
    return redirect('login')


def home(request):
    return render(request, 'main_app/home.html')


def publications(request):
    return render(request, 'main_app/publications.html')


def about_us(request):
    return render(request, 'main_app/about_us.html')
