from django.shortcuts import render
from home.models import Post


# Create your views here.
def index(request):
    posts = Post.objects.filter(status=1).order_by('-creation_date')
    return render(request, 'home/index.html', {'posts': posts})
