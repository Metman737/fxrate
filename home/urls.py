from django.urls import path

from home import views

app_name = 'service'
urlpatterns = [
    path('', views.index, name='index'),
    path('exchange-rate-table', views.table_detail, name='exchange-rate-detail'),
]