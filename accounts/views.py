from django.shortcuts import render, redirect
from .forms import LoginForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from accounts.models import UserProfile
from django.views import generic
from home.views import CustomView
from blog.models import Post
from django.contrib.auth.decorators import login_required


def new_account(request):
    return HttpResponse("new account")

def edit_account(request):
    return HttpResponse("edit account")

@login_required
def my_account(request):
    return redirect('accounts:view', pk=request.user.pk)

class UserInfoView(CustomView, generic.DetailView):
    model = UserProfile
    template_name = 'accounts/profile.html'
    
    def get_more_context(self):
        return {'title': "profile", 'page': "info"}


class UserBlogInfoView(CustomView, generic.ListView):
    model = UserProfile
    context_object_name = 'posts'
    template_name = 'accounts/profile.html'

    def get_queryset(self):
        qs = Post.objects.all().filter(author_id=self.kwargs['pk'])
        return qs
    def get_more_context(self):
        return {'title': "profile", 'page': "blog", 'user': UserProfile.objects.filter(pk=self.kwargs['pk']).first()}


