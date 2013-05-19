# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.template import RequestContext

from .models import Interest, GroupOfInterest


def index(request):
    return render_to_response(
        'loginform.html',
        context_instance=RequestContext(request))


def interests(request, type=None):
    groups = GroupOfInterest.objects.all()
    interests = Interest.objects.all()
    if type:
        interests = interests.filter(root=type)
    return render_to_response('interest.html',
        { 'groups': groups,
          'interests': interests,
        },
        context_instance=RequestContext(request)
    )
