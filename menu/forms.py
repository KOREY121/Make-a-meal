from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User



class LoginForm(AuthenticationForm):
    username= forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your Username',
        'class': 'w-full py-4 px-6 rounded-full',
    }))
    password= forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your Password',
        'class': 'w-full py-4 px-6 rounded-full',
    }))
    
class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    username= forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your Username',
        'class': 'w-full py-4 px-6 rounded-full',
    }))
    email= forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': 'Your Email',
        'class': 'w-full py-4 px-6 rounded-full',
    }))
    address= forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your address',
        'class': 'w-full py-4 px-6 rounded-full',
    }))
    location= forms.ChoiceField(choices=[
            ('', 'Select your country'),
            ('NG', 'Nigeria'),
            ('US', 'United States'),
            ('UK', 'United Kingdom'),
            ('CA', 'Canada'),
            ('GH', 'Ghana'),
            ('KE', 'Kenya'),
        ],
        widget=forms.Select(attrs={
        'placeholder': 'Your address',
        'class': 'w-full py-4 px-6 rounded-full',
    }))
    gender = forms.ChoiceField(
        choices=[
            ('', 'Select gender'),
            ('M', 'Male'),
            ('F', 'Female'),
            ('O', 'Other'),
        ],
        widget=forms.Select(attrs={
            'class': 'w-full py-4 px-6 rounded-full'
        })
    )
    password1= forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your Password',
        'class': 'w-full py-4 px-6 rounded-full',
    }))
    password2= forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Repeat Password',
        'class': 'w-full py-4 px-6 rounded-full',
    }))