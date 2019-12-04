from django.urls import path

from home import views

app_name = 'service'
urlpatterns = [
    path('', views.index, name='home'),
    path('<slug:slug>/', views.PostAsDatail.as_view(), name='post_detail'),
    path('exchange-rate-table', views.table_detail, name='exchange-rate-detail'),
]