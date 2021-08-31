# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from .models import Post, Notification


# @receiver(post_save, sender=Post)
# def create_notification(sender, instance, created, **kwargs):
#     # if created:
#     # Notification.objects.createa(notify='liked your post',post=instance,from_user=instance.user)
#     print('Liked Notification created')
