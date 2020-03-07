from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from rest_framework.generics import ListCreateAPIView, RetrieveDestroyAPIView
from post.models import Post
from api.serializers import PostSerializer

class PostList(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetail(APIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer