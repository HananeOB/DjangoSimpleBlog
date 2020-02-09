from django.views import generic
from .models import Post
from taggit.models import Tag
from django.template.defaultfilters import slugify
from django.shortcuts import render, get_object_or_404
from django.views.generic.list import ListView



class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'

class ListByTag(generic.ListView):
    model = Post
    template_name = "index.html"
    ordering = ("-published_date",)
    def get_queryset(self):
        tag = self.kwargs.get("tag", None)
        results = []
        if tag:
            results = Post.objects.filter(tags__name=tag)
        return results
       

