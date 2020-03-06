from django.shortcuts import render
from django.views.generic import (
     ListView, 
     CreateView,
     DetailView 
)

from django.http import HttpResponseRedirect
from django.urls import reverse_lazy

from .models import Post
# Create your views here.

class PostListView(ListView):
    model = Post
    template_name ='post/list.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
 
    # def get(self, request):
    #     ''' Get a list of posts.'''
    #     posts = self.get_queryset().all()
    #     return render(request, 'post/list.html', {'posts':posts})

class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'description']

class PostDetailView(DetailView):
    model = Post

    # def get(self, request, slug):
    #     ''' Renders specific post via slug.'''
    #     post = self.get_queryset().get(slug__iexact=slug)
    #     return render(request, 'post/detail.html', {
    #         'post':post , 'title':'About'
    #     })

    

def about(request):
    return render(request, 'post/about.html', {'title':'About'})
    


