from django.shortcuts import render

from blogs.models import Post
from .models import *
# Create your views here.

def main_page(request):
    company=Company.objects.get()

    posts=Post.objects.all().order_by('-created_at')[:3]
    links=SocialLinks.objects.all()
    context={
        "company":company,
        "posts":posts,
        'links':links
    }
    return render(request, 'home.html',context=context)




def contact_page(request):
    notify={
        "class":"",
        "message":""
    }
    if request.method == 'POST':
        name=request.POST.get("name")
        email=request.POST.get("email")
        subject=request.POST.get("subject")
        message=request.POST.get("message")
        if(name=="" or email=="" or subject=="" or message==""):
            notify={
                "class":"danger",
                "message":"Please fill all required fields!!"
            }
        else:
            ContactUs.objects.create(
                full_name=name,
                email=email,
                subject=subject,
                message=message
            )
            notify={
                "class":"success",
                "message":"Thank you for contacting us! We'll get back to you soon."
            }
        # return redirect(reverse('blogs:blog_details',args=[pk]))

    company=Company.objects.get()

    address=company.address.split("\n")
    links=SocialLinks.objects.all()

    context={
        "company":company,
        "address":address,
        'links':links,
        "notify":notify

    }
    return render(request, 'contact.html',context=context)



def about_page(request):
    company=Company.objects.get()

    links=SocialLinks.objects.all()

    context={
        "company":company,
        'links':links

    }
    return render(request, 'about.html',context=context)
