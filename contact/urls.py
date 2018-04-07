from django.urls import path, re_path
from . import views

app_name = 'contact'
urlpatterns = [
    path('thankyou/', views.thankyou, name="thankyou"),
    re_path(r'^$', views.ContactView.as_view(), name='contact'),
]
