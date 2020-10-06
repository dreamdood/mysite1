#from rest_framework import viewsets, permissions
#from .models import Blog
#from .serializers import PostSerializer

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the blog index.")

"""
NOTE:
we just use "views" to mean the same thing as controllers in rails
views offer the API methods
"""
#class PostViewSet(viewsets.ModelViewSet):
    # TODO: require authentication here
    # permission_classes = [
    #     permissions.IsAuthenticated,
    # ]
    #serializer_class = PostSerializer
    #queryset = Post.objects.all()