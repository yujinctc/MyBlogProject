from django.contrib.auth.forms import UserCreationForm

from django import forms

from django.forms import TextInput

from .models import User



class RegisterForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email")

        # widgets = {
        #     # 'username': TextInput (attrs={'class': 'form-control', 'placeholder': 'Your account'}),
        #     # 'email': TextInput (attrs={'class': 'form-control', 'placeholder': 'Email address'}),
        #     # 'password': PasswordInput (attrs={'class': 'form-control', 'placeholder': 'password'}),
        # }
