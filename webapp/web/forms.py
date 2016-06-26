from django import forms

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm

from web.models import UserInfo


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        max_length=8,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'ID',
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Password',
            }
        )
    )


class UserCreateForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'ID',
            }
        )
    )

    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Password',
            }
        )
    )

    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Password',
            }
        )
    )

    age = forms.NumberInput()

    class Meta:
        model = UserInfo
        fields = ("username", "password1", "password2")

    def save(self, commit=True):
        user = self.save(commit=False)
        #user.age = self.age

        if commit:
            user.save()

        return user


class registerForm(forms.Form):
    username = forms.CharField(label = 'ID', max_length=15)
    password1 = forms.CharField(label='password', widget=forms.PasswordInput())
    password2 = forms.CharField(label='password check', widget=forms.PasswordInput())
    age = forms.CharField(label='age', max_length=3)
