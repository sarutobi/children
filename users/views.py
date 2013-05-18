# coding: utf-8

from django.shortcuts import redirect

from .forms import RegistrationForm


def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
        request.session['mood'] = form.cleaned_data['mood']
    return redirect('/')
