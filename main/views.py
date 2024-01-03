from django.shortcuts import render

# Create your views here.

def main_page(request):
    context={
        
    }
    return render(request, 'index.html',context=context)


def blogs_page(request):
    context={
        
    }
    return render(request, 'blogs.html',context=context)


