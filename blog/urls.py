from django.conf.urls import url
from django.views.generic import ListView, DetailView
from blog.models import Blog

urlpatterns = [
    url(r'^$', ListView.as_view(queryset = Blog.objects.all().order_by('-date')[:25], template_name = 'blog/blog_list.html')),
    url(r'^(?P<pk>[0-9]+)$', DetailView.as_view(model = Blog, template_name = 'blog/blog_details.html')),
]