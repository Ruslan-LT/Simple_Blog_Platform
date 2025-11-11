from string import ascii_letters, digits

from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.db.models import Q
from django.utils.deconstruct import deconstructible

from .models import User


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={"class": "LoginInput"}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "PasswInput"})
    )

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        password = cleaned_data.get("password")

        user_obj = User.objects.filter(Q(username=username) | Q(email=username)).first()
        if not user_obj:
            raise ValidationError("Невірне ім'я або пароль")
        user = authenticate(username=user_obj.username, password=password)
        if not user:
            raise ValidationError("Невірне ім'я або пароль")
        if user.is_blocked:
            raise ValidationError("Ваш обліковий запис заблоковано.")

        return cleaned_data

    def get_user(self):
        return getattr(self, "user_cache", None)


class RegistrationForm(forms.ModelForm):

    password1 = forms.CharField(
        max_length=30, widget=forms.PasswordInput(attrs={"class": "PasswordInp"})
    )
    password2 = forms.CharField(
        max_length=30, widget=forms.PasswordInput(attrs={"class": "PasswordInp"})
    )

    class Meta:
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
            "password",
        )

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        email = cleaned_data.get("email")
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 != password2:
            raise ValidationError("Паролі не співпадають.")

        if User.objects.filter(username=username).exists():
            self.add_error(
                "username",
                "Даний нікнейм користувача вже існує! Придумайте інший нікнейм.",
            )

        if User.objects.filter(email=email).exists():
            self.add_error(
                "email",
                "На дану електронну пошту вже зареєстровано акаунт! Введіть іншу.",
            )

        if not set(username).issubset(set(ascii_letters + digits)):
            self.add_error(
                "username",
                "У полі нікнейм дозволені лише латинські літери та цифри.",
            )

        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
