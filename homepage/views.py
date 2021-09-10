from django.shortcuts import redirect, render
from django.http import JsonResponse
from django.urls.conf import path
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
from app_users.models import (InstaUser, Post, Comment, Notification)
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required(login_url='login')
def homepage_view(request):

    posts = Post.objects.order_by('-gen_time')
    active_not = Notification.objects.filter(
        to_user=request.user, active=True).exists()
    request.session['active_not'] = active_not

    # In case user dont't follow any one show people to follow
    flwng = request.user.following.all()
    peoplemayknow = InstaUser.objects.filter(~Q(id__in=[o.id for o in flwng]))
    context = {'posts': posts, 'peoplemayknow': peoplemayknow}
    return render(request, 'homepage/homepage.html', context)


@ csrf_exempt
def comment_view(request):
    if request.is_ajax():
        post = Post.objects.get(id=request.POST.get('post_id', None))
        cmnt = request.POST.get('comment')
        comment = Comment.objects.create(
            comment=cmnt, post=post, cmnt_user=request.user)
        Notification.objects.create(
            post=post, from_user=request.user, to_user=post.user, notify='Commented on your post')
        print('this is img url', request.user.img_url())
        img_url = request.user.img_url()
        data = {'comment': comment.comment, 'username': request.user.username,
                'img_url': img_url}
        return JsonResponse(data)


def liked_view(request):
    post_id = request.GET.get('post_id', None)
    post = Post.objects.prefetch_related('like').get(id=post_id)
    liked = False
    # Like or unlike logic
    if request.user in post.like.all():
        post.like.remove(request.user)
        post.save()

    else:
        liked = True
        post.like.add(request.user)
        post.save()
        Notification.objects.create(
            notify='liked your post', post=post, from_user=request.user, to_user=post.user)

    data = {
        'status': liked
    }
    return JsonResponse(data)


@ login_required(login_url='login')
def notification_view(request):
    nots = Notification.objects.filter(
        to_user=request.user).order_by('-gen_time')
    context = {'notifications': nots}
    return render(request, 'homepage/notificationlist.html', context)


@ login_required(login_url='login')
def explore_view(request):
    post = Post.objects.all()
    context = {'posts': post}
    return render(request, 'homepage/explore.html', context)


@ login_required(login_url='login')
def post_detail(request, pk):
    post = Post.objects.get(id=pk)
    Notification.objects.filter(post=post).update(active=False)
    request.session['active_not'] = False
    context = {'post': post}
    return render(request, 'homepage/postdetail.html', context)
