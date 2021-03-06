from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):

    username = forms.CharField(label='Логин', required=True, help_text='нельзя вводить символы: @,/,_',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Введите логин',
            })
    )
    email = forms.EmailField(required=True, label='Email',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Введите email',
            })
    )
    password1 = forms.CharField(label='Пароль', required=True, help_text='пароль должен быть сложным',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Введите пароль',
            }),
    )
    password2 = forms.CharField(label='Подтвердите пароль', required=True, help_text='пароль должен быть сложным',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Введите повторно пароль',
            }),
    )
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2',]


class UserUpdateForm(forms.ModelForm):
    username = forms.CharField(label='Логин', required=True, help_text='нельзя вводить символы: @,/,_',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Введите логин',
            })
    )
    email = forms.EmailField(required=True, label='Email',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Введите email',
            })
    )
    class Meta:
        model = User
        fields = [
            'username',
            'email',
        ]

class ProfileImage(forms.ModelForm):
    def __init__(self, *args, **kwards):
        super(ProfileImage, self).__init__(*args, **kwards)
        self.fields['img'].label = "Изображение профиля"
        self.fields['gender'].label = "Выберите пол"
        self.fields['agreement'].label = "Соглашение про отправку уведомлений на почту"
        self.fields['telephone'].label = "Телефон"

    class Meta:
        model = Profile
        fields = ['img', 'gender', 'agreement', 'telephone',]


