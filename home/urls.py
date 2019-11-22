from django.urls import path

from home import views

app_name = 'service'
urlpatterns = [
    path('', views.index, name='index'),
]