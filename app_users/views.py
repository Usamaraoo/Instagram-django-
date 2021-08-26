from django.shortcuts import redirect, render
from django.http import HttpResponse
from .forms import PostForm
from .models import InstaUser, Post


def user_profile(request):
    return render(request, 'app_users/profile_page.html', )


def signup_view(request):
    return render(request, 'app_users/signup.html')


def login_view(request):
    return render(request, 'app_users/login.html')


def post_view(request):
    form = PostForm()
    if request.method == 'POST':

        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()

            return redirect('homepage')
    context = {'form': form}
    return render(request, 'app_users/post.html', context)
