from django.shortcuts import redirect, render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from app_users.models import (InstaUser, Post, Comment)


# Create your views here.


def homepage_view(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'homepage/homepage.html', context)


@csrf_exempt
def comment_view(request):
    if request.is_ajax():
        post = Post.objects.get(id=request.POST.get('post_id', None))
        cmnt = request.POST.get('comment')
        comment = Comment.objects.create(
            comment=cmnt, post=post, cmnt_user=request.user)
        img_url = request.user.profile_pic.url if request.user.profile_pic else '/static/resource_imgs/camera.png'
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
    data = {
        'status': liked
    }
    return JsonResponse(data)
