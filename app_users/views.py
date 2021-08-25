from django.shortcuts import render
from django.http import HttpResponse


def user_profile(request):

    return render(request, 'app_users/profile_page.html', )


def signup_view(request):
    return render(request, 'app_users/signup.html')


def login_view(request):
    return render(request, 'app_users/login.html')
