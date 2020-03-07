from django.shortcuts import render
from django.views.generic import (
     ListView, 
     CreateView,
     DetailView,
     UpdateView,
     DeleteView
)

from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post
# Create your views here.

#  naming convenvtion:
#  <app>/<model>_<viewtype>.html  

class PostListView(LoginRequiredMixin, ListView):
    ''' home page - lists all the current posts '''
    model = Post
    # template_name ='post/list.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostCreateView(LoginRequiredMixin, CreateView):
    ''' create a post with a title and description, author is automatically the person logged in '''
    model = Post
    fields = ['title', 'description']
    # success_url = ('post-list-page')

    def form_valid(self, form):
        form.instance.author = self.request.user  # set author to current logged in user
        return super().form_valid(form)

class PostDetailView(LoginRequiredMixin, DetailView):
    ''' posts description of product '''
    model = Post

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView,):
    ''' form to update the post, ensures the person updating the post is logged in to the correct user '''
    model = Post
    fields = ['title', 'description']
    # success_url = ('post-list-page')

    def form_valid(self, form):
        form.instance.author = self.request.user  # set author to current logged in user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(DeleteView, LoginRequiredMixin, UserPassesTestMixin):
    ''' Deletes the post if you are the poster '''
    model = Post
    success_url = ('/post')

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

    


    # def get(self, request, slug):
    #     ''' Renders specific post via slug.'''
    #     post = self.get_queryset().get(slug__iexact=slug)
    #     return render(request, 'post/detail.html', {
    #         'post':post , 'title':'About'
    #     })

    

def about(request):
    return render(request, 'post/about.html', {'title':'About'})
    


