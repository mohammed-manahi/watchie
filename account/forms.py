from django import forms
from account.models import User, Profile, Favorite, Subscription


class LoginForm(forms.Form):
    # Create login form to authenticate users
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
