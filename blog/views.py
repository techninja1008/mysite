from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.utils import timezone
from home.views import CustomView
from .models import Post
from .forms import PostForm
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

class PostListView(CustomView, generic.ListView):
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
     
    def get_more_context(self):
        return {'title': "blog"}

    def get_queryset(self):
        posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
        return posts

class PostDetailView(CustomView, generic.DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    def get_more_context(self):
        return {'title': "blog"}

class NewPostView(LoginRequiredMixin, CustomView, generic.edit.FormView):
    template_name = 'blog/post_edit.html'
    form_class = PostForm
    success_url = reverse_lazy('blog:post_list')

    def form_valid(self, form):
        if super().form_valid(form):
            post = form.save(commit=False)
            post.author = self.request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('blog:post_detail', pk=post.pk)
    
    def get_more_context(self):
        return {'title': "blog"}
    
class EditPostView(LoginRequiredMixin, CustomView, generic.edit.UpdateView):
    template_name = 'blog/post_edit.html'
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('blog:post_list')

    def get_more_context(self):
        return {'title': "blog"}

    def form_valid(self, form):
        if super().form_valid(form):
            post = form.save(commit=False)
            post.author = self.request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('blog:post_detail', pk=post.pk)


