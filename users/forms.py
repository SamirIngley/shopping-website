from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email=forms.EmailField()

    class Meta: #gives us a nested namespace for configurations. The User model will be affected. When we save it will be added to the User model. We specify the fields in that order. Inherits from UserCreationForm
        model = User 
        fields = ['username', 'email', 'password1', 'password2']

     