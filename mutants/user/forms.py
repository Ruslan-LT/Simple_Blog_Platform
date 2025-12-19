from inspect import signature as _mutmut_signature
from string import ascii_letters, digits
from typing import Annotated, Callable, ClassVar

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

MutantDict = Annotated[dict[str, Callable], "Mutant"]


def _mutmut_trampoline(orig, mutants, call_args, call_kwargs, self_arg=None):
    """Forward call to original or mutated function, depending on the environment"""
    import os

    mutant_under_test = os.environ["MUTANT_UNDER_TEST"]
    if mutant_under_test == "fail":
        from mutmut.__main__ import MutmutProgrammaticFailException

        raise MutmutProgrammaticFailException("Failed programmatically")
    elif mutant_under_test == "stats":
        from mutmut.__main__ import record_trampoline_hit

        record_trampoline_hit(orig.__module__ + "." + orig.__name__)
        result = orig(*call_args, **call_kwargs)
        return result
    prefix = orig.__module__ + "." + orig.__name__ + "__mutmut_"
    if not mutant_under_test.startswith(prefix):
        result = orig(*call_args, **call_kwargs)
        return result
    mutant_name = mutant_under_test.rpartition(".")[-1]
    if self_arg is not None:
        # call to a class method where self is not bound
        result = mutants[mutant_name](self_arg, *call_args, **call_kwargs)
    else:
        result = mutants[mutant_name](*call_args, **call_kwargs)
    return result


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={"class": "LoginInput"}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "PasswInput"})
    )

    def xǁLoginFormǁclean__mutmut_orig(self):
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

        self.user_cache = user

        return cleaned_data

    def xǁLoginFormǁclean__mutmut_1(self):
        cleaned_data = None
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

        self.user_cache = user

        return cleaned_data

    def xǁLoginFormǁclean__mutmut_2(self):
        cleaned_data = super().clean()
        username = None
        password = cleaned_data.get("password")

        user_obj = User.objects.filter(Q(username=username) | Q(email=username)).first()
        if not user_obj:
            raise ValidationError("Невірне ім'я або пароль")
        user = authenticate(username=user_obj.username, password=password)
        if not user:
            raise ValidationError("Невірне ім'я або пароль")
        if user.is_blocked:
            raise ValidationError("Ваш обліковий запис заблоковано.")

        self.user_cache = user

        return cleaned_data

    def xǁLoginFormǁclean__mutmut_3(self):
        cleaned_data = super().clean()
        username = cleaned_data.get(None)
        password = cleaned_data.get("password")

        user_obj = User.objects.filter(Q(username=username) | Q(email=username)).first()
        if not user_obj:
            raise ValidationError("Невірне ім'я або пароль")
        user = authenticate(username=user_obj.username, password=password)
        if not user:
            raise ValidationError("Невірне ім'я або пароль")
        if user.is_blocked:
            raise ValidationError("Ваш обліковий запис заблоковано.")

        self.user_cache = user

        return cleaned_data

    def xǁLoginFormǁclean__mutmut_4(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("XXusernameXX")
        password = cleaned_data.get("password")

        user_obj = User.objects.filter(Q(username=username) | Q(email=username)).first()
        if not user_obj:
            raise ValidationError("Невірне ім'я або пароль")
        user = authenticate(username=user_obj.username, password=password)
        if not user:
            raise ValidationError("Невірне ім'я або пароль")
        if user.is_blocked:
            raise ValidationError("Ваш обліковий запис заблоковано.")

        self.user_cache = user

        return cleaned_data

    def xǁLoginFormǁclean__mutmut_5(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("USERNAME")
        password = cleaned_data.get("password")

        user_obj = User.objects.filter(Q(username=username) | Q(email=username)).first()
        if not user_obj:
            raise ValidationError("Невірне ім'я або пароль")
        user = authenticate(username=user_obj.username, password=password)
        if not user:
            raise ValidationError("Невірне ім'я або пароль")
        if user.is_blocked:
            raise ValidationError("Ваш обліковий запис заблоковано.")

        self.user_cache = user

        return cleaned_data

    def xǁLoginFormǁclean__mutmut_6(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        password = None

        user_obj = User.objects.filter(Q(username=username) | Q(email=username)).first()
        if not user_obj:
            raise ValidationError("Невірне ім'я або пароль")
        user = authenticate(username=user_obj.username, password=password)
        if not user:
            raise ValidationError("Невірне ім'я або пароль")
        if user.is_blocked:
            raise ValidationError("Ваш обліковий запис заблоковано.")

        self.user_cache = user

        return cleaned_data

    def xǁLoginFormǁclean__mutmut_7(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        password = cleaned_data.get(None)

        user_obj = User.objects.filter(Q(username=username) | Q(email=username)).first()
        if not user_obj:
            raise ValidationError("Невірне ім'я або пароль")
        user = authenticate(username=user_obj.username, password=password)
        if not user:
            raise ValidationError("Невірне ім'я або пароль")
        if user.is_blocked:
            raise ValidationError("Ваш обліковий запис заблоковано.")

        self.user_cache = user

        return cleaned_data

    def xǁLoginFormǁclean__mutmut_8(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        password = cleaned_data.get("XXpasswordXX")

        user_obj = User.objects.filter(Q(username=username) | Q(email=username)).first()
        if not user_obj:
            raise ValidationError("Невірне ім'я або пароль")
        user = authenticate(username=user_obj.username, password=password)
        if not user:
            raise ValidationError("Невірне ім'я або пароль")
        if user.is_blocked:
            raise ValidationError("Ваш обліковий запис заблоковано.")

        self.user_cache = user

        return cleaned_data

    def xǁLoginFormǁclean__mutmut_9(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        password = cleaned_data.get("PASSWORD")

        user_obj = User.objects.filter(Q(username=username) | Q(email=username)).first()
        if not user_obj:
            raise ValidationError("Невірне ім'я або пароль")
        user = authenticate(username=user_obj.username, password=password)
        if not user:
            raise ValidationError("Невірне ім'я або пароль")
        if user.is_blocked:
            raise ValidationError("Ваш обліковий запис заблоковано.")

        self.user_cache = user

        return cleaned_data

    def xǁLoginFormǁclean__mutmut_10(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        password = cleaned_data.get("password")

        user_obj = None
        if not user_obj:
            raise ValidationError("Невірне ім'я або пароль")
        user = authenticate(username=user_obj.username, password=password)
        if not user:
            raise ValidationError("Невірне ім'я або пароль")
        if user.is_blocked:
            raise ValidationError("Ваш обліковий запис заблоковано.")

        self.user_cache = user

        return cleaned_data

    def xǁLoginFormǁclean__mutmut_11(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        password = cleaned_data.get("password")

        user_obj = User.objects.filter(None).first()
        if not user_obj:
            raise ValidationError("Невірне ім'я або пароль")
        user = authenticate(username=user_obj.username, password=password)
        if not user:
            raise ValidationError("Невірне ім'я або пароль")
        if user.is_blocked:
            raise ValidationError("Ваш обліковий запис заблоковано.")

        self.user_cache = user

        return cleaned_data

    def xǁLoginFormǁclean__mutmut_12(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        password = cleaned_data.get("password")

        user_obj = User.objects.filter(Q(username=username) & Q(email=username)).first()
        if not user_obj:
            raise ValidationError("Невірне ім'я або пароль")
        user = authenticate(username=user_obj.username, password=password)
        if not user:
            raise ValidationError("Невірне ім'я або пароль")
        if user.is_blocked:
            raise ValidationError("Ваш обліковий запис заблоковано.")

        self.user_cache = user

        return cleaned_data

    def xǁLoginFormǁclean__mutmut_13(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        password = cleaned_data.get("password")

        user_obj = User.objects.filter(Q(username=None) | Q(email=username)).first()
        if not user_obj:
            raise ValidationError("Невірне ім'я або пароль")
        user = authenticate(username=user_obj.username, password=password)
        if not user:
            raise ValidationError("Невірне ім'я або пароль")
        if user.is_blocked:
            raise ValidationError("Ваш обліковий запис заблоковано.")

        self.user_cache = user

        return cleaned_data

    def xǁLoginFormǁclean__mutmut_14(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        password = cleaned_data.get("password")

        user_obj = User.objects.filter(Q(username=username) | Q(email=None)).first()
        if not user_obj:
            raise ValidationError("Невірне ім'я або пароль")
        user = authenticate(username=user_obj.username, password=password)
        if not user:
            raise ValidationError("Невірне ім'я або пароль")
        if user.is_blocked:
            raise ValidationError("Ваш обліковий запис заблоковано.")

        self.user_cache = user

        return cleaned_data

    def xǁLoginFormǁclean__mutmut_15(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        password = cleaned_data.get("password")

        user_obj = User.objects.filter(Q(username=username) | Q(email=username)).first()
        if user_obj:
            raise ValidationError("Невірне ім'я або пароль")
        user = authenticate(username=user_obj.username, password=password)
        if not user:
            raise ValidationError("Невірне ім'я або пароль")
        if user.is_blocked:
            raise ValidationError("Ваш обліковий запис заблоковано.")

        self.user_cache = user

        return cleaned_data

    def xǁLoginFormǁclean__mutmut_16(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        password = cleaned_data.get("password")

        user_obj = User.objects.filter(Q(username=username) | Q(email=username)).first()
        if not user_obj:
            raise ValidationError(None)
        user = authenticate(username=user_obj.username, password=password)
        if not user:
            raise ValidationError("Невірне ім'я або пароль")
        if user.is_blocked:
            raise ValidationError("Ваш обліковий запис заблоковано.")

        self.user_cache = user

        return cleaned_data

    def xǁLoginFormǁclean__mutmut_17(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        password = cleaned_data.get("password")

        user_obj = User.objects.filter(Q(username=username) | Q(email=username)).first()
        if not user_obj:
            raise ValidationError("XXНевірне ім'я або парольXX")
        user = authenticate(username=user_obj.username, password=password)
        if not user:
            raise ValidationError("Невірне ім'я або пароль")
        if user.is_blocked:
            raise ValidationError("Ваш обліковий запис заблоковано.")

        self.user_cache = user

        return cleaned_data

    def xǁLoginFormǁclean__mutmut_18(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        password = cleaned_data.get("password")

        user_obj = User.objects.filter(Q(username=username) | Q(email=username)).first()
        if not user_obj:
            raise ValidationError("невірне ім'я або пароль")
        user = authenticate(username=user_obj.username, password=password)
        if not user:
            raise ValidationError("Невірне ім'я або пароль")
        if user.is_blocked:
            raise ValidationError("Ваш обліковий запис заблоковано.")

        self.user_cache = user

        return cleaned_data

    def xǁLoginFormǁclean__mutmut_19(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        password = cleaned_data.get("password")

        user_obj = User.objects.filter(Q(username=username) | Q(email=username)).first()
        if not user_obj:
            raise ValidationError("НЕВІРНЕ ІМ'Я АБО ПАРОЛЬ")
        user = authenticate(username=user_obj.username, password=password)
        if not user:
            raise ValidationError("Невірне ім'я або пароль")
        if user.is_blocked:
            raise ValidationError("Ваш обліковий запис заблоковано.")

        self.user_cache = user

        return cleaned_data

    def xǁLoginFormǁclean__mutmut_20(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        password = cleaned_data.get("password")

        user_obj = User.objects.filter(Q(username=username) | Q(email=username)).first()
        if not user_obj:
            raise ValidationError("Невірне ім'я або пароль")
        user = None
        if not user:
            raise ValidationError("Невірне ім'я або пароль")
        if user.is_blocked:
            raise ValidationError("Ваш обліковий запис заблоковано.")

        self.user_cache = user

        return cleaned_data

    def xǁLoginFormǁclean__mutmut_21(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        password = cleaned_data.get("password")

        user_obj = User.objects.filter(Q(username=username) | Q(email=username)).first()
        if not user_obj:
            raise ValidationError("Невірне ім'я або пароль")
        user = authenticate(username=None, password=password)
        if not user:
            raise ValidationError("Невірне ім'я або пароль")
        if user.is_blocked:
            raise ValidationError("Ваш обліковий запис заблоковано.")

        self.user_cache = user

        return cleaned_data

    def xǁLoginFormǁclean__mutmut_22(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        password = cleaned_data.get("password")

        user_obj = User.objects.filter(Q(username=username) | Q(email=username)).first()
        if not user_obj:
            raise ValidationError("Невірне ім'я або пароль")
        user = authenticate(username=user_obj.username, password=None)
        if not user:
            raise ValidationError("Невірне ім'я або пароль")
        if user.is_blocked:
            raise ValidationError("Ваш обліковий запис заблоковано.")

        self.user_cache = user

        return cleaned_data

    def xǁLoginFormǁclean__mutmut_23(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        password = cleaned_data.get("password")

        user_obj = User.objects.filter(Q(username=username) | Q(email=username)).first()
        if not user_obj:
            raise ValidationError("Невірне ім'я або пароль")
        user = authenticate(password=password)
        if not user:
            raise ValidationError("Невірне ім'я або пароль")
        if user.is_blocked:
            raise ValidationError("Ваш обліковий запис заблоковано.")

        self.user_cache = user

        return cleaned_data

    def xǁLoginFormǁclean__mutmut_24(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        password = cleaned_data.get("password")

        user_obj = User.objects.filter(Q(username=username) | Q(email=username)).first()
        if not user_obj:
            raise ValidationError("Невірне ім'я або пароль")
        user = authenticate(
            username=user_obj.username,
        )
        if not user:
            raise ValidationError("Невірне ім'я або пароль")
        if user.is_blocked:
            raise ValidationError("Ваш обліковий запис заблоковано.")

        self.user_cache = user

        return cleaned_data

    def xǁLoginFormǁclean__mutmut_25(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        password = cleaned_data.get("password")

        user_obj = User.objects.filter(Q(username=username) | Q(email=username)).first()
        if not user_obj:
            raise ValidationError("Невірне ім'я або пароль")
        user = authenticate(username=user_obj.username, password=password)
        if user:
            raise ValidationError("Невірне ім'я або пароль")
        if user.is_blocked:
            raise ValidationError("Ваш обліковий запис заблоковано.")

        self.user_cache = user

        return cleaned_data

    def xǁLoginFormǁclean__mutmut_26(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        password = cleaned_data.get("password")

        user_obj = User.objects.filter(Q(username=username) | Q(email=username)).first()
        if not user_obj:
            raise ValidationError("Невірне ім'я або пароль")
        user = authenticate(username=user_obj.username, password=password)
        if not user:
            raise ValidationError(None)
        if user.is_blocked:
            raise ValidationError("Ваш обліковий запис заблоковано.")

        self.user_cache = user

        return cleaned_data

    def xǁLoginFormǁclean__mutmut_27(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        password = cleaned_data.get("password")

        user_obj = User.objects.filter(Q(username=username) | Q(email=username)).first()
        if not user_obj:
            raise ValidationError("Невірне ім'я або пароль")
        user = authenticate(username=user_obj.username, password=password)
        if not user:
            raise ValidationError("XXНевірне ім'я або парольXX")
        if user.is_blocked:
            raise ValidationError("Ваш обліковий запис заблоковано.")

        self.user_cache = user

        return cleaned_data

    def xǁLoginFormǁclean__mutmut_28(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        password = cleaned_data.get("password")

        user_obj = User.objects.filter(Q(username=username) | Q(email=username)).first()
        if not user_obj:
            raise ValidationError("Невірне ім'я або пароль")
        user = authenticate(username=user_obj.username, password=password)
        if not user:
            raise ValidationError("невірне ім'я або пароль")
        if user.is_blocked:
            raise ValidationError("Ваш обліковий запис заблоковано.")

        self.user_cache = user

        return cleaned_data

    def xǁLoginFormǁclean__mutmut_29(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        password = cleaned_data.get("password")

        user_obj = User.objects.filter(Q(username=username) | Q(email=username)).first()
        if not user_obj:
            raise ValidationError("Невірне ім'я або пароль")
        user = authenticate(username=user_obj.username, password=password)
        if not user:
            raise ValidationError("НЕВІРНЕ ІМ'Я АБО ПАРОЛЬ")
        if user.is_blocked:
            raise ValidationError("Ваш обліковий запис заблоковано.")

        self.user_cache = user

        return cleaned_data

    def xǁLoginFormǁclean__mutmut_30(self):
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
            raise ValidationError(None)

        self.user_cache = user

        return cleaned_data

    def xǁLoginFormǁclean__mutmut_31(self):
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
            raise ValidationError("XXВаш обліковий запис заблоковано.XX")

        self.user_cache = user

        return cleaned_data

    def xǁLoginFormǁclean__mutmut_32(self):
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
            raise ValidationError("ваш обліковий запис заблоковано.")

        self.user_cache = user

        return cleaned_data

    def xǁLoginFormǁclean__mutmut_33(self):
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
            raise ValidationError("ВАШ ОБЛІКОВИЙ ЗАПИС ЗАБЛОКОВАНО.")

        self.user_cache = user

        return cleaned_data

    def xǁLoginFormǁclean__mutmut_34(self):
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

        self.user_cache = None

        return cleaned_data

    xǁLoginFormǁclean__mutmut_mutants: ClassVar[MutantDict] = {
        "xǁLoginFormǁclean__mutmut_1": xǁLoginFormǁclean__mutmut_1,
        "xǁLoginFormǁclean__mutmut_2": xǁLoginFormǁclean__mutmut_2,
        "xǁLoginFormǁclean__mutmut_3": xǁLoginFormǁclean__mutmut_3,
        "xǁLoginFormǁclean__mutmut_4": xǁLoginFormǁclean__mutmut_4,
        "xǁLoginFormǁclean__mutmut_5": xǁLoginFormǁclean__mutmut_5,
        "xǁLoginFormǁclean__mutmut_6": xǁLoginFormǁclean__mutmut_6,
        "xǁLoginFormǁclean__mutmut_7": xǁLoginFormǁclean__mutmut_7,
        "xǁLoginFormǁclean__mutmut_8": xǁLoginFormǁclean__mutmut_8,
        "xǁLoginFormǁclean__mutmut_9": xǁLoginFormǁclean__mutmut_9,
        "xǁLoginFormǁclean__mutmut_10": xǁLoginFormǁclean__mutmut_10,
        "xǁLoginFormǁclean__mutmut_11": xǁLoginFormǁclean__mutmut_11,
        "xǁLoginFormǁclean__mutmut_12": xǁLoginFormǁclean__mutmut_12,
        "xǁLoginFormǁclean__mutmut_13": xǁLoginFormǁclean__mutmut_13,
        "xǁLoginFormǁclean__mutmut_14": xǁLoginFormǁclean__mutmut_14,
        "xǁLoginFormǁclean__mutmut_15": xǁLoginFormǁclean__mutmut_15,
        "xǁLoginFormǁclean__mutmut_16": xǁLoginFormǁclean__mutmut_16,
        "xǁLoginFormǁclean__mutmut_17": xǁLoginFormǁclean__mutmut_17,
        "xǁLoginFormǁclean__mutmut_18": xǁLoginFormǁclean__mutmut_18,
        "xǁLoginFormǁclean__mutmut_19": xǁLoginFormǁclean__mutmut_19,
        "xǁLoginFormǁclean__mutmut_20": xǁLoginFormǁclean__mutmut_20,
        "xǁLoginFormǁclean__mutmut_21": xǁLoginFormǁclean__mutmut_21,
        "xǁLoginFormǁclean__mutmut_22": xǁLoginFormǁclean__mutmut_22,
        "xǁLoginFormǁclean__mutmut_23": xǁLoginFormǁclean__mutmut_23,
        "xǁLoginFormǁclean__mutmut_24": xǁLoginFormǁclean__mutmut_24,
        "xǁLoginFormǁclean__mutmut_25": xǁLoginFormǁclean__mutmut_25,
        "xǁLoginFormǁclean__mutmut_26": xǁLoginFormǁclean__mutmut_26,
        "xǁLoginFormǁclean__mutmut_27": xǁLoginFormǁclean__mutmut_27,
        "xǁLoginFormǁclean__mutmut_28": xǁLoginFormǁclean__mutmut_28,
        "xǁLoginFormǁclean__mutmut_29": xǁLoginFormǁclean__mutmut_29,
        "xǁLoginFormǁclean__mutmut_30": xǁLoginFormǁclean__mutmut_30,
        "xǁLoginFormǁclean__mutmut_31": xǁLoginFormǁclean__mutmut_31,
        "xǁLoginFormǁclean__mutmut_32": xǁLoginFormǁclean__mutmut_32,
        "xǁLoginFormǁclean__mutmut_33": xǁLoginFormǁclean__mutmut_33,
        "xǁLoginFormǁclean__mutmut_34": xǁLoginFormǁclean__mutmut_34,
    }

    def clean(self, *args, **kwargs):
        result = _mutmut_trampoline(
            object.__getattribute__(self, "xǁLoginFormǁclean__mutmut_orig"),
            object.__getattribute__(self, "xǁLoginFormǁclean__mutmut_mutants"),
            args,
            kwargs,
            self,
        )
        return result

    clean.__signature__ = _mutmut_signature(xǁLoginFormǁclean__mutmut_orig)
    xǁLoginFormǁclean__mutmut_orig.__name__ = "xǁLoginFormǁclean"

    def xǁLoginFormǁget_user__mutmut_orig(self):
        return getattr(self, "user_cache", None)

    def xǁLoginFormǁget_user__mutmut_1(self):
        return getattr(None, "user_cache", None)

    def xǁLoginFormǁget_user__mutmut_2(self):
        return getattr(self, None, None)

    def xǁLoginFormǁget_user__mutmut_3(self):
        return getattr("user_cache", None)

    def xǁLoginFormǁget_user__mutmut_4(self):
        return getattr(self, None)

    def xǁLoginFormǁget_user__mutmut_5(self):
        return getattr(
            self,
            "user_cache",
        )

    def xǁLoginFormǁget_user__mutmut_6(self):
        return getattr(self, "XXuser_cacheXX", None)

    def xǁLoginFormǁget_user__mutmut_7(self):
        return getattr(self, "USER_CACHE", None)

    xǁLoginFormǁget_user__mutmut_mutants: ClassVar[MutantDict] = {
        "xǁLoginFormǁget_user__mutmut_1": xǁLoginFormǁget_user__mutmut_1,
        "xǁLoginFormǁget_user__mutmut_2": xǁLoginFormǁget_user__mutmut_2,
        "xǁLoginFormǁget_user__mutmut_3": xǁLoginFormǁget_user__mutmut_3,
        "xǁLoginFormǁget_user__mutmut_4": xǁLoginFormǁget_user__mutmut_4,
        "xǁLoginFormǁget_user__mutmut_5": xǁLoginFormǁget_user__mutmut_5,
        "xǁLoginFormǁget_user__mutmut_6": xǁLoginFormǁget_user__mutmut_6,
        "xǁLoginFormǁget_user__mutmut_7": xǁLoginFormǁget_user__mutmut_7,
    }

    def get_user(self, *args, **kwargs):
        result = _mutmut_trampoline(
            object.__getattribute__(self, "xǁLoginFormǁget_user__mutmut_orig"),
            object.__getattribute__(self, "xǁLoginFormǁget_user__mutmut_mutants"),
            args,
            kwargs,
            self,
        )
        return result

    get_user.__signature__ = _mutmut_signature(xǁLoginFormǁget_user__mutmut_orig)
    xǁLoginFormǁget_user__mutmut_orig.__name__ = "xǁLoginFormǁget_user"


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

    def xǁRegistrationFormǁclean__mutmut_orig(self):
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

    def xǁRegistrationFormǁclean__mutmut_1(self):
        cleaned_data = None
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

    def xǁRegistrationFormǁclean__mutmut_2(self):
        cleaned_data = super().clean()
        username = None
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

    def xǁRegistrationFormǁclean__mutmut_3(self):
        cleaned_data = super().clean()
        username = cleaned_data.get(None)
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

    def xǁRegistrationFormǁclean__mutmut_4(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("XXusernameXX")
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

    def xǁRegistrationFormǁclean__mutmut_5(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("USERNAME")
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

    def xǁRegistrationFormǁclean__mutmut_6(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        email = None
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

    def xǁRegistrationFormǁclean__mutmut_7(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        email = cleaned_data.get(None)
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

    def xǁRegistrationFormǁclean__mutmut_8(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        email = cleaned_data.get("XXemailXX")
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

    def xǁRegistrationFormǁclean__mutmut_9(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        email = cleaned_data.get("EMAIL")
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

    def xǁRegistrationFormǁclean__mutmut_10(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        email = cleaned_data.get("email")
        password1 = None
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

    def xǁRegistrationFormǁclean__mutmut_11(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        email = cleaned_data.get("email")
        password1 = cleaned_data.get(None)
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

    def xǁRegistrationFormǁclean__mutmut_12(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        email = cleaned_data.get("email")
        password1 = cleaned_data.get("XXpassword1XX")
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

    def xǁRegistrationFormǁclean__mutmut_13(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        email = cleaned_data.get("email")
        password1 = cleaned_data.get("PASSWORD1")
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

    def xǁRegistrationFormǁclean__mutmut_14(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        email = cleaned_data.get("email")
        password1 = cleaned_data.get("password1")
        password2 = None

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

    def xǁRegistrationFormǁclean__mutmut_15(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        email = cleaned_data.get("email")
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get(None)

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

    def xǁRegistrationFormǁclean__mutmut_16(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        email = cleaned_data.get("email")
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("XXpassword2XX")

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

    def xǁRegistrationFormǁclean__mutmut_17(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        email = cleaned_data.get("email")
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("PASSWORD2")

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

    def xǁRegistrationFormǁclean__mutmut_18(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        email = cleaned_data.get("email")
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 == password2:
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

    def xǁRegistrationFormǁclean__mutmut_19(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        email = cleaned_data.get("email")
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 != password2:
            raise ValidationError(None)

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

    def xǁRegistrationFormǁclean__mutmut_20(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        email = cleaned_data.get("email")
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 != password2:
            raise ValidationError("XXПаролі не співпадають.XX")

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

    def xǁRegistrationFormǁclean__mutmut_21(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        email = cleaned_data.get("email")
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 != password2:
            raise ValidationError("паролі не співпадають.")

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

    def xǁRegistrationFormǁclean__mutmut_22(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        email = cleaned_data.get("email")
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 != password2:
            raise ValidationError("ПАРОЛІ НЕ СПІВПАДАЮТЬ.")

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

    def xǁRegistrationFormǁclean__mutmut_23(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        email = cleaned_data.get("email")
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 != password2:
            raise ValidationError("Паролі не співпадають.")

        if User.objects.filter(username=None).exists():
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

    def xǁRegistrationFormǁclean__mutmut_24(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        email = cleaned_data.get("email")
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 != password2:
            raise ValidationError("Паролі не співпадають.")

        if User.objects.filter(username=username).exists():
            self.add_error(
                None,
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

    def xǁRegistrationFormǁclean__mutmut_25(self):
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
                None,
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

    def xǁRegistrationFormǁclean__mutmut_26(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        email = cleaned_data.get("email")
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 != password2:
            raise ValidationError("Паролі не співпадають.")

        if User.objects.filter(username=username).exists():
            self.add_error(
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

    def xǁRegistrationFormǁclean__mutmut_27(self):
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

    def xǁRegistrationFormǁclean__mutmut_28(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        email = cleaned_data.get("email")
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 != password2:
            raise ValidationError("Паролі не співпадають.")

        if User.objects.filter(username=username).exists():
            self.add_error(
                "XXusernameXX",
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

    def xǁRegistrationFormǁclean__mutmut_29(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        email = cleaned_data.get("email")
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 != password2:
            raise ValidationError("Паролі не співпадають.")

        if User.objects.filter(username=username).exists():
            self.add_error(
                "USERNAME",
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

    def xǁRegistrationFormǁclean__mutmut_30(self):
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
                "XXДаний нікнейм користувача вже існує! Придумайте інший нікнейм.XX",
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

    def xǁRegistrationFormǁclean__mutmut_31(self):
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
                "даний нікнейм користувача вже існує! придумайте інший нікнейм.",
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

    def xǁRegistrationFormǁclean__mutmut_32(self):
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
                "ДАНИЙ НІКНЕЙМ КОРИСТУВАЧА ВЖЕ ІСНУЄ! ПРИДУМАЙТЕ ІНШИЙ НІКНЕЙМ.",
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

    def xǁRegistrationFormǁclean__mutmut_33(self):
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

        if User.objects.filter(email=None).exists():
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

    def xǁRegistrationFormǁclean__mutmut_34(self):
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
                None,
                "На дану електронну пошту вже зареєстровано акаунт! Введіть іншу.",
            )

        if not set(username).issubset(set(ascii_letters + digits)):
            self.add_error(
                "username",
                "У полі нікнейм дозволені лише латинські літери та цифри.",
            )

        return cleaned_data

    def xǁRegistrationFormǁclean__mutmut_35(self):
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
                None,
            )

        if not set(username).issubset(set(ascii_letters + digits)):
            self.add_error(
                "username",
                "У полі нікнейм дозволені лише латинські літери та цифри.",
            )

        return cleaned_data

    def xǁRegistrationFormǁclean__mutmut_36(self):
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
                "На дану електронну пошту вже зареєстровано акаунт! Введіть іншу.",
            )

        if not set(username).issubset(set(ascii_letters + digits)):
            self.add_error(
                "username",
                "У полі нікнейм дозволені лише латинські літери та цифри.",
            )

        return cleaned_data

    def xǁRegistrationFormǁclean__mutmut_37(self):
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
            )

        if not set(username).issubset(set(ascii_letters + digits)):
            self.add_error(
                "username",
                "У полі нікнейм дозволені лише латинські літери та цифри.",
            )

        return cleaned_data

    def xǁRegistrationFormǁclean__mutmut_38(self):
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
                "XXemailXX",
                "На дану електронну пошту вже зареєстровано акаунт! Введіть іншу.",
            )

        if not set(username).issubset(set(ascii_letters + digits)):
            self.add_error(
                "username",
                "У полі нікнейм дозволені лише латинські літери та цифри.",
            )

        return cleaned_data

    def xǁRegistrationFormǁclean__mutmut_39(self):
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
                "EMAIL",
                "На дану електронну пошту вже зареєстровано акаунт! Введіть іншу.",
            )

        if not set(username).issubset(set(ascii_letters + digits)):
            self.add_error(
                "username",
                "У полі нікнейм дозволені лише латинські літери та цифри.",
            )

        return cleaned_data

    def xǁRegistrationFormǁclean__mutmut_40(self):
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
                "XXНа дану електронну пошту вже зареєстровано акаунт! Введіть іншу.XX",
            )

        if not set(username).issubset(set(ascii_letters + digits)):
            self.add_error(
                "username",
                "У полі нікнейм дозволені лише латинські літери та цифри.",
            )

        return cleaned_data

    def xǁRegistrationFormǁclean__mutmut_41(self):
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
                "на дану електронну пошту вже зареєстровано акаунт! введіть іншу.",
            )

        if not set(username).issubset(set(ascii_letters + digits)):
            self.add_error(
                "username",
                "У полі нікнейм дозволені лише латинські літери та цифри.",
            )

        return cleaned_data

    def xǁRegistrationFormǁclean__mutmut_42(self):
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
                "НА ДАНУ ЕЛЕКТРОННУ ПОШТУ ВЖЕ ЗАРЕЄСТРОВАНО АКАУНТ! ВВЕДІТЬ ІНШУ.",
            )

        if not set(username).issubset(set(ascii_letters + digits)):
            self.add_error(
                "username",
                "У полі нікнейм дозволені лише латинські літери та цифри.",
            )

        return cleaned_data

    def xǁRegistrationFormǁclean__mutmut_43(self):
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

        if set(username).issubset(set(ascii_letters + digits)):
            self.add_error(
                "username",
                "У полі нікнейм дозволені лише латинські літери та цифри.",
            )

        return cleaned_data

    def xǁRegistrationFormǁclean__mutmut_44(self):
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

        if not set(username).issubset(None):
            self.add_error(
                "username",
                "У полі нікнейм дозволені лише латинські літери та цифри.",
            )

        return cleaned_data

    def xǁRegistrationFormǁclean__mutmut_45(self):
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

        if not set(None).issubset(set(ascii_letters + digits)):
            self.add_error(
                "username",
                "У полі нікнейм дозволені лише латинські літери та цифри.",
            )

        return cleaned_data

    def xǁRegistrationFormǁclean__mutmut_46(self):
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

        if not set(username).issubset(set(None)):
            self.add_error(
                "username",
                "У полі нікнейм дозволені лише латинські літери та цифри.",
            )

        return cleaned_data

    def xǁRegistrationFormǁclean__mutmut_47(self):
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

        if not set(username).issubset(set(ascii_letters - digits)):
            self.add_error(
                "username",
                "У полі нікнейм дозволені лише латинські літери та цифри.",
            )

        return cleaned_data

    def xǁRegistrationFormǁclean__mutmut_48(self):
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
                None,
                "У полі нікнейм дозволені лише латинські літери та цифри.",
            )

        return cleaned_data

    def xǁRegistrationFormǁclean__mutmut_49(self):
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
                None,
            )

        return cleaned_data

    def xǁRegistrationFormǁclean__mutmut_50(self):
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
                "У полі нікнейм дозволені лише латинські літери та цифри.",
            )

        return cleaned_data

    def xǁRegistrationFormǁclean__mutmut_51(self):
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
            )

        return cleaned_data

    def xǁRegistrationFormǁclean__mutmut_52(self):
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
                "XXusernameXX",
                "У полі нікнейм дозволені лише латинські літери та цифри.",
            )

        return cleaned_data

    def xǁRegistrationFormǁclean__mutmut_53(self):
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
                "USERNAME",
                "У полі нікнейм дозволені лише латинські літери та цифри.",
            )

        return cleaned_data

    def xǁRegistrationFormǁclean__mutmut_54(self):
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
                "XXУ полі нікнейм дозволені лише латинські літери та цифри.XX",
            )

        return cleaned_data

    def xǁRegistrationFormǁclean__mutmut_55(self):
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
                "у полі нікнейм дозволені лише латинські літери та цифри.",
            )

        return cleaned_data

    def xǁRegistrationFormǁclean__mutmut_56(self):
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
                "У ПОЛІ НІКНЕЙМ ДОЗВОЛЕНІ ЛИШЕ ЛАТИНСЬКІ ЛІТЕРИ ТА ЦИФРИ.",
            )

        return cleaned_data

    xǁRegistrationFormǁclean__mutmut_mutants: ClassVar[MutantDict] = {
        "xǁRegistrationFormǁclean__mutmut_1": xǁRegistrationFormǁclean__mutmut_1,
        "xǁRegistrationFormǁclean__mutmut_2": xǁRegistrationFormǁclean__mutmut_2,
        "xǁRegistrationFormǁclean__mutmut_3": xǁRegistrationFormǁclean__mutmut_3,
        "xǁRegistrationFormǁclean__mutmut_4": xǁRegistrationFormǁclean__mutmut_4,
        "xǁRegistrationFormǁclean__mutmut_5": xǁRegistrationFormǁclean__mutmut_5,
        "xǁRegistrationFormǁclean__mutmut_6": xǁRegistrationFormǁclean__mutmut_6,
        "xǁRegistrationFormǁclean__mutmut_7": xǁRegistrationFormǁclean__mutmut_7,
        "xǁRegistrationFormǁclean__mutmut_8": xǁRegistrationFormǁclean__mutmut_8,
        "xǁRegistrationFormǁclean__mutmut_9": xǁRegistrationFormǁclean__mutmut_9,
        "xǁRegistrationFormǁclean__mutmut_10": xǁRegistrationFormǁclean__mutmut_10,
        "xǁRegistrationFormǁclean__mutmut_11": xǁRegistrationFormǁclean__mutmut_11,
        "xǁRegistrationFormǁclean__mutmut_12": xǁRegistrationFormǁclean__mutmut_12,
        "xǁRegistrationFormǁclean__mutmut_13": xǁRegistrationFormǁclean__mutmut_13,
        "xǁRegistrationFormǁclean__mutmut_14": xǁRegistrationFormǁclean__mutmut_14,
        "xǁRegistrationFormǁclean__mutmut_15": xǁRegistrationFormǁclean__mutmut_15,
        "xǁRegistrationFormǁclean__mutmut_16": xǁRegistrationFormǁclean__mutmut_16,
        "xǁRegistrationFormǁclean__mutmut_17": xǁRegistrationFormǁclean__mutmut_17,
        "xǁRegistrationFormǁclean__mutmut_18": xǁRegistrationFormǁclean__mutmut_18,
        "xǁRegistrationFormǁclean__mutmut_19": xǁRegistrationFormǁclean__mutmut_19,
        "xǁRegistrationFormǁclean__mutmut_20": xǁRegistrationFormǁclean__mutmut_20,
        "xǁRegistrationFormǁclean__mutmut_21": xǁRegistrationFormǁclean__mutmut_21,
        "xǁRegistrationFormǁclean__mutmut_22": xǁRegistrationFormǁclean__mutmut_22,
        "xǁRegistrationFormǁclean__mutmut_23": xǁRegistrationFormǁclean__mutmut_23,
        "xǁRegistrationFormǁclean__mutmut_24": xǁRegistrationFormǁclean__mutmut_24,
        "xǁRegistrationFormǁclean__mutmut_25": xǁRegistrationFormǁclean__mutmut_25,
        "xǁRegistrationFormǁclean__mutmut_26": xǁRegistrationFormǁclean__mutmut_26,
        "xǁRegistrationFormǁclean__mutmut_27": xǁRegistrationFormǁclean__mutmut_27,
        "xǁRegistrationFormǁclean__mutmut_28": xǁRegistrationFormǁclean__mutmut_28,
        "xǁRegistrationFormǁclean__mutmut_29": xǁRegistrationFormǁclean__mutmut_29,
        "xǁRegistrationFormǁclean__mutmut_30": xǁRegistrationFormǁclean__mutmut_30,
        "xǁRegistrationFormǁclean__mutmut_31": xǁRegistrationFormǁclean__mutmut_31,
        "xǁRegistrationFormǁclean__mutmut_32": xǁRegistrationFormǁclean__mutmut_32,
        "xǁRegistrationFormǁclean__mutmut_33": xǁRegistrationFormǁclean__mutmut_33,
        "xǁRegistrationFormǁclean__mutmut_34": xǁRegistrationFormǁclean__mutmut_34,
        "xǁRegistrationFormǁclean__mutmut_35": xǁRegistrationFormǁclean__mutmut_35,
        "xǁRegistrationFormǁclean__mutmut_36": xǁRegistrationFormǁclean__mutmut_36,
        "xǁRegistrationFormǁclean__mutmut_37": xǁRegistrationFormǁclean__mutmut_37,
        "xǁRegistrationFormǁclean__mutmut_38": xǁRegistrationFormǁclean__mutmut_38,
        "xǁRegistrationFormǁclean__mutmut_39": xǁRegistrationFormǁclean__mutmut_39,
        "xǁRegistrationFormǁclean__mutmut_40": xǁRegistrationFormǁclean__mutmut_40,
        "xǁRegistrationFormǁclean__mutmut_41": xǁRegistrationFormǁclean__mutmut_41,
        "xǁRegistrationFormǁclean__mutmut_42": xǁRegistrationFormǁclean__mutmut_42,
        "xǁRegistrationFormǁclean__mutmut_43": xǁRegistrationFormǁclean__mutmut_43,
        "xǁRegistrationFormǁclean__mutmut_44": xǁRegistrationFormǁclean__mutmut_44,
        "xǁRegistrationFormǁclean__mutmut_45": xǁRegistrationFormǁclean__mutmut_45,
        "xǁRegistrationFormǁclean__mutmut_46": xǁRegistrationFormǁclean__mutmut_46,
        "xǁRegistrationFormǁclean__mutmut_47": xǁRegistrationFormǁclean__mutmut_47,
        "xǁRegistrationFormǁclean__mutmut_48": xǁRegistrationFormǁclean__mutmut_48,
        "xǁRegistrationFormǁclean__mutmut_49": xǁRegistrationFormǁclean__mutmut_49,
        "xǁRegistrationFormǁclean__mutmut_50": xǁRegistrationFormǁclean__mutmut_50,
        "xǁRegistrationFormǁclean__mutmut_51": xǁRegistrationFormǁclean__mutmut_51,
        "xǁRegistrationFormǁclean__mutmut_52": xǁRegistrationFormǁclean__mutmut_52,
        "xǁRegistrationFormǁclean__mutmut_53": xǁRegistrationFormǁclean__mutmut_53,
        "xǁRegistrationFormǁclean__mutmut_54": xǁRegistrationFormǁclean__mutmut_54,
        "xǁRegistrationFormǁclean__mutmut_55": xǁRegistrationFormǁclean__mutmut_55,
        "xǁRegistrationFormǁclean__mutmut_56": xǁRegistrationFormǁclean__mutmut_56,
    }

    def clean(self, *args, **kwargs):
        result = _mutmut_trampoline(
            object.__getattribute__(self, "xǁRegistrationFormǁclean__mutmut_orig"),
            object.__getattribute__(self, "xǁRegistrationFormǁclean__mutmut_mutants"),
            args,
            kwargs,
            self,
        )
        return result

    clean.__signature__ = _mutmut_signature(xǁRegistrationFormǁclean__mutmut_orig)
    xǁRegistrationFormǁclean__mutmut_orig.__name__ = "xǁRegistrationFormǁclean"

    def xǁRegistrationFormǁsave__mutmut_orig(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

    def xǁRegistrationFormǁsave__mutmut_1(self, commit=False):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

    def xǁRegistrationFormǁsave__mutmut_2(self, commit=True):
        user = None
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

    def xǁRegistrationFormǁsave__mutmut_3(self, commit=True):
        user = super().save(commit=None)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

    def xǁRegistrationFormǁsave__mutmut_4(self, commit=True):
        user = super().save(commit=True)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

    def xǁRegistrationFormǁsave__mutmut_5(self, commit=True):
        user = super().save(commit=False)
        user.set_password(None)
        if commit:
            user.save()
        return user

    def xǁRegistrationFormǁsave__mutmut_6(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["XXpassword1XX"])
        if commit:
            user.save()
        return user

    def xǁRegistrationFormǁsave__mutmut_7(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["PASSWORD1"])
        if commit:
            user.save()
        return user

    xǁRegistrationFormǁsave__mutmut_mutants: ClassVar[MutantDict] = {
        "xǁRegistrationFormǁsave__mutmut_1": xǁRegistrationFormǁsave__mutmut_1,
        "xǁRegistrationFormǁsave__mutmut_2": xǁRegistrationFormǁsave__mutmut_2,
        "xǁRegistrationFormǁsave__mutmut_3": xǁRegistrationFormǁsave__mutmut_3,
        "xǁRegistrationFormǁsave__mutmut_4": xǁRegistrationFormǁsave__mutmut_4,
        "xǁRegistrationFormǁsave__mutmut_5": xǁRegistrationFormǁsave__mutmut_5,
        "xǁRegistrationFormǁsave__mutmut_6": xǁRegistrationFormǁsave__mutmut_6,
        "xǁRegistrationFormǁsave__mutmut_7": xǁRegistrationFormǁsave__mutmut_7,
    }

    def save(self, *args, **kwargs):
        result = _mutmut_trampoline(
            object.__getattribute__(self, "xǁRegistrationFormǁsave__mutmut_orig"),
            object.__getattribute__(self, "xǁRegistrationFormǁsave__mutmut_mutants"),
            args,
            kwargs,
            self,
        )
        return result

    save.__signature__ = _mutmut_signature(xǁRegistrationFormǁsave__mutmut_orig)
    xǁRegistrationFormǁsave__mutmut_orig.__name__ = "xǁRegistrationFormǁsave"


class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("first_name", "last_name", "email", "username", "bio", "image")

    def xǁProfileFormǁclean__mutmut_orig(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        email = cleaned_data.get("email")
        if User.objects.filter(email=email).exclude(id=self.instance.id).exists():
            self.add_error(
                "email",
                "На дану електронну пошту вже зареєстровано акаунт! Введіть іншу.",
            )

        if not set(username).issubset(set(ascii_letters + digits)):
            self.add_error(
                "username",
                "У полі нікнейм дозволені лише латинські літери та цифри.",
            )

    def xǁProfileFormǁclean__mutmut_1(self):
        cleaned_data = None
        username = cleaned_data.get("username")
        email = cleaned_data.get("email")
        if User.objects.filter(email=email).exclude(id=self.instance.id).exists():
            self.add_error(
                "email",
                "На дану електронну пошту вже зареєстровано акаунт! Введіть іншу.",
            )

        if not set(username).issubset(set(ascii_letters + digits)):
            self.add_error(
                "username",
                "У полі нікнейм дозволені лише латинські літери та цифри.",
            )

    def xǁProfileFormǁclean__mutmut_2(self):
        cleaned_data = super().clean()
        username = None
        email = cleaned_data.get("email")
        if User.objects.filter(email=email).exclude(id=self.instance.id).exists():
            self.add_error(
                "email",
                "На дану електронну пошту вже зареєстровано акаунт! Введіть іншу.",
            )

        if not set(username).issubset(set(ascii_letters + digits)):
            self.add_error(
                "username",
                "У полі нікнейм дозволені лише латинські літери та цифри.",
            )

    def xǁProfileFormǁclean__mutmut_3(self):
        cleaned_data = super().clean()
        username = cleaned_data.get(None)
        email = cleaned_data.get("email")
        if User.objects.filter(email=email).exclude(id=self.instance.id).exists():
            self.add_error(
                "email",
                "На дану електронну пошту вже зареєстровано акаунт! Введіть іншу.",
            )

        if not set(username).issubset(set(ascii_letters + digits)):
            self.add_error(
                "username",
                "У полі нікнейм дозволені лише латинські літери та цифри.",
            )

    def xǁProfileFormǁclean__mutmut_4(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("XXusernameXX")
        email = cleaned_data.get("email")
        if User.objects.filter(email=email).exclude(id=self.instance.id).exists():
            self.add_error(
                "email",
                "На дану електронну пошту вже зареєстровано акаунт! Введіть іншу.",
            )

        if not set(username).issubset(set(ascii_letters + digits)):
            self.add_error(
                "username",
                "У полі нікнейм дозволені лише латинські літери та цифри.",
            )

    def xǁProfileFormǁclean__mutmut_5(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("USERNAME")
        email = cleaned_data.get("email")
        if User.objects.filter(email=email).exclude(id=self.instance.id).exists():
            self.add_error(
                "email",
                "На дану електронну пошту вже зареєстровано акаунт! Введіть іншу.",
            )

        if not set(username).issubset(set(ascii_letters + digits)):
            self.add_error(
                "username",
                "У полі нікнейм дозволені лише латинські літери та цифри.",
            )

    def xǁProfileFormǁclean__mutmut_6(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        email = None
        if User.objects.filter(email=email).exclude(id=self.instance.id).exists():
            self.add_error(
                "email",
                "На дану електронну пошту вже зареєстровано акаунт! Введіть іншу.",
            )

        if not set(username).issubset(set(ascii_letters + digits)):
            self.add_error(
                "username",
                "У полі нікнейм дозволені лише латинські літери та цифри.",
            )

    def xǁProfileFormǁclean__mutmut_7(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        email = cleaned_data.get(None)
        if User.objects.filter(email=email).exclude(id=self.instance.id).exists():
            self.add_error(
                "email",
                "На дану електронну пошту вже зареєстровано акаунт! Введіть іншу.",
            )

        if not set(username).issubset(set(ascii_letters + digits)):
            self.add_error(
                "username",
                "У полі нікнейм дозволені лише латинські літери та цифри.",
            )

    def xǁProfileFormǁclean__mutmut_8(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        email = cleaned_data.get("XXemailXX")
        if User.objects.filter(email=email).exclude(id=self.instance.id).exists():
            self.add_error(
                "email",
                "На дану електронну пошту вже зареєстровано акаунт! Введіть іншу.",
            )

        if not set(username).issubset(set(ascii_letters + digits)):
            self.add_error(
                "username",
                "У полі нікнейм дозволені лише латинські літери та цифри.",
            )

    def xǁProfileFormǁclean__mutmut_9(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        email = cleaned_data.get("EMAIL")
        if User.objects.filter(email=email).exclude(id=self.instance.id).exists():
            self.add_error(
                "email",
                "На дану електронну пошту вже зареєстровано акаунт! Введіть іншу.",
            )

        if not set(username).issubset(set(ascii_letters + digits)):
            self.add_error(
                "username",
                "У полі нікнейм дозволені лише латинські літери та цифри.",
            )

    def xǁProfileFormǁclean__mutmut_10(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        email = cleaned_data.get("email")
        if User.objects.filter(email=email).exclude(id=None).exists():
            self.add_error(
                "email",
                "На дану електронну пошту вже зареєстровано акаунт! Введіть іншу.",
            )

        if not set(username).issubset(set(ascii_letters + digits)):
            self.add_error(
                "username",
                "У полі нікнейм дозволені лише латинські літери та цифри.",
            )

    def xǁProfileFormǁclean__mutmut_11(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        email = cleaned_data.get("email")
        if User.objects.filter(email=None).exclude(id=self.instance.id).exists():
            self.add_error(
                "email",
                "На дану електронну пошту вже зареєстровано акаунт! Введіть іншу.",
            )

        if not set(username).issubset(set(ascii_letters + digits)):
            self.add_error(
                "username",
                "У полі нікнейм дозволені лише латинські літери та цифри.",
            )

    def xǁProfileFormǁclean__mutmut_12(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        email = cleaned_data.get("email")
        if User.objects.filter(email=email).exclude(id=self.instance.id).exists():
            self.add_error(
                None,
                "На дану електронну пошту вже зареєстровано акаунт! Введіть іншу.",
            )

        if not set(username).issubset(set(ascii_letters + digits)):
            self.add_error(
                "username",
                "У полі нікнейм дозволені лише латинські літери та цифри.",
            )

    def xǁProfileFormǁclean__mutmut_13(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        email = cleaned_data.get("email")
        if User.objects.filter(email=email).exclude(id=self.instance.id).exists():
            self.add_error(
                "email",
                None,
            )

        if not set(username).issubset(set(ascii_letters + digits)):
            self.add_error(
                "username",
                "У полі нікнейм дозволені лише латинські літери та цифри.",
            )

    def xǁProfileFormǁclean__mutmut_14(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        email = cleaned_data.get("email")
        if User.objects.filter(email=email).exclude(id=self.instance.id).exists():
            self.add_error(
                "На дану електронну пошту вже зареєстровано акаунт! Введіть іншу.",
            )

        if not set(username).issubset(set(ascii_letters + digits)):
            self.add_error(
                "username",
                "У полі нікнейм дозволені лише латинські літери та цифри.",
            )

    def xǁProfileFormǁclean__mutmut_15(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        email = cleaned_data.get("email")
        if User.objects.filter(email=email).exclude(id=self.instance.id).exists():
            self.add_error(
                "email",
            )

        if not set(username).issubset(set(ascii_letters + digits)):
            self.add_error(
                "username",
                "У полі нікнейм дозволені лише латинські літери та цифри.",
            )

    def xǁProfileFormǁclean__mutmut_16(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        email = cleaned_data.get("email")
        if User.objects.filter(email=email).exclude(id=self.instance.id).exists():
            self.add_error(
                "XXemailXX",
                "На дану електронну пошту вже зареєстровано акаунт! Введіть іншу.",
            )

        if not set(username).issubset(set(ascii_letters + digits)):
            self.add_error(
                "username",
                "У полі нікнейм дозволені лише латинські літери та цифри.",
            )

    def xǁProfileFormǁclean__mutmut_17(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        email = cleaned_data.get("email")
        if User.objects.filter(email=email).exclude(id=self.instance.id).exists():
            self.add_error(
                "EMAIL",
                "На дану електронну пошту вже зареєстровано акаунт! Введіть іншу.",
            )

        if not set(username).issubset(set(ascii_letters + digits)):
            self.add_error(
                "username",
                "У полі нікнейм дозволені лише латинські літери та цифри.",
            )

    def xǁProfileFormǁclean__mutmut_18(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        email = cleaned_data.get("email")
        if User.objects.filter(email=email).exclude(id=self.instance.id).exists():
            self.add_error(
                "email",
                "XXНа дану електронну пошту вже зареєстровано акаунт! Введіть іншу.XX",
            )

        if not set(username).issubset(set(ascii_letters + digits)):
            self.add_error(
                "username",
                "У полі нікнейм дозволені лише латинські літери та цифри.",
            )

    def xǁProfileFormǁclean__mutmut_19(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        email = cleaned_data.get("email")
        if User.objects.filter(email=email).exclude(id=self.instance.id).exists():
            self.add_error(
                "email",
                "на дану електронну пошту вже зареєстровано акаунт! введіть іншу.",
            )

        if not set(username).issubset(set(ascii_letters + digits)):
            self.add_error(
                "username",
                "У полі нікнейм дозволені лише латинські літери та цифри.",
            )

    def xǁProfileFormǁclean__mutmut_20(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        email = cleaned_data.get("email")
        if User.objects.filter(email=email).exclude(id=self.instance.id).exists():
            self.add_error(
                "email",
                "НА ДАНУ ЕЛЕКТРОННУ ПОШТУ ВЖЕ ЗАРЕЄСТРОВАНО АКАУНТ! ВВЕДІТЬ ІНШУ.",
            )

        if not set(username).issubset(set(ascii_letters + digits)):
            self.add_error(
                "username",
                "У полі нікнейм дозволені лише латинські літери та цифри.",
            )

    def xǁProfileFormǁclean__mutmut_21(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        email = cleaned_data.get("email")
        if User.objects.filter(email=email).exclude(id=self.instance.id).exists():
            self.add_error(
                "email",
                "На дану електронну пошту вже зареєстровано акаунт! Введіть іншу.",
            )

        if set(username).issubset(set(ascii_letters + digits)):
            self.add_error(
                "username",
                "У полі нікнейм дозволені лише латинські літери та цифри.",
            )

    def xǁProfileFormǁclean__mutmut_22(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        email = cleaned_data.get("email")
        if User.objects.filter(email=email).exclude(id=self.instance.id).exists():
            self.add_error(
                "email",
                "На дану електронну пошту вже зареєстровано акаунт! Введіть іншу.",
            )

        if not set(username).issubset(None):
            self.add_error(
                "username",
                "У полі нікнейм дозволені лише латинські літери та цифри.",
            )

    def xǁProfileFormǁclean__mutmut_23(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        email = cleaned_data.get("email")
        if User.objects.filter(email=email).exclude(id=self.instance.id).exists():
            self.add_error(
                "email",
                "На дану електронну пошту вже зареєстровано акаунт! Введіть іншу.",
            )

        if not set(None).issubset(set(ascii_letters + digits)):
            self.add_error(
                "username",
                "У полі нікнейм дозволені лише латинські літери та цифри.",
            )

    def xǁProfileFormǁclean__mutmut_24(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        email = cleaned_data.get("email")
        if User.objects.filter(email=email).exclude(id=self.instance.id).exists():
            self.add_error(
                "email",
                "На дану електронну пошту вже зареєстровано акаунт! Введіть іншу.",
            )

        if not set(username).issubset(set(None)):
            self.add_error(
                "username",
                "У полі нікнейм дозволені лише латинські літери та цифри.",
            )

    def xǁProfileFormǁclean__mutmut_25(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        email = cleaned_data.get("email")
        if User.objects.filter(email=email).exclude(id=self.instance.id).exists():
            self.add_error(
                "email",
                "На дану електронну пошту вже зареєстровано акаунт! Введіть іншу.",
            )

        if not set(username).issubset(set(ascii_letters - digits)):
            self.add_error(
                "username",
                "У полі нікнейм дозволені лише латинські літери та цифри.",
            )

    def xǁProfileFormǁclean__mutmut_26(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        email = cleaned_data.get("email")
        if User.objects.filter(email=email).exclude(id=self.instance.id).exists():
            self.add_error(
                "email",
                "На дану електронну пошту вже зареєстровано акаунт! Введіть іншу.",
            )

        if not set(username).issubset(set(ascii_letters + digits)):
            self.add_error(
                None,
                "У полі нікнейм дозволені лише латинські літери та цифри.",
            )

    def xǁProfileFormǁclean__mutmut_27(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        email = cleaned_data.get("email")
        if User.objects.filter(email=email).exclude(id=self.instance.id).exists():
            self.add_error(
                "email",
                "На дану електронну пошту вже зареєстровано акаунт! Введіть іншу.",
            )

        if not set(username).issubset(set(ascii_letters + digits)):
            self.add_error(
                "username",
                None,
            )

    def xǁProfileFormǁclean__mutmut_28(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        email = cleaned_data.get("email")
        if User.objects.filter(email=email).exclude(id=self.instance.id).exists():
            self.add_error(
                "email",
                "На дану електронну пошту вже зареєстровано акаунт! Введіть іншу.",
            )

        if not set(username).issubset(set(ascii_letters + digits)):
            self.add_error(
                "У полі нікнейм дозволені лише латинські літери та цифри.",
            )

    def xǁProfileFormǁclean__mutmut_29(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        email = cleaned_data.get("email")
        if User.objects.filter(email=email).exclude(id=self.instance.id).exists():
            self.add_error(
                "email",
                "На дану електронну пошту вже зареєстровано акаунт! Введіть іншу.",
            )

        if not set(username).issubset(set(ascii_letters + digits)):
            self.add_error(
                "username",
            )

    def xǁProfileFormǁclean__mutmut_30(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        email = cleaned_data.get("email")
        if User.objects.filter(email=email).exclude(id=self.instance.id).exists():
            self.add_error(
                "email",
                "На дану електронну пошту вже зареєстровано акаунт! Введіть іншу.",
            )

        if not set(username).issubset(set(ascii_letters + digits)):
            self.add_error(
                "XXusernameXX",
                "У полі нікнейм дозволені лише латинські літери та цифри.",
            )

    def xǁProfileFormǁclean__mutmut_31(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        email = cleaned_data.get("email")
        if User.objects.filter(email=email).exclude(id=self.instance.id).exists():
            self.add_error(
                "email",
                "На дану електронну пошту вже зареєстровано акаунт! Введіть іншу.",
            )

        if not set(username).issubset(set(ascii_letters + digits)):
            self.add_error(
                "USERNAME",
                "У полі нікнейм дозволені лише латинські літери та цифри.",
            )

    def xǁProfileFormǁclean__mutmut_32(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        email = cleaned_data.get("email")
        if User.objects.filter(email=email).exclude(id=self.instance.id).exists():
            self.add_error(
                "email",
                "На дану електронну пошту вже зареєстровано акаунт! Введіть іншу.",
            )

        if not set(username).issubset(set(ascii_letters + digits)):
            self.add_error(
                "username",
                "XXУ полі нікнейм дозволені лише латинські літери та цифри.XX",
            )

    def xǁProfileFormǁclean__mutmut_33(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        email = cleaned_data.get("email")
        if User.objects.filter(email=email).exclude(id=self.instance.id).exists():
            self.add_error(
                "email",
                "На дану електронну пошту вже зареєстровано акаунт! Введіть іншу.",
            )

        if not set(username).issubset(set(ascii_letters + digits)):
            self.add_error(
                "username",
                "у полі нікнейм дозволені лише латинські літери та цифри.",
            )

    def xǁProfileFormǁclean__mutmut_34(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        email = cleaned_data.get("email")
        if User.objects.filter(email=email).exclude(id=self.instance.id).exists():
            self.add_error(
                "email",
                "На дану електронну пошту вже зареєстровано акаунт! Введіть іншу.",
            )

        if not set(username).issubset(set(ascii_letters + digits)):
            self.add_error(
                "username",
                "У ПОЛІ НІКНЕЙМ ДОЗВОЛЕНІ ЛИШЕ ЛАТИНСЬКІ ЛІТЕРИ ТА ЦИФРИ.",
            )

    xǁProfileFormǁclean__mutmut_mutants: ClassVar[MutantDict] = {
        "xǁProfileFormǁclean__mutmut_1": xǁProfileFormǁclean__mutmut_1,
        "xǁProfileFormǁclean__mutmut_2": xǁProfileFormǁclean__mutmut_2,
        "xǁProfileFormǁclean__mutmut_3": xǁProfileFormǁclean__mutmut_3,
        "xǁProfileFormǁclean__mutmut_4": xǁProfileFormǁclean__mutmut_4,
        "xǁProfileFormǁclean__mutmut_5": xǁProfileFormǁclean__mutmut_5,
        "xǁProfileFormǁclean__mutmut_6": xǁProfileFormǁclean__mutmut_6,
        "xǁProfileFormǁclean__mutmut_7": xǁProfileFormǁclean__mutmut_7,
        "xǁProfileFormǁclean__mutmut_8": xǁProfileFormǁclean__mutmut_8,
        "xǁProfileFormǁclean__mutmut_9": xǁProfileFormǁclean__mutmut_9,
        "xǁProfileFormǁclean__mutmut_10": xǁProfileFormǁclean__mutmut_10,
        "xǁProfileFormǁclean__mutmut_11": xǁProfileFormǁclean__mutmut_11,
        "xǁProfileFormǁclean__mutmut_12": xǁProfileFormǁclean__mutmut_12,
        "xǁProfileFormǁclean__mutmut_13": xǁProfileFormǁclean__mutmut_13,
        "xǁProfileFormǁclean__mutmut_14": xǁProfileFormǁclean__mutmut_14,
        "xǁProfileFormǁclean__mutmut_15": xǁProfileFormǁclean__mutmut_15,
        "xǁProfileFormǁclean__mutmut_16": xǁProfileFormǁclean__mutmut_16,
        "xǁProfileFormǁclean__mutmut_17": xǁProfileFormǁclean__mutmut_17,
        "xǁProfileFormǁclean__mutmut_18": xǁProfileFormǁclean__mutmut_18,
        "xǁProfileFormǁclean__mutmut_19": xǁProfileFormǁclean__mutmut_19,
        "xǁProfileFormǁclean__mutmut_20": xǁProfileFormǁclean__mutmut_20,
        "xǁProfileFormǁclean__mutmut_21": xǁProfileFormǁclean__mutmut_21,
        "xǁProfileFormǁclean__mutmut_22": xǁProfileFormǁclean__mutmut_22,
        "xǁProfileFormǁclean__mutmut_23": xǁProfileFormǁclean__mutmut_23,
        "xǁProfileFormǁclean__mutmut_24": xǁProfileFormǁclean__mutmut_24,
        "xǁProfileFormǁclean__mutmut_25": xǁProfileFormǁclean__mutmut_25,
        "xǁProfileFormǁclean__mutmut_26": xǁProfileFormǁclean__mutmut_26,
        "xǁProfileFormǁclean__mutmut_27": xǁProfileFormǁclean__mutmut_27,
        "xǁProfileFormǁclean__mutmut_28": xǁProfileFormǁclean__mutmut_28,
        "xǁProfileFormǁclean__mutmut_29": xǁProfileFormǁclean__mutmut_29,
        "xǁProfileFormǁclean__mutmut_30": xǁProfileFormǁclean__mutmut_30,
        "xǁProfileFormǁclean__mutmut_31": xǁProfileFormǁclean__mutmut_31,
        "xǁProfileFormǁclean__mutmut_32": xǁProfileFormǁclean__mutmut_32,
        "xǁProfileFormǁclean__mutmut_33": xǁProfileFormǁclean__mutmut_33,
        "xǁProfileFormǁclean__mutmut_34": xǁProfileFormǁclean__mutmut_34,
    }

    def clean(self, *args, **kwargs):
        result = _mutmut_trampoline(
            object.__getattribute__(self, "xǁProfileFormǁclean__mutmut_orig"),
            object.__getattribute__(self, "xǁProfileFormǁclean__mutmut_mutants"),
            args,
            kwargs,
            self,
        )
        return result

    clean.__signature__ = _mutmut_signature(xǁProfileFormǁclean__mutmut_orig)
    xǁProfileFormǁclean__mutmut_orig.__name__ = "xǁProfileFormǁclean"
