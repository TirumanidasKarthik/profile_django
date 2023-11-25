from django.db import models

# Create your models here.

class PersonalInfo(models.Model):
    name = models.CharField(max_length=200)
    role = models.CharField(max_length=200)
    github = models.URLField()
    linkdin = models.URLField()
    gmail = models.EmailField()
    photo = models.ImageField()
