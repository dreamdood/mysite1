from django.db import models

# Create your models here.

class Comment(models.Model):
    post = models.ForeignKey(Post, null = True, on_delete = 'models.CASCADE', 
                             related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = model.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.user