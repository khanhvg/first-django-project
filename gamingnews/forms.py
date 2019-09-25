from django import forms
from django.contrib.auth.models import User
from .models import UserProfileInfo, Contact



class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class UserProfileInfoForm(forms.ModelForm):
    picture = forms.ImageField(required=False)

    class Meta:
        model = UserProfileInfo
        exclude = ('user',)


class FormContact(forms.ModelForm):
    name = forms.CharField(max_length=100)
    phone = forms.CharField(max_length=200)
    email = forms.EmailField()
    message = forms.Textarea()

    class Meta:
        model = Contact
        fields = ['name', 'phone', 'email', 'message']
