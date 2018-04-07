from django.urls import path
from . import views

app_name = 'mail'
urlpatterns = [
    path('send/', views.SendMailView.as_view(), name='send'),
]
