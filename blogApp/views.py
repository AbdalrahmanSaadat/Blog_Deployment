from typing import Any
from django.db.models.query import QuerySet
from django.forms import BaseModelForm
from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Post
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView, 
)
# Create your views here.


# posters = [
#     {
#         'author' : 'CoreyMS',
#         'title' : 'Blog Post 1',
#         'content' : 'First post conten',
#         'date_posted': 'August 27, 2018'
#     },
#     {
#         'author' : 'Jane doe',
#         'title' : 'Blog Post 2',
#         'content' : 'second post conten',
#         'date_posted': 'August 28, 2018'
#     } 
# ]


# def home(request):
#     context = {
#         # 'posts' : posters
#         'posts' : Post.objects.all()
#     }
#     return render(request,'home.html', context)
    
    

class PostListView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5
    
    
class UserPostListView(ListView):
    model = Post
    template_name = 'blogApp/user_posts.html'
    context_object_name = 'posts'
    # ordering = ['-date_posted']
    paginate_by = 5
    title = 'Posts'
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        
        context =  super().get_context_data(**kwargs)
        context['title']= self.title
        return context
    
    def get_queryset(self) -> QuerySet[Any]:
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
    model = Post

    title = 'Post'
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        
        context =  super().get_context_data(**kwargs)
        context['title']= self.title
        return context


    
    
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    title = 'New Post'
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        
        context =  super().get_context_data(**kwargs)
        context['title']= self.title
        return context


class PostUpdateView(UserPassesTestMixin,LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self) -> bool | None:
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(UserPassesTestMixin,LoginRequiredMixin, DeleteView):
    model = Post
    success_url = '/'
    
    def test_func(self) -> bool | None:
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    


def about(request):
    return render(request, 'about.html',{'title': 'About'})