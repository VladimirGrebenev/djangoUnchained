from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):

    username = forms.CharField(
        label='Логин',
        required=True,
        help_text='нельзя вводить символы: @,/,_',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Введите логин',
            })
    )
    email = forms.EmailField(
        required=True,
        label='Email',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder': 'Введите email',
            })
    )
    telephone = forms.CharField(
        required=True,
        label= 'Телефон',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Введите телефон',
            })
    )


    password1 = forms.CharField(
        label='Пароль',
        required=True,
        help_text='пароль должен быть сложным',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Введите пароль',
            }),
    )
    password2 = forms.CharField(
        label='Подтвердите пароль',
        required=True,
        help_text='пароль должен быть сложным',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Введите повторно пароль',
            }),
    )

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'telephone',
            'password1',
            'password2',
        ]