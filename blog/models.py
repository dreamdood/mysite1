from django.db import models
from django.utils import timezone

from django.db import models

# Create your models here.

class user(models.Model):
    display_name = models.CharField(max_length=64)
    name = models.CharField(max_length=64)
    email = models.CharField(max_length=64)
    created = models.DateTimeField(auto_now_add=True)
    updated = model.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)


    def __str__(self):
        return "%s (%s)" % (self.name, self.email)