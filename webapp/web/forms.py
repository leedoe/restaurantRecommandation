from django import forms

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm

from webapp.web.models import UserInfo


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
    age = forms.NumberInput(required=True)

    class Meta:
        model = UserInfo
        fields = ("username", "password1", "password2", "age")

    def save(self, commit=True):
        user = self.save(commit=False)
        user.age = self.age

        if commit:
            user.save()

        return user