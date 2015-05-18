from django.db import models
from django.contrib.auth.models import User
import datetime

class Hobby(models.Model):
    name = models.CharField(max_length=128)

class UserProfile(models.Model):
    user = models.OneToOneField(User)

    # The additional attributes will include.
    birthdate = models.DateField(blank=True)

    HAIR_COLOR_CHOICES = (
        ('BLACK', 'Black'),
        ('BROWN', 'Brown'),
        ('RED', 'Red'),
        ('BLONDE', 'Blonde'),
        ('SALTNPEPPER', 'Salt N Peppa'),
        ('GREEN', 'Green'),
    )

    hair_color = models.CharField(max_length=128,
                                      choices=HAIR_COLOR_CHOICES,
                                      blank=True)

    favorite_hobby = models.OneToOneField(Hobby)

    created = models.DateTimeField(default=datetime.datetime.now)

    def __unicode__(self):
        return self.user.username