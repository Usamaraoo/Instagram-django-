from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect
from .forms import PostForm
from .models import InstaUser, Post


def user_profile(request, username=None):
    profile_user = InstaUser.objects.get(username=username)
    user_posts = Post.objects.filter(user=profile_user)
    context = {'profile_user': profile_user, 'user_posts': user_posts}
    return render(request, 'app_users/profile_page.html', context)


def signup_view(request):
    return render(request, 'app_users/signup.html')


def login_view(request):
    return render(request, 'app_users/login.html')


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
