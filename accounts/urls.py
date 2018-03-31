from django.contrib.auth import views as auth_views
from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('new/', views.new_account, name='new'),
    path('edit/', views.edit_account, name='edit'),
    path('profile/', views.my_account, name='me'),
    path('profile/<pk>/', views.UserInfoView.as_view(), name='view'),
    path('profile/<pk>/blog/', views.UserBlogInfoView.as_view(), name='view_blog'),
    path('login/', auth_views.login, {'template_name': 'accounts/login.html'}, name='login'),
    path('logout/', auth_views.logout, {'template_name': 'accounts/logout.html'}, name='logout'),
]
