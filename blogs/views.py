from django.shortcuts import render, get_object_or_404
# Create your views here.
from .models import *

import django_filters

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

class PostFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(field_name='title', lookup_expr='exact')
    class Meta:
        model = Post
        fields = []

def blogs_page(request):

    posts=Post.objects.all().order_by('-created_at')
    tags=Tag.objects.all()

    posts_per_page = 4

    page= request.GET.get('page', 1)
    filter = PostFilter(request.GET,queryset=posts)
    paginator = Paginator(filter.qs, posts_per_page)


    try:
        paginated_items = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver the first page
        paginated_items = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g., 9999), deliver the last page
        paginated_items = paginator.page(paginator.num_pages)


    context={
        # "posts":paginated_items,
        "tags":tags,
        "posts":paginated_items,

    }
    return render(request, 'blogs.html',context=context)

def blog_details(request,pk):
    post = get_object_or_404(Post, pk=pk)
    tags=Tag.objects.all()

    context={
        "post":post,
        "tags":tags

    }
    return render(request, 'blogs-details.html',context=context)
