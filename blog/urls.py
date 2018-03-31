from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('post/new/', views.NewPostView.as_view(), name='post_new'),
    path('post/<pk>/edit/', views.EditPostView.as_view(), name='post_edit'),
    path('post/<pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('', views.PostListView.as_view(), name='post_list'),
]
