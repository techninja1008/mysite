from django.urls import path
from django.views.generic import RedirectView

from . import views

app_name = 'home'
urlpatterns = [
    path('links/', views.LinksView.as_view(), name='links'),
    path('<page>/', views.IndexView.as_view(), name='index'),
    path('', RedirectView.as_view(url='/home')),
]

