from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm, TextInput, Textarea

from .models import POST


class NewUserForm(forms.ModelForm):

    class Meta:
        model = POST
        fields = ["username", "first_name" , "last_name", "phone_number", "birthday", "email", "city"]


