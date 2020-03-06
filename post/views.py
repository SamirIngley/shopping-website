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

#  naming convenvtion:
#  <app>/<model>_<viewtype>.html 
#  

class PostListView(ListView):
    model = Post
    # template_name ='post/list.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'description']

    def form_valid(self, form):
        form.instance.author = self.request.user  # set author to current logged in user
        return super().form_valid(form)


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
    


