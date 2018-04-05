from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.utils import timezone
from blog.models import Post

from .models import Details

class CustomView():
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(self.get_more_context())
        context.update({
            'nav_links': [
                {'text': "Home", 'href': reverse('home:index')},
                {'text': "About", 'href': reverse('about:about')},
                {'text': "Links", 'href': reverse('about:links')},
                {'text': "Blog", 'href': reverse('blog:post_list')}
            ],
            'can_post': self.request.user.has_perm('blog.add_post')
            })

        return context

class IndexView(CustomView, generic.ListView):
    template_name = 'home/index.html'
    context_object_name = 'posts'

    def get_more_context(self):
        return {
            'title': 'Home',
            'welcome_msg': Details.objects.all().first().welcome_msg 
            }

    def get_queryset(self):
        posts = [
            Post.objects.order_by('-published_date')[:3],
            Post.objects.order_by('-published_date')[3:6],
            Post.objects.order_by('-published_date')[6:9],
            ]
        return posts
    

