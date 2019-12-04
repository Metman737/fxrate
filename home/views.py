from django.shortcuts import render
from django.views.generic import DetailView

from home.models import Post, ExchangeRate


# Create your views here.
def index(request):
    posts = Post.objects.filter(status=1).order_by('-creation_date')
    return render(request, 'home/index.html', {'posts': posts})


def table_detail(request):
    exchengerates = ExchangeRate.objects.all()
    return render(request, 'home/exchangerate_detail.html', {'exchangerates': exchengerates})


class PostAsDatail(DetailView):
    model = Post
