from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

from .models import *

class hostsForm(forms.ModelForm):
    class Meta:
        model = list_of_hosts
        fields = ['first_name', 'last_name', 'address', 'phone']

class hostsDelete(forms.Form):
    id = forms.IntegerField(label='ID записи для удаления')
class hostsUpdate(forms.Form):
    id = forms.IntegerField()
    first_name = forms.CharField(max_length=20, required=False)
    last_name = forms.CharField(max_length=30, required=False)
    address = forms.CharField(max_length=50, required=False)
    phone = forms.CharField(max_length=13, required=False)


class animalsForm(forms.ModelForm):
    class Meta:
        model = list_of_animals
        fields = ['name', 'kind_of_animal', 'breed', 'age', 'host']
class animalsDelete(forms.Form):
    id = forms.IntegerField(label='ID записи для удаления')
class animalsUpdate(forms.Form):
        id = forms.IntegerField()
        name = forms.CharField(max_length=20, required=False)
        kind_of_animal = forms.CharField(max_length=30, required=False)
        breed = forms.CharField(max_length=20, required=False)
        age = forms.IntegerField(required=False)
        host = forms.IntegerField(required=False)

class diseasesForm(forms.ModelForm):
    class Meta:
        model = diseases
        fields = ['name']
class diseasesDelete(forms.Form):
    id = forms.IntegerField(label='ID записи для удаления')
class diseasesUpdate(forms.Form):
    id = forms.IntegerField()
    name = forms.CharField(max_length=255)


class RegistrationForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class':'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    first_name = forms.CharField(label='Имя',validators=[RegexValidator(r'^[А-ЯЁ][а-яё]*$')], widget=forms.TextInput(attrs={'class': 'form-input'}))
    last_name = forms.CharField(label='Фамилие', validators=[RegexValidator(r'^[А-ЯЁ][а-яё]*$')], widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='Почта', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'first_name', 'last_name', 'email']

class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))