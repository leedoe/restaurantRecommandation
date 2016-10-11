from django import forms

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm

from web.models import UserInfo


class LoginForm(AuthenticationForm):
    username = forms.EmailField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Email',
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
    username = forms.EmailField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Email',
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
    username = forms.EmailField(
        label = 'ID',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Email',
            }
        )
    )
    password1 = forms.CharField(
        label='password',
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Password',
            }
        )
    )
    password2 = forms.CharField(
        label='password check',
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Password',
            }
        )
    )
    age = forms.CharField(
        label='age',
        max_length=3,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Age',
            }
        )
    )
