from django.forms import BaseModelForm
from django.shortcuts import render, HttpResponse
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView 
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


def home(request):
    context = {
        # 'posts' : posters
        'posts' : Post.objects.all()
    }
    return render(request,'home.html', context)
    
    

class PostListView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    model = Post



    
    
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.instance.author = self.request.user
        return super().form_valid(form)


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