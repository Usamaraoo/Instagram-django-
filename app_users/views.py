from django.db import reset_queries
from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .forms import (PostForm, LoginForm, SignUpForm, UserImageForm)
from .models import (InstaUser, Post)


@login_required(login_url='login')
def user_profile(request, username=None):
    profile_user = InstaUser.objects.get(username=username)
    user_posts = Post.objects.filter(user=profile_user)
    context = {'profile_user': profile_user, 'user_posts': user_posts}
    return render(request, 'app_users/profile_page.html', context)


def signup_view(request):
    form = SignUpForm()

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            print('valid')
            user = form.save()
            user.following.add(user)
            user.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            print('username', username, 'password', raw_password)
            # user = authenticate(username=username, password=raw_password)
            # print(user)
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('set_dp')
        else:
            print(form.errors)
    return render(request, 'app_users/signup.html', {'form': form})


def login_view(request):
    if request.user.is_authenticated:
        return redirect('homepage')
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            credentials = form.cleaned_data
            user = authenticate(
                username=credentials['username'], password=credentials['password'])
            print()
            # username = form.cleaned_data.get('username')
            # raw_password = form.cleaned_data.get('password')
            # user = authenticate(username=username, password=raw_password)
            if user is not None:
                login(request, user)
                return redirect("homepage")

    return render(request, 'app_users/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('/')


@ login_required(login_url='login')
def post_view(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('homepage')
    context = {'form': form}
    return render(request, 'app_users/post.html', context)


@ login_required(login_url='login')
def follow_unfollow(request, pk):
    user_to_follow = InstaUser.objects.get(id=pk)
    if request.user not in user_to_follow.followers.all():
        print('followed')
        user_to_follow.followers.add(request.user)
        request.user.following.add(user_to_follow)
    else:
        print('unfollowed')
        user_to_follow.followers.remove(request.user)
        request.user.following.remove(user_to_follow)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@ login_required(login_url='login')
def following_view(request):
    # if pk is None:
    flwrs = request.user.followers.all()
    flwng = request.user.following.all()
    peoplemayknow = InstaUser.objects.filter(~Q(id__in=[o.id for o in flwng]))
    # else:
    # user = InstaUser.objects.filter(id=pk)
    # flwrs = user.followers.all()
    # flwng = user.following.all()
    context = {'flwrs': flwrs, 'flwing': flwng, 'peoplemayknow': peoplemayknow}
    return render(request, 'app_users/follow.html', context)


def follow_ajax(request):
    followed = False
    print('user came', request.GET.get('username', None))
    user = InstaUser.objects.get(username=request.GET.get('username', None))
    if user is not None:
        if user not in request.user.following.all():
            request.user.following.add(user)
            followed = True
        else:
            request.user.following.remove(user)

    data = {'followed': followed}
    return JsonResponse(data)


def set_dp(request):

    form = UserImageForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save(commit=False)
        dp = form.cleaned_data['profile_pic']
        request.user.profile_pic = dp
        request.user.save()
        return JsonResponse({'message': 'works'})
    context = {'form': form}

    return render(request, 'app_users/setprofile.html', context)
