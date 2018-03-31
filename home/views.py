from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.utils import timezone

from .models import Content, Page, Link

class CustomView():
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(self.get_more_context())
        context.update({
            'nav_links': [
                {'text': "Home", 'href': reverse('home:index', args=['home'])},
                {'text': "About", 'href': reverse('home:index', args=['about'])},
                {'text': "Links", 'href': reverse('home:links')},
                {'text': "Blog", 'href': reverse('blog:post_list')}
            ]})

        return context

class IndexView(CustomView, generic.ListView):
    template_name = 'home/index.html'
    context_object_name = 'content'

    def get_more_context(self):
        return {'title': self.kwargs['page']}

    def get_queryset(self):
        page = get_object_or_404(Page, page=self.kwargs['page']).id
        return Content.objects.filter(page=page)
    

class LinksView(CustomView, generic.ListView):
    template_name = 'home/links.html'
    context_object_name = 'links'
    model = Link

    def get_more_context(self):
        return {'title': "links"}

