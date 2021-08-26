from django.shortcuts import redirect, render
from app_users.models import (InstaUser,  Post, Comment)
# Create your views here.


def homepage_view(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'homepage/homepage.html', context)


def liked_view(request, pk):
    post = Post.objects.prefetch_related('like').get(id=pk)

    # Like or unlike logic
    if request.user in post.like.all():
        print('user removed')
        post.like.remove(request.user)
        post.save()
    else:
        post.like.add(request.user)
        post.save()
    return redirect('homepage')
