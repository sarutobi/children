# coding: utf-8

from django.shortcuts import redirect, render_to_response
from django.template import RequestContext

from .forms import RegistrationForm


def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
        request.session['mood'] = form.cleaned_data['mood']
    return redirect('/anketa')


def anketa(request):
    return render_to_response(
        'anketa.html',
        context_instance=RequestContext(request))
