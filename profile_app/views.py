from django.shortcuts import render
from django.conf import settings

import json

# Create your views here.

def index(request):
    context = {}
    bio(request, context)
    return render(request, 'profile_app/index.html', context)

def bio(request, context):
    with open( settings.MEDIA_ROOT + '/profile_app/bio.txt', 'r') as f:
        data = f.read()
    context.update({'bio': data})
    return context


