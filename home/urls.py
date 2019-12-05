from django.urls import path

from home import views

app_name = 'home'
urlpatterns = [
    path('', views.PostList.as_view(), name='homepage'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('exchange-rate-table', views.ExchangeRateTable.as_view(), name='exchange_rate_table'),
]
