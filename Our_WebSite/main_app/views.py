from django.shortcuts import render, redirect
from .form import CreateUserForm, UserForm
from django.contrib import messages
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.models import Group
from .models import UserModel
from .decorators import unauthenticated_user, allowed_users


@unauthenticated_user
def register_page(request):
    form_ = CreateUserForm()

    if request.method == 'POST':
        form_ = CreateUserForm(request.POST)
        if form_.is_valid():
            user = form_.save()
            username = form_.cleaned_data.get('username')
            email = form_.cleaned_data.get('email')

            group = Group.objects.get(name='user')
            user.groups.add(group)
            UserModel.objects.create(user=user, name=username, email=email)

            messages.success(request, "Account was created for " + username)
            return redirect('login')

    context = {
        'form': form_
    }
    return render(request, 'main_app/register.html', context)


@unauthenticated_user
def login_page(request):
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
    return redirect('home')


def home(request):
    return render(request, 'main_app/home.html')


def publications(request):
    return render(request, 'main_app/publications.html')


def account_settings(request):
    person = request.user.usermodel
    form_ = UserForm(instance=person)

    if request.method == 'POST':
        form_ = UserForm(request.POST, request.FILES, instance=person)
        if form_.is_valid():
            form_.save()

    context = {
        'form': form_
    }
    return render(request, 'main_app/account_settings.html', context)



def admin_page(request):
    return render(request, 'main_app/admin_page.html')


@allowed_users(['user', 'admin', 'author'])
def user_page(request):
    context = {}
    return render(request, 'main_app/user_page.html')


def about_us(request):
    return render(request, 'main_app/about_us.html')
