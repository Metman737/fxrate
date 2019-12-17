from django.urls import path

from exchange import views

app_name = 'exchange'
urlpatterns = [
    path('overview/', views.ExchangeRateOverview.as_view(), name='overview'),
]
