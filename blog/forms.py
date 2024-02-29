from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.contrib.auth.models import User
from .models import BlogPost


class SignUpForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control'}), label='Password')
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control'}), label='Confirm Password')


    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name',
                  'email', 'password1', 'password2']
        labels = {'email': 'Email', 'first_name': 'First Name',
                  'last_name': 'Last Name'}
        widgets = {'username': forms.TextInput(attrs={'class': 'form-control'}),
                   'first_name': forms.TextInput(attrs={'class': 'form-control'}),
                   'last_name': forms.TextInput(attrs={'class': 'form-control'}),
                   'email': forms.EmailInput(attrs={'class': 'form-control'})}



class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(
        attrs={'autofocus': True, 'class': 'form-control'}))
    password = forms.CharField(label='Password', strip=False, widget=forms.PasswordInput(
        attrs={'autocomplete': 'current-password', 'class': 'form-control'}))



class PostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'description']
        labels = {'title': 'Title', 'description': 'Description'}
        widgets = {'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter title here...'}),
                   'description': forms.Textarea(attrs={'class': 'form-control' , 'rows': '5', 'placeholder': 'Write your post here...'})}


