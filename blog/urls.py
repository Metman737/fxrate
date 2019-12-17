from django.urls import path

from blog import views

app_name = 'blog'
urlpatterns = [
    path('<slug:slug>/', views.PostDetail.as_view(), name='post-detail'),
]
