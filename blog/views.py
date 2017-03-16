from django.shortcuts import render


def blog_list(request):
    return render(request, template_name='blog/blog_list.html')
