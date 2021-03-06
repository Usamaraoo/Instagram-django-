from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Post, InstaUser, Story


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['post_img', 'description']
        exclude = ['user']


class StoryForm(forms.ModelForm):
    class Meta:
        model = Story
        fields = ['story_img']


class LoginForm(forms.Form):
    """user login form"""
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())


class SignUpForm(UserCreationForm):
    # date_of_birth = forms.DateTimeField()
    class Meta:
        model = InstaUser
        fields = ('username', 'email', 'password1', 'password2')


class UserImageForm(forms.ModelForm):
    # date_of_birth = forms.DateTimeField()
    class Meta:
        model = InstaUser
        fields = ['profile_pic', ]
