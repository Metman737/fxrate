from django.db.models import Max, Subquery, OuterRef, Prefetch
from django.views.generic import DetailView, ListView

from home.models import Post, ExchangeRate, Currency


class PostList(ListView):
    queryset = Post.objects.filter(status=1).order_by('creation_date')[:4]
    template_name = 'home/homepage.html'


class PostDetail(DetailView):
    model = Post
    template_name = 'home/post_detail.html'


class ExchangeRateTable(ListView):
    # finds the latest exchangerate row for each currency
    # TODO: Disable caching
    # TODO: Find django method instead of SQL query
    queryset = ExchangeRate.objects.raw( '''SELECT c.*, e1.*
    FROM home_currency c
    JOIN home_exchangerate e1 ON (c.id = e1.currency_id)
    LEFT OUTER JOIN home_exchangerate e2 ON (c.id = e2.currency_id AND 
        (e1.change_date_time < e2.change_date_time OR (e1.change_date_time = e2.change_date_time AND e1.id < e2.id)))
    WHERE e2.id IS NULL''' )

    template_name = 'home/exchange_rate_table.html'
