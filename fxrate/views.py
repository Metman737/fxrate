from django.shortcuts import redirect
from django.views.generic import ListView

from blog.models import Post


class Homepage(ListView):
    queryset = Post.objects.filter(status=1).order_by('creation_date')[:4]
    template_name = 'homepage.html'
