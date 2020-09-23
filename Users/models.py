from django.db import models

# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    username = models.CharField(max_length=70)
    email = models.EmailField()
    birthday = models.DateField()
    created = models.DateTimeField(auto_now_add=True)
    updated = model.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)


    def __str__(self):
        return self.first_name + " " + self.last_name