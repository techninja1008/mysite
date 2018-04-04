from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.utils import timezone
from blog.models import Post
from home.views import CustomView
from .models import Content, Link


class AboutView(CustomView, generic.ListView):
    template_name = 'about/index.html'
    context_object_name = 'content'

    def get_more_context(self):
        return {
            'title': 'About',
            }

    def get_queryset(self):
        content = Content.objects.all()
        return content
    

class LinksView(CustomView, generic.ListView):
    template_name = 'about/links.html'
    context_object_name = 'links'
    model = Link

    def get_more_context(self):
        return {'title': "links"}

