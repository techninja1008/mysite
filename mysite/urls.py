"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.contrib.sitemaps.views import sitemap
from django.contrib.sitemaps import GenericSitemap
from blog.models import Post
from sites.models import Site
from time import time
post_dict = {
        'queryset': Post.objects.all(),
            'date_field': 'published_date'
}
sites_dict = {
    'queryset': Site.objects.all(),
}
sitemaps = {
        'blog': GenericSitemap(post_dict, priority=0.6),
        'home': GenericSitemap(sites_dict, priority=0.7),
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    path('accounts/', include('accounts.urls')),
    path('search/', include('search.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('about/', include('about.urls')),
    path('danny/', include('birthday.urls')),
    path('mail/', include('mail.urls')),
    path('contact/', include('contact.urls')),
    path('', include('home.urls')),
]
