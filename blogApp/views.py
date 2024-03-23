from django.shortcuts import render, HttpResponse
from .models import Post
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
    
    
def about(request):
    return render(request, 'about.html',{'title': 'About'})