from django.shortcuts import render
from home.models import Post, ExchangeRate


# Create your views here.
def index(request):
    posts = Post.objects.filter(status=1).order_by('-creation_date')
    return render(request, 'home/index.html', {'posts': posts})


def table_detail(request):
    exchengerates = ExchangeRate
    return render(request, 'home/exchangerate_detail.html', {'exchangerates': exchengerates})
