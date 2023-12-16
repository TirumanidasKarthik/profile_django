from django.shortcuts import render
from django.conf import settings

import json

# Create your views here.

def index(request):
    context = {}
    load_bio(request, context)
    load_skills(request, context)
    load_experience(request, context)
    load_education(request, context)
    load_certification(request, context)
    load_achievement(request, context)
    return render(request, 'profile_app/index.html', context)

def load_bio(request, context):
    with open( settings.MEDIA_ROOT + '/profile_app/bio.txt', 'r') as f:
        data = f.read()
    context.update({'bio': data})
    return

def load_skills(request, context):
    with open(settings.MEDIA_ROOT + '/profile_app/skills.json') as fp:
        skills = json.load(fp)
    context.update({'skills': skills})
    return

def load_experience(request, context):
    with open(settings.MEDIA_ROOT + '/profile_app/experience.json') as fp:
        experience = json.load(fp)
    context.update({'experience': experience})
    return

def load_education(request, context):
    with open(settings.MEDIA_ROOT + '/profile_app/education.json') as fp:
        education = json.load(fp)
    context.update({'education': education})
    return

def load_certification(request, context):
    with open(settings.MEDIA_ROOT + '/profile_app/certification.json') as fp:
        certification = json.load(fp)
    context.update({'certification': certification})
    return

def load_achievement(request, context):
    with open(settings.MEDIA_ROOT + '/profile_app/achievement.json') as fp:
        achievement = json.load(fp)
    context.update({'achievement': achievement})
    return



