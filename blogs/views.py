from django.shortcuts import render, get_object_or_404,redirect

from main.models import Company, SocialLinks
# Create your views here.
from .models import *

import django_filters
from django.urls import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

class PostFilter(django_filters.FilterSet):
    tag = django_filters.CharFilter(field_name='tags__name', lookup_expr='exact')
    search=django_filters.CharFilter(field_name='title', lookup_expr='contains')
    class Meta:
        model = Post
        fields = []

def blogs_page(request):

    posts=Post.objects.all().order_by('-created_at')
    tags=Tag.objects.all()

    posts_per_page = 3

    page= request.GET.get('page', 1)
    filter = PostFilter(request.GET,queryset=posts)
    # print(filter.qs)
    paginator = Paginator(filter.qs, posts_per_page)

    try:
        paginated_items = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver the first page
        paginated_items = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g., 9999), deliver the last page
        paginated_items = paginator.page(paginator.num_pages)

    company=Company.objects.get()
 
    links=SocialLinks.objects.all()
    
    context={
        "tags":tags,
        "posts":paginated_items,
        "company":company,
        'links':links,

    }
    return render(request, 'blogs.html',context=context)


def add_comment(request,pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':       
        if request.user.is_authenticated:
            commenter, created=Commenter.objects.get_or_create(
                user=request.user,
                defaults={'user':request.user}
            )
            comment=Comment.objects.create(
                post=post,
                commenter=commenter,
                content=request.POST.get('content')
            )

        else:
            # not logged in user
            commenter=Commenter.objects.create(
                name=request.POST.get('name'),
                email=request.POST.get('email')
            )
            comment=Comment.objects.create(
                post=post,
                commenter=commenter,
                content=request.POST.get('content')
            )

    return redirect(reverse('blogs:blog_details',args=[pk]))

    
def blog_details(request,pk):
    post = get_object_or_404(Post, pk=pk)
    tags=Tag.objects.all()
    company=Company.objects.get()
    links=SocialLinks.objects.all()

    context={
        "post":post,
        "tags":tags,
        "company":company,
        'links':links,

    }
    return render(request, 'blogs-details.html',context=context)
