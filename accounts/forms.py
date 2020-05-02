from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# this forms.py is created to add extra field in user registration page- apart from username and password like email

class UserRegistrationForm(UserCreationForm): # This class inherits from UserCreationForm Class
    email  = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email','password1', 'password2']
