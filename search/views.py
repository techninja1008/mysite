from django.contrib.postgres.search import SearchVector
from blog.models import Post
from django.views.generic.list import ListView
from home.views import CustomView

class SearchView(CustomView, ListView):
    context_object_name = 'results'
    template_name = 'search/results.html'
    def get_more_context(self):
        return {'title': 'search', 'query': self.request.GET['q']}

    def get_queryset(self):
        return Post.objects.annotate(search=SearchVector('title', 'body')).filter(search=self.request.GET['q'])   

