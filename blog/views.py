from django.shortcuts import render
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context )


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html' # <app>/<model>_<viewytpe>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView): # author needed to create a post in createview
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form) 
        # this statement runs self in the class but when we change some default values it needs to be run by us
        # need to redirect now but good news is post is created

# mixin needs to be in the left of the updated view
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView): # it will use the same view as create view
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user # same as if below but diff function type so needs to be seprated
        return super().form_valid(form) 

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if post.author == self.request.user:
            return True
        return False


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})