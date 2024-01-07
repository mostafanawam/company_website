from django.shortcuts import render

# Create your views here.

def main_page(request):
    context={}
    return render(request, 'home.html',context=context)




def contact_page(request):
    context={}
    return render(request, 'contact.html',context=context)



def about_page(request):
    context={}
    return render(request, 'about.html',context=context)
