from django.shortcuts import render
from django.views.generic import DetailView, ListView

from home.models import Post, ExchangeRate


class ExchangeRateTable(ListView):
    queryset = ExchangeRate.objects.all()
    template_name = 'home/exchange_rate_table.html'


class PostList(ListView):
    queryset = Post.objects.filter(status=1).order_by('creation_date')[:4]
    template_name = 'home/homepage.html'


class PostDetail(DetailView):
    model = Post
    template_name = 'home/post_detail.html'
