# coding: utf-8

from django import forms
from django.contrib.auth.models import User


class RegistrationForm(forms.Form):
    name = forms.CharField(max_length=50)
    username = forms.EmailField()
    password = forms.CharField(max_length=30)
    mood = forms.IntegerField()

    def save(self):
        u = User()
        u.username = self.cleaned_data['name']
        u.email = self.cleaned_data['username']
        u.set_password(self.cleaned_data['password'])
        u.is_active = True
        try:
            test = User.objects.get(email=self.cleaned_data['username'])
        except:
            u.save()
