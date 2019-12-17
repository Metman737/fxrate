from django.views.generic import DetailView
from blog.models import Post


class PostDetail(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'


class ExchangeRateOverview( object ):
    pass