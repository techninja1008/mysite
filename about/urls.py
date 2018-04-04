from django.urls import path

from . import views

app_name = 'about'
urlpatterns = [
    path('links/', views.LinksView.as_view(), name='links'),
    path('', views.AboutView.as_view(), name='about'),
]

