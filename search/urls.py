from django.urls import path
from django.views.generic import RedirectView

from . import views

app_name = 'search'
urlpatterns = [
    path('', views.SearchView.as_view(), name='query'),
]
