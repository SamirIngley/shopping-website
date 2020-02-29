from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic import CreateView
from django.views.generic.detail import DetailView

from django.http import HttpResponseRedirect
from django.urls import reverse_lazy

from post.models import Post
# Create your views here.

class PostListView(ListView):
    model = Post
    def get(self, request):
        ''' Get a list of posts.'''
        posts = self.get_queryset().all()
        return render(request, 'list.html', {'posts':posts})

class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'image', 'description', 'price']
    template_name = 'new.html'

class PostDetailView(DetailView):
    model = Post
    def get(self, request, slug):
        ''' Renders specific post via slug.'''
        post = self.get_queryset().get(slug__iexact=slug)
        return render(request, 'post.html', {
            'post':post
        })