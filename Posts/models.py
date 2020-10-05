from django.db import models

# Create your models here.

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, null=False, blank=True)
    body = models.TextField(null=False, blank=True)
    image = models.ImageField
    likes = models.PositiveIntegerField(null=False, default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = model.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)


    def __str__(self):
        return self.title