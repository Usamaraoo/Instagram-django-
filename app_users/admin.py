from django.contrib import admin
from .models import InstaUser, Notification, Post, Comment, Story


class NotificationAdmin(admin.ModelAdmin):
    list_display = ['notify', 'to_user',  'active']


admin.site.register(InstaUser)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Notification, NotificationAdmin)
admin.site.register(Story)
